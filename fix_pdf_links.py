#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有PDF链接的脚本
问题：
1. 路径分隔符使用了反斜杠（\）而不是正斜杠（/）
2. 路径中包含中文字符、空格和特殊字符需要URL编码
"""

import os
import re
from urllib.parse import quote
from pathlib import Path

def url_encode_path(path):
    """对路径进行URL编码，但保留路径分隔符"""
    # 将反斜杠替换为正斜杠
    path = path.replace('\\', '/')
    
    # 分割路径并对每个部分进行编码
    parts = path.split('/')
    encoded_parts = []
    
    for part in parts:
        if part:  # 跳过空字符串
            # 对每个路径部分进行URL编码
            encoded_part = quote(part, safe='')
            encoded_parts.append(encoded_part)
        else:
            encoded_parts.append('')
    
    return '/'.join(encoded_parts)

def fix_pdf_links_in_file(file_path):
    """修复单个文件中的PDF链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找所有PDF链接的模式
        # 匹配格式：[文本](路径.pdf)
        pdf_pattern = r'\[([^\]]+)\]\(([^\)]+\.pdf)\)'
        
        def replace_link(match):
            link_text = match.group(1)
            link_path = match.group(2)
            
            # 修复路径
            fixed_path = url_encode_path(link_path)
            
            return f'[{link_text}]({fixed_path})'
        
        # 替换所有PDF链接
        new_content = re.sub(pdf_pattern, replace_link, content)
        
        # 如果内容有变化，写回文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已修复: {file_path}")
            return True
        else:
            print(f"⏭️  无需修复: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 处理文件时出错 {file_path}: {e}")
        return False

def find_and_fix_all_pdf_links(docs_dir):
    """查找并修复所有Markdown文件中的PDF链接"""
    docs_path = Path(docs_dir)
    fixed_count = 0
    total_count = 0
    
    # 查找所有.md文件
    for md_file in docs_path.rglob('*.md'):
        total_count += 1
        if fix_pdf_links_in_file(md_file):
            fixed_count += 1
    
    print(f"\n📊 修复完成统计:")
    print(f"   总文件数: {total_count}")
    print(f"   已修复文件数: {fixed_count}")
    print(f"   无需修复文件数: {total_count - fixed_count}")

if __name__ == '__main__':
    # 设置docs目录路径
    docs_directory = 'docs'
    
    print("🔧 开始修复PDF链接...")
    print(f"📁 扫描目录: {os.path.abspath(docs_directory)}")
    print("="*50)
    
    find_and_fix_all_pdf_links(docs_directory)
    
    print("="*50)
    print("✨ PDF链接修复完成！")
    print("\n修复内容:")
    print("1. 将路径分隔符从反斜杠（\\）改为正斜杠（/）")
    print("2. 对路径中的中文字符、空格和特殊字符进行URL编码")
    print("\n现在所有PDF链接应该可以正常访问了！")