#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正KTH78系列产品文档中的图片引用问题
将所有无效的图片引用替换为文本说明
"""

import os
import re
from pathlib import Path

def fix_kth78_images():
    """修正KTH78系列产品文档中的图片引用"""
    
    # 文档目录
    docs_dir = Path('/Users/mac/Documents/VerySync/VerySync_Work/0705_vitpress_conntek/docs/products/KTH78xx')
    
    # 需要处理的文件模式
    kth78_files = list(docs_dir.glob('KTH78*.md'))
    
    # 图片替换规则
    replacements = [
        # 产品外观图片
        (r'### 产品外观\n\n(?:!\[.*?\]\(/kth\d+/.*?\)\n\n?)*', 
         '### 产品外观\n\n*产品外观图片请参考产品数据手册*\n\n'),
        
        # 应用电路原理图
        (r'### 应用电路原理图\n\n(?:!\[.*?\]\(/kth\d+/.*?\)\n\n?)*',
         '### 应用电路原理图\n\n*应用电路原理图请参考产品数据手册*\n\n'),
        
        # 引脚结构图
        (r'### 引脚结构图（俯视图）\n\n(?:!\[.*?\]\(/kth\d+/.*?\)\n\n?)*',
         '### 引脚结构图（俯视图）\n\n*引脚结构图请参考产品数据手册*\n\n'),
        
        # 功能框图
        (r'### 功能框图\n\n(?:!\[.*?\]\(/kth\d+/.*?\)\n\n?)*',
         '### 功能框图\n\n*功能框图请参考产品数据手册*\n\n'),
        
        # 产品型号构成图
        (r'!\[产品型号构成\]\(/kth\d+/.*?\)\n\*KTH\d+产品型号构成说明\*',
         '*产品型号构成说明请参考产品数据手册*'),
        
        # 封装尺寸图
        (r'### 封装尺寸图\n\n!\[封装尺寸图\]\(/kth\d+/.*?\)\n\*KTH\d+封装详细尺寸图\*',
         '### 封装尺寸图\n\n*封装尺寸图请参考产品数据手册*'),
        
        # 推荐焊盘尺寸
        (r'### 推荐焊盘尺寸\n\n!\[推荐焊盘尺寸\]\(/kth\d+/.*?\)\n\*推荐的PCB焊盘设计\*',
         '### 推荐焊盘尺寸\n\n*推荐焊盘尺寸请参考产品数据手册*'),
        
        # 其他单独的图片引用
        (r'!\[.*?\]\(/kth\d+/.*?\)',
         '*相关图片请参考产品数据手册*')
    ]
    
    processed_files = []
    
    for file_path in kth78_files:
        if file_path.name == 'index.md':
            continue
            
        print(f"处理文件: {file_path.name}")
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用替换规则
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            # 创建备份
            backup_path = file_path.with_suffix('.md.image_fix_backup')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # 写入修正后的内容
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            processed_files.append(file_path.name)
            print(f"  ✓ 已修正图片引用")
        else:
            print(f"  - 无需修正")
    
    print(f"\n处理完成！共修正了 {len(processed_files)} 个文件的图片引用：")
    for filename in processed_files:
        print(f"  - {filename}")
    
    if processed_files:
        print("\n所有修正前的内容已备份为 .image_fix_backup 文件")

if __name__ == '__main__':
    fix_kth78_images()