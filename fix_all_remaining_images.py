#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正所有剩余的图片引用问题
"""

import os
import re
import shutil
from pathlib import Path

def fix_image_references_in_file(file_path):
    """修正单个文件中的图片引用"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 定义图片引用的替换规则
        replacements = [
            # 产品外观相关图片
            (r'!\[([^\]]*产品外观[^\]]*)\]\([^)]+\)', r'**产品外观图**\n*产品外观图请参考产品数据手册*'),
            (r'!\[([^\]]*外观[^\]]*)\]\([^)]+\)', r'**产品外观图**\n*产品外观图请参考产品数据手册*'),
            
            # 应用电路相关图片
            (r'!\[([^\]]*应用电路[^\]]*)\]\([^)]+\)', r'**应用电路原理图**\n*应用电路原理图请参考产品数据手册*'),
            (r'!\[([^\]]*电路[^\]]*)\]\([^)]+\)', r'**应用电路原理图**\n*应用电路原理图请参考产品数据手册*'),
            
            # 引脚相关图片
            (r'!\[([^\]]*引脚[^\]]*)\]\([^)]+\)', r'**引脚结构图**\n*引脚结构图请参考产品数据手册*'),
            (r'!\[([^\]]*配置[^\]]*)\]\([^)]+\)', r'**引脚配置图**\n*引脚配置图请参考产品数据手册*'),
            
            # 功能框图
            (r'!\[([^\]]*功能框图[^\]]*)\]\([^)]+\)', r'**功能框图**\n*功能框图请参考产品数据手册*'),
            (r'!\[([^\]]*框图[^\]]*)\]\([^)]+\)', r'**功能框图**\n*功能框图请参考产品数据手册*'),
            
            # 磁场特性图
            (r'!\[([^\]]*磁场[^\]]*)\]\([^)]+\)', r'**磁场特性图**\n*磁场特性图请参考产品数据手册*'),
            (r'!\[([^\]]*特性[^\]]*)\]\([^)]+\)', r'**磁场特性图**\n*磁场特性图请参考产品数据手册*'),
            
            # 产品型号构成
            (r'!\[([^\]]*产品型号构成[^\]]*)\]\([^)]+\)', r'**产品型号构成图**\n*产品型号构成图请参考产品数据手册*'),
            (r'!\[([^\]]*型号构成[^\]]*)\]\([^)]+\)', r'**产品型号构成图**\n*产品型号构成图请参考产品数据手册*'),
            
            # 封装尺寸图
            (r'!\[([^\]]*封装尺寸[^\]]*)\]\([^)]+\)', r'**封装尺寸图**\n*封装尺寸图请参考产品数据手册*'),
            (r'!\[([^\]]*尺寸[^\]]*)\]\([^)]+\)', r'**封装尺寸图**\n*封装尺寸图请参考产品数据手册*'),
            
            # 推荐焊盘尺寸
            (r'!\[([^\]]*推荐焊盘[^\]]*)\]\([^)]+\)', r'**推荐焊盘尺寸图**\n*推荐焊盘尺寸图请参考产品数据手册*'),
            (r'!\[([^\]]*焊盘[^\]]*)\]\([^)]+\)', r'**推荐焊盘尺寸图**\n*推荐焊盘尺寸图请参考产品数据手册*'),
            
            # 通用图片引用（以产品型号开头的图片）
            (r'!\[([A-Z]+\d+[A-Z]*\s*图片\s*\d+)\]\([^)]+\)', r'**产品图片**\n*产品图片请参考产品数据手册*'),
            
            # 其他所有以 / 开头的图片引用
            (r'!\[([^\]]*)\]\(/[^)]+\)', r'**相关图片**\n*相关图片请参考产品数据手册*'),
        ]
        
        # 应用替换规则
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        # 如果内容有变化，则写入文件并创建备份
        if content != original_content:
            # 创建备份文件
            backup_path = file_path + '.image_fix_backup'
            if not os.path.exists(backup_path):
                shutil.copy2(file_path, backup_path)
            
            # 写入修正后的内容
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
        
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    docs_dir = Path('/Users/mac/Documents/VerySync/VerySync_Work/0705_vitpress_conntek/docs')
    
    if not docs_dir.exists():
        print(f"错误：目录 {docs_dir} 不存在")
        return
    
    # 查找所有 .md 文件（排除备份文件）
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md') and not any(backup in file for backup in ['.backup', '.precise_backup', '.final_backup', '.image_fix_backup']):
                md_files.append(os.path.join(root, file))
    
    print(f"找到 {len(md_files)} 个 Markdown 文件")
    
    fixed_count = 0
    total_files = len(md_files)
    
    for i, file_path in enumerate(md_files, 1):
        print(f"处理文件 {i}/{total_files}: {os.path.relpath(file_path, docs_dir)}")
        
        if fix_image_references_in_file(file_path):
            fixed_count += 1
            print(f"  ✓ 已修正图片引用")
    
    print(f"\n处理完成！")
    print(f"总共处理了 {total_files} 个文件")
    print(f"修正了 {fixed_count} 个文件的图片引用")
    print(f"为每个修正的文件创建了 .image_fix_backup 备份")

if __name__ == '__main__':
    main()