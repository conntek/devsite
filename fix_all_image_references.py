#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正所有产品文档中的图片引用问题
将所有无效的图片引用替换为文本说明
"""

import os
import re
from pathlib import Path
import shutil

def fix_all_image_references():
    """修正所有产品文档中的图片引用"""
    
    # 文档目录
    docs_dir = Path('/Users/mac/Documents/VerySync/VerySync_Work/0705_vitpress_conntek/docs/products')
    
    # 需要处理的系列
    series_patterns = [
        'KTH16xx/*.md',
        'KTH17xx/*.md', 
        'KTH25xx/*.md',
        'KTH31xx/*.md',
        'KTH46xx/*.md',
        'KTH56xx/*.md',
        'KTH57xx/*.md',
        'KTH78xx/*.md',
        'KTM13xx/*.md',
        'KTM58xx/*.md',
        'KTAX333/*.md',
        'KTP112/*.md'
    ]
    
    # 收集所有需要处理的文件
    files_to_process = []
    for pattern in series_patterns:
        files_to_process.extend(docs_dir.glob(pattern))
    
    # 过滤掉备份文件
    files_to_process = [f for f in files_to_process if not f.name.endswith('.backup') and not f.name.endswith('.precise_backup')]
    
    print(f"找到 {len(files_to_process)} 个文件需要处理")
    
    # 图片替换规则
    replacements = [
        # 产品外观图片
        (r'### 产品外观\n\n(?:!\[.*?\]\(/[^)]+\)\n\n?)*', 
         '### 产品外观\n\n*产品外观图片请参考产品数据手册*\n\n'),
        
        # 应用电路原理图
        (r'### 应用电路原理图\n\n(?:!\[.*?\]\(/[^)]+\)\n\n?)*',
         '### 应用电路原理图\n\n*应用电路原理图请参考产品数据手册*\n\n'),
        
        # 引脚结构图
        (r'### 引脚结构图（俯视图）\n\n(?:!\[.*?\]\(/[^)]+\)\n\n?)*',
         '### 引脚结构图（俯视图）\n\n*引脚结构图请参考产品数据手册*\n\n'),
        
        # 功能框图
        (r'### 功能框图\n\n(?:!\[.*?\]\(/[^)]+\)\n\n?)*',
         '### 功能框图\n\n*功能框图请参考产品数据手册*\n\n'),
        
        # 产品型号构成图
        (r'!\[产品型号构成\]\(/[^)]+\)\n\*[^*]+产品型号构成说明\*',
         '*产品型号构成说明请参考产品数据手册*'),
        
        # 封装尺寸图
        (r'### 封装尺寸图\n\n!\[封装尺寸图\]\(/[^)]+\)\n\*[^*]+封装详细尺寸图\*',
         '### 封装尺寸图\n\n*封装尺寸图请参考产品数据手册*'),
        
        # 推荐焊盘尺寸
        (r'### 推荐焊盘尺寸\n\n!\[推荐焊盘尺寸\]\(/[^)]+\)\n\*[^*]+推荐焊盘尺寸\*',
         '### 推荐焊盘尺寸\n\n*推荐焊盘尺寸请参考产品数据手册*'),
        
        # 通用图片引用（匹配所有剩余的图片引用）
        (r'!\[[^\]]*\]\(/[^)]+\)',
         '*相关图片请参考产品数据手册*')
    ]
    
    processed_files = []
    
    for file_path in files_to_process:
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否包含图片引用
            if '![' not in content or '](/kth' not in content.lower():
                continue
                
            # 创建备份
            backup_path = file_path.with_suffix(file_path.suffix + '.image_fix_backup')
            shutil.copy2(file_path, backup_path)
            
            # 应用替换规则
            original_content = content
            for pattern, replacement in replacements:
                content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            
            # 如果内容有变化，保存文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                processed_files.append(file_path.name)
                print(f"✅ 修正: {file_path.relative_to(docs_dir)}")
            else:
                # 如果没有变化，删除备份文件
                backup_path.unlink()
                
        except Exception as e:
            print(f"❌ 处理文件 {file_path} 时出错: {e}")
    
    print(f"\n🎉 处理完成！")
    print(f"📝 共修正了 {len(processed_files)} 个文件:")
    for file_name in processed_files:
        print(f"   - {file_name}")
    
    if processed_files:
        print(f"\n💾 备份文件已创建，文件名后缀为 .image_fix_backup")

if __name__ == "__main__":
    fix_all_image_references()