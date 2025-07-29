#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版产品页面生成器 - 包含完整PDF内容和图片
为每个产品型号生成包含PDF所有文字内容和图片的详细技术参考页面
"""

import os
import re
import glob
import fitz  # PyMuPDF
import pymupdf4llm
from pathlib import Path
import hashlib
from PIL import Image
import numpy as np

class FullContentProductGenerator:
    def __init__(self, docs_dir="docs", resources_dir="docs/resources"):
        self.docs_dir = Path(docs_dir)
        self.resources_dir = Path(resources_dir)
        self.output_dir = self.docs_dir / "enhanced-products"
        self.output_dir.mkdir(exist_ok=True)
        
        # 产品分类映射
        self.category_mapping = {
            "KTH31": "3d-hall",
            "KTH57": "3d-hall", 
            "KTH74": "3d-hall",
            "KTH78": "magnetic-encoder",
            "KTM58": "magnetic-encoder",
            "KTM59": "magnetic-encoder",
            "KTH12": "hall-switch",
            "KTH13": "hall-switch",
            "KTH15": "hall-switch",
            "KTH16": "hall-switch",
            "KTH17": "hall-switch",
            "KTH25": "hall-switch",
            "KTH46": "hall-switch",
            "KTH56": "hall-switch",
            "KTM13": "hall-switch",
            "KTA": "other-sensors",
            "KTP": "other-sensors"
        }
    
    def find_product_pdfs(self, product_code):
        """查找特定产品的所有PDF文件"""
        pdf_files = []
        
        # 在resources目录下递归搜索
        for pdf_file in self.resources_dir.rglob("*.pdf"):
            filename = pdf_file.stem.upper()
            if product_code.upper() in filename:
                pdf_files.append(pdf_file)
        
        return pdf_files
    
    def extract_images_from_pdf(self, pdf_path, output_dir):
        """从PDF中提取所有图片"""
        doc = fitz.open(str(pdf_path))
        images = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    
                    if pix.n - pix.alpha < 4:  # 确保不是CMYK
                        # 生成唯一文件名
                        img_hash = hashlib.md5(pix.tobytes()).hexdigest()[:8]
                        img_filename = f"page_{page_num+1}_img_{img_index+1}_{img_hash}.png"
                        img_path = output_dir / img_filename
                        
                        # 保存图片
                        pix.save(str(img_path))
                        
                        # 检查图片质量
                        if self.is_high_quality_image(img_path):
                            images.append({
                                'filename': img_filename,
                                'page': page_num + 1,
                                'path': img_path
                            })
                        else:
                            # 删除低质量图片
                            img_path.unlink()
                    
                    pix = None
                except Exception as e:
                    print(f"  ⚠️ 图片提取失败: {e}")
                    continue
        
        doc.close()
        return images
    
    def is_high_quality_image(self, img_path, min_size=50, min_std=10):
        """检查图片质量"""
        try:
            with Image.open(img_path) as img:
                # 检查尺寸
                if img.width < min_size or img.height < min_size:
                    return False
                
                # 转换为numpy数组
                img_array = np.array(img.convert('L'))
                
                # 检查标准差（避免纯色图片）
                if np.std(img_array) < min_std:
                    return False
                
                # 检查黑色像素比例
                black_pixels = np.sum(img_array < 50)
                total_pixels = img_array.size
                black_ratio = black_pixels / total_pixels
                
                if black_ratio > 0.8:  # 超过80%是黑色
                    return False
                
                return True
        except Exception:
            return False
    
    def extract_full_text_content(self, pdf_path):
        """提取PDF的完整文字内容"""
        try:
            # 使用pymupdf4llm提取结构化内容
            md_text = pymupdf4llm.to_markdown(str(pdf_path))
            return md_text
        except Exception as e:
            print(f"  ⚠️ 文本提取失败: {e}")
            return ""
    
    def determine_category(self, product_code):
        """根据产品代码确定分类"""
        for prefix, category in self.category_mapping.items():
            if product_code.upper().startswith(prefix.upper()):
                return category
        return "other-sensors"
    
    def generate_enhanced_page(self, product_code, pdf_files):
        """生成包含完整内容的增强版产品页面"""
        if not pdf_files:
            return None
        
        # 创建产品专用图片目录
        img_dir = self.output_dir / "images" / product_code.lower()
        img_dir.mkdir(parents=True, exist_ok=True)
        
        # 提取所有PDF的内容
        all_content = []
        all_images = []
        
        for pdf_file in pdf_files:
            print(f"  📖 处理PDF: {pdf_file.name}")
            
            # 提取文字内容
            content = self.extract_full_text_content(pdf_file)
            if content:
                all_content.append({
                    'filename': pdf_file.name,
                    'content': content
                })
            
            # 提取图片
            images = self.extract_images_from_pdf(pdf_file, img_dir)
            all_images.extend(images)
        
        if not all_content:
            return None
        
        # 生成页面内容
        category = self.determine_category(product_code)
        page_content = self.create_enhanced_page_content(
            product_code, category, all_content, all_images
        )
        
        # 保存页面
        output_file = self.output_dir / f"{product_code}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        return output_file
    
    def create_enhanced_page_content(self, product_code, category, content_list, images):
        """创建增强版页面内容"""
        # 页面头部
        content = f"""# {product_code} - 完整技术参考

