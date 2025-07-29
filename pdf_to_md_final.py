#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终版PDF到Markdown转换器，集成图片质量检测
自动过滤全黑和低质量图片
"""

import pymupdf4llm
import fitz  # PyMuPDF
import os
from pathlib import Path
import numpy as np
from PIL import Image

def is_valid_image_advanced(pix):
    """
    高级图片质量检测
    """
    try:
        # 基本检查
        if not pix or pix.width < 50 or pix.height < 50:
            return False, "图片太小"
        
        # 获取像素数据
        samples = pix.samples
        if not samples:
            return False, "无像素数据"
        
        # 转换为numpy数组进行分析
        pixel_data = np.frombuffer(samples, dtype=np.uint8)
        
        # 重塑数组
        if pix.n == 1:  # 灰度图
            img_array = pixel_data.reshape(pix.height, pix.width)
            gray = img_array
        elif pix.n == 3:  # RGB
            img_array = pixel_data.reshape(pix.height, pix.width, 3)
            # 计算灰度值
            gray = np.dot(img_array, [0.2989, 0.5870, 0.1140])
        elif pix.n == 4:  # RGBA
            img_array = pixel_data.reshape(pix.height, pix.width, 4)
            # 计算灰度值（忽略alpha通道）
            gray = np.dot(img_array[:,:,:3], [0.2989, 0.5870, 0.1140])
        else:
            return False, f"不支持的颜色通道数: {pix.n}"
        
        # 统计分析
        mean_brightness = np.mean(gray)
        std_brightness = np.std(gray)
        min_brightness = np.min(gray)
        max_brightness = np.max(gray)
        
        # 计算黑色像素比例
        black_pixels = np.sum(gray < 20)
        total_pixels = gray.size
        black_ratio = black_pixels / total_pixels
        
        # 质量检查规则
        if black_ratio > 0.95:
            return False, f"95%以上为黑色 (黑色比例: {black_ratio:.1%})"
        
        if mean_brightness < 5:
            return False, f"平均亮度过低 (亮度: {mean_brightness:.1f})"
        
        if std_brightness < 2:
            return False, f"亮度变化过小 (标准差: {std_brightness:.1f})"
        
        if max_brightness - min_brightness < 10:
            return False, f"亮度范围过小 (范围: {max_brightness - min_brightness:.1f})"
        
        # 检查颜色多样性
        unique_values = len(np.unique(gray.flatten()[:1000]))  # 采样检查
        if unique_values < 5:
            return False, f"颜色过于单一 (唯一值: {unique_values})"
        
        return True, f"质量良好 (亮度: {mean_brightness:.1f}, 标准差: {std_brightness:.1f}, 黑色: {black_ratio:.1%})"
        
    except Exception as e:
        return False, f"分析失败: {e}"

def extract_images_from_pdf(pdf_path, output_dir):
    """
    从PDF提取高质量图片
    """
    doc = fitz.open(pdf_path)
    images_info = []
    
    # 创建图片目录
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    total_extracted = 0
    total_skipped = 0
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images()
        
        for img_index, img in enumerate(image_list):
            try:
                # 获取图片数据
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                
                # 转换CMYK到RGB
                if pix.n - pix.alpha >= 4:  # CMYK
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                
                # 高级质量检测
                is_valid, reason = is_valid_image_advanced(pix)
                
                if not is_valid:
                    print(f"跳过第{page_num+1}页第{img_index+1}张图片: {reason}")
                    total_skipped += 1
                    pix = None
                    continue
                
                # 生成文件名
                img_filename = f"page_{page_num+1}_img_{img_index+1}.png"
                img_path = os.path.join(images_dir, img_filename)
                
                # 保存图片
                pix.save(img_path)
                total_extracted += 1
                
                images_info.append({
                    'page': page_num + 1,
                    'filename': img_filename,
                    'path': img_path,
                    'relative_path': f"images/{img_filename}",
                    'quality_info': reason
                })
                
                print(f"✓ 第{page_num+1}页第{img_index+1}张图片: {reason}")
                
                pix = None
                
            except Exception as e:
                print(f"跳过第{page_num+1}页第{img_index+1}张图片: {e}")
                total_skipped += 1
                continue
    
    doc.close()
    print(f"\n图片提取完成: 成功 {total_extracted} 张, 跳过 {total_skipped} 张")
    return images_info

def convert_pdf_to_markdown_with_images(pdf_path, output_dir):
    """
    转换PDF为Markdown并提取高质量图片
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 提取图片
    print("正在提取高质量图片...")
    images_info = extract_images_from_pdf(pdf_path, output_dir)
    
    # 转换PDF为Markdown
    print("\n正在转换PDF为Markdown...")
    markdown_content = pymupdf4llm.to_markdown(pdf_path)
    
    # 增强内容
    enhanced_content = markdown_content
    
    # 添加图片引用
    if images_info:
        image_section = "\n\n## 图片列表\n\n"
        for img in images_info:
            image_section += f"### 第{img['page']}页图片\n\n"
            image_section += f"![第{img['page']}页图片]({img['relative_path']})\n\n"
            image_section += f"*质量信息: {img['quality_info']}*\n\n"
        
        enhanced_content = image_section + enhanced_content
    
    # 保存Markdown文件
    pdf_name = Path(pdf_path).stem
    output_file = os.path.join(output_dir, f"{pdf_name}_final.md")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(enhanced_content)
    
    print(f"\n转换完成！")
    print(f"Markdown文件: {output_file}")
    print(f"图片目录: {os.path.join(output_dir, 'images')}")
    print(f"内容长度: {len(enhanced_content)} 字符")
    print(f"高质量图片数量: {len(images_info)}")
    
    return output_file, images_info

if __name__ == "__main__":
    # 配置路径
    pdf_path = "docs/resources/070504-BU4/04-温感（112系列）/KTP112_CN.pdf"
    output_dir = "test_pdf_output_ktp112"
    
    try:
        output_file, images = convert_pdf_to_markdown_with_images(pdf_path, output_dir)
        print(f"\n=== 转换总结 ===")
        print(f"PDF文件: {pdf_path}")
        print(f"输出文件: {output_file}")
        print(f"高质量图片: {len(images)} 张")
        
        if images:
            print(f"\n=== 图片质量报告 ===")
            for img in images[:5]:  # 显示前5张图片的信息
                print(f"  {img['filename']}: {img['quality_info']}")
            if len(images) > 5:
                print(f"  ... 还有 {len(images) - 5} 张图片")
        
    except Exception as e:
        print(f"转换过程中出现错误: {e}")
        import traceback
        traceback.print_exc()