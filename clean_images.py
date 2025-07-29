#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片质量检测和清理工具
检测并删除全黑、过于单一或质量差的图片
"""

import os
from PIL import Image
import numpy as np
from pathlib import Path

def analyze_image_quality(image_path):
    """
    分析图片质量
    返回: (is_valid, reason, stats)
    """
    try:
        with Image.open(image_path) as img:
            # 转换为RGB模式
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 转换为numpy数组
            img_array = np.array(img)
            
            # 基本统计信息
            height, width = img_array.shape[:2]
            total_pixels = height * width
            
            # 计算亮度（灰度值）
            gray = np.dot(img_array[...,:3], [0.2989, 0.5870, 0.1140])
            
            # 统计信息
            mean_brightness = np.mean(gray)
            std_brightness = np.std(gray)
            min_brightness = np.min(gray)
            max_brightness = np.max(gray)
            
            # 计算黑色像素比例（亮度 < 20）
            black_pixels = np.sum(gray < 20)
            black_ratio = black_pixels / total_pixels
            
            # 计算暗色像素比例（亮度 < 50）
            dark_pixels = np.sum(gray < 50)
            dark_ratio = dark_pixels / total_pixels
            
            # 计算唯一颜色数量（采样检查）
            sample_size = min(1000, total_pixels)
            flat_img = img_array.reshape(-1, 3)
            sample_indices = np.random.choice(len(flat_img), sample_size, replace=False)
            sample_colors = flat_img[sample_indices]
            unique_colors = len(np.unique(sample_colors.view(np.dtype((np.void, sample_colors.dtype.itemsize * sample_colors.shape[1])))))
            
            stats = {
                'width': width,
                'height': height,
                'mean_brightness': mean_brightness,
                'std_brightness': std_brightness,
                'min_brightness': min_brightness,
                'max_brightness': max_brightness,
                'black_ratio': black_ratio,
                'dark_ratio': dark_ratio,
                'unique_colors': unique_colors,
                'color_diversity': unique_colors / sample_size
            }
            
            # 质量检查规则
            if black_ratio > 0.95:
                return False, "图片95%以上为黑色", stats
            
            if dark_ratio > 0.98:
                return False, "图片98%以上为暗色", stats
            
            if mean_brightness < 5:
                return False, "平均亮度过低", stats
            
            if std_brightness < 2:
                return False, "亮度变化过小，图片过于单一", stats
            
            if max_brightness - min_brightness < 10:
                return False, "亮度范围过小", stats
            
            if stats['color_diversity'] < 0.01:
                return False, "颜色多样性过低", stats
            
            return True, "图片质量良好", stats
            
    except Exception as e:
        return False, f"无法分析图片: {e}", {}

def clean_images_directory(images_dir, dry_run=True):
    """
    清理图片目录中的低质量图片
    """
    if not os.path.exists(images_dir):
        print(f"目录不存在: {images_dir}")
        return
    
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    print(f"找到 {len(image_files)} 张图片")
    print(f"模式: {'预览模式（不删除文件）' if dry_run else '删除模式'}")
    print("-" * 80)
    
    valid_count = 0
    invalid_count = 0
    deleted_files = []
    
    for filename in image_files:
        image_path = os.path.join(images_dir, filename)
        is_valid, reason, stats = analyze_image_quality(image_path)
        
        if is_valid:
            valid_count += 1
            print(f"✓ {filename} - {reason}")
            if stats:
                print(f"  亮度: {stats['mean_brightness']:.1f}, 标准差: {stats['std_brightness']:.1f}, 黑色比例: {stats['black_ratio']:.2%}")
        else:
            invalid_count += 1
            print(f"✗ {filename} - {reason}")
            if stats:
                print(f"  亮度: {stats.get('mean_brightness', 0):.1f}, 标准差: {stats.get('std_brightness', 0):.1f}, 黑色比例: {stats.get('black_ratio', 0):.2%}")
            
            if not dry_run:
                try:
                    os.remove(image_path)
                    deleted_files.append(filename)
                    print(f"  已删除: {filename}")
                except Exception as e:
                    print(f"  删除失败: {e}")
    
    print("-" * 80)
    print(f"总结:")
    print(f"  有效图片: {valid_count}")
    print(f"  无效图片: {invalid_count}")
    if not dry_run:
        print(f"  已删除: {len(deleted_files)}")
    
    return deleted_files

if __name__ == "__main__":
    images_dir = "test_pdf_output/images"
    
    print("=== 图片质量分析 ===")
    print("首先进行预览分析...")
    clean_images_directory(images_dir, dry_run=True)
    
    print("\n" + "=" * 80)
    response = input("是否要删除无效图片？(y/N): ")
    
    if response.lower() == 'y':
        print("\n开始删除无效图片...")
        deleted = clean_images_directory(images_dir, dry_run=False)
        print(f"\n清理完成！删除了 {len(deleted)} 张无效图片。")
    else:
        print("\n已取消删除操作。")