[返回产品目录](../index.md) | [返回{category}分类](../{category}/index.md)

## 产品概述

**{product_code}** 完整技术参考文档，包含所有PDF数据手册的详细内容和技术图片。

---

"""
        
        # 添加图片展示区域
        if images:
            content += "## 产品图片\n\n"
            for i, img in enumerate(images[:12]):  # 最多显示12张图片
                img_path = f"./images/{product_code.lower()}/{img['filename']}"
                content += f"![{product_code} 图片 {i+1}]({img_path})\n\n"
            content += "---\n\n"
        
        # 添加每个PDF的完整内容
        for i, pdf_content in enumerate(content_list):
            content += f"## 📄 {pdf_content['filename']}\n\n"
            content += "<details>\n"
            content += f"<summary>点击展开 {pdf_content['filename']} 完整内容</summary>\n\n"
            content += pdf_content['content']
            content += "\n\n</details>\n\n---\n\n"
        
        # 页面尾部
        content += f"""## 相关资源

### PDF文档
{self.generate_pdf_links(product_code)}

### 其他资源
- [产品选型指南](../technical/)
- [应用案例](../technical/)
- [技术支持](../technical/)

---

## 技术支持

如需技术支持、样品申请或定制化服务，请联系我们：

- 📧 邮箱: support@ktsense.com
- 📞 技术热线: 400-xxx-xxxx
- 🌐 在线支持: [技术论坛](../technical/)

---

*最后更新: 2024年*
*版本: Enhanced v1.0*
*包含完整PDF内容和技术图片*
"""
        
        return content
    
    def generate_pdf_links(self, product_code):
        """生成PDF文档链接"""
        pdf_files = self.find_product_pdfs(product_code)
        links = []
        
        for pdf_file in pdf_files:
            rel_path = pdf_file.relative_to(self.docs_dir)
            links.append(f"- [📋 {pdf_file.name}](../{rel_path})")
        
        return "\n".join(links) if links else "- 暂无PDF文档"
    
    def get_all_product_codes(self):
        """获取所有产品代码"""
        product_codes = set()
        
        # 从PDF文件名中提取产品代码
        for pdf_file in self.resources_dir.rglob("*.pdf"):
            filename = pdf_file.stem
            
            # 提取产品代码的正则表达式
            patterns = [
                r'(KT[HMP]\d{2,4}[A-Z]*\d*)',
                r'(KTA[A-Z]?\d{3})',
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, filename.upper())
                for match in matches:
                    product_codes.add(match)
        
        return sorted(list(product_codes))
    
    def process_all_products(self):
        """处理所有产品"""
        print("=== 增强版完整内容产品页面生成器 ===")
        
        product_codes = self.get_all_product_codes()
        print(f"发现产品数量: {len(product_codes)}")
        
        success_count = 0
        
        for product_code in product_codes:
            print(f"\n🎯 处理产品: {product_code}")
            
            # 查找PDF文件
            pdf_files = self.find_product_pdfs(product_code)
            
            if not pdf_files:
                print(f"  ❌ 未找到PDF文件")
                continue
            
            print(f"  📁 找到 {len(pdf_files)} 个PDF文件")
            
            # 生成增强页面
            try:
                output_file = self.generate_enhanced_page(product_code, pdf_files)
                if output_file:
                    print(f"  ✅ 生成增强页面: {output_file}")
                    success_count += 1
                else:
                    print(f"  ❌ 页面生成失败")
            except Exception as e:
                print(f"  ❌ 处理失败: {e}")
        
        print(f"\n🎉 处理完成!")
        print(f"✅ 成功: {success_count}/{len(product_codes)}")
        
        # 生成索引页面
        self.generate_index_page(product_codes, success_count)
    
    def generate_index_page(self, product_codes, success_count):
        """生成增强版产品索引页面"""
        index_content = f"""# 增强版产品技术参考

[返回主页](../index.md)

## 概述

本页面包含所有产品的增强版技术参考文档，每个产品页面都包含：
- 📄 完整的PDF文字内容
- 🖼️ 高质量技术图片
- 📋 详细的技术规格
- 🔗 相关资源链接

## 产品列表

共 {success_count} 个产品的增强版技术参考：

"""
        
        # 按分类组织产品
        categories = {}
        for code in product_codes:
            category = self.determine_category(code)
            if category not in categories:
                categories[category] = []
            categories[category].append(code)
        
        category_names = {
            "3d-hall": "🎯 3D霍尔传感器",
            "magnetic-encoder": "🔄 磁编码器", 
            "hall-switch": "⚡ 霍尔开关",
            "other-sensors": "🚀 其他传感器"
        }
        
        for category, codes in categories.items():
            index_content += f"\n### {category_names.get(category, category)}\n\n"
            for code in sorted(codes):
                index_content += f"- [{code}](./{code}.md)\n"
        
        index_content += f"\n\n---\n\n*生成时间: 2024年*\n*包含 {success_count} 个产品的完整技术参考*\n"
        
        # 保存索引页面
        index_file = self.output_dir / "index.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"📋 生成索引页面: {index_file}")

def main():
    generator = FullContentProductGenerator()
    generator.process_all_products()

if __name__ == "__main__":
    main()