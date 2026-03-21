#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强页面连接脚本
为产品页面和增强版页面之间建立丰富的连接关系
"""

import os
import re
from pathlib import Path

class PageConnectionEnhancer:
    def __init__(self, docs_dir="docs"):
        self.docs_dir = Path(docs_dir)
        self.enhanced_dir = self.docs_dir / "enhanced-products"
        
        # 产品分类映射
        self.category_mapping = {
            "3d-hall": "3D霍尔传感器",
            "magnetic-encoder": "磁编码器", 
            "hall-switch": "霍尔开关",
            "other-sensors": "其他传感器"
        }
        
        # 产品分类目录
        self.category_dirs = {
            "3d-hall": self.docs_dir / "3d-hall",
            "magnetic-encoder": self.docs_dir / "magnetic-encoder",
            "hall-switch": self.docs_dir / "hall-switch", 
            "other-sensors": self.docs_dir / "other-sensors"
        }
    
    def get_product_category(self, product_code):
        """根据产品代码确定分类"""
        product_code = product_code.upper()
        
        if product_code.startswith('KTH31') or product_code.startswith('KTH57') or product_code.startswith('KTH74'):
            return "3d-hall"
        elif product_code.startswith('KTH78') or product_code.startswith('KTM5'):
            return "magnetic-encoder"
        elif product_code.startswith('KTH1') or product_code.startswith('KTH2') or product_code.startswith('KTH4') or product_code.startswith('KTH5') or product_code.startswith('KTM1'):
            return "hall-switch"
        else:
            return "other-sensors"
    
    def enhance_category_index_pages(self):
        """为分类索引页面添加增强版页面链接"""
        print("正在增强分类索引页面...")
        
        for category, category_dir in self.category_dirs.items():
            index_file = category_dir / "index.md"
            if not index_file.exists():
                continue
                
            print(f"处理分类页面: {category}")
            
            # 读取现有内容
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否已经有增强版链接
            if "📖 查看增强版技术参考" in content:
                print(f"  {category} 已有增强版链接，跳过")
                continue
            
            # 在产品列表前添加增强版链接
            enhanced_section = f"""
## 📖 增强版技术参考

查看包含完整PDF内容和高质量图片的详细技术参考：
- [🔗 {self.category_mapping[category]}增强版页面](../enhanced-products/#-{category.replace('-', '')})
- [📚 所有产品增强版技术参考](../enhanced-products/)

"""
            
            # 在"## 产品列表"前插入增强版链接
            if "## 产品列表" in content:
                content = content.replace("## 产品列表", enhanced_section + "## 产品列表")
            else:
                # 如果没有"产品列表"标题，在第一个产品链接前插入
                lines = content.split('\n')
                insert_index = -1
                for i, line in enumerate(lines):
                    if line.strip().startswith('- ['):
                        insert_index = i
                        break
                
                if insert_index > 0:
                    lines.insert(insert_index, enhanced_section)
                    content = '\n'.join(lines)
            
            # 写回文件
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ {category} 分类页面已增强")
    
    def enhance_product_pages(self):
        """为产品页面添加增强版页面链接"""
        print("正在增强产品页面...")
        
        for category, category_dir in self.category_dirs.items():
            if not category_dir.exists():
                continue
                
            # 遍历该分类下的所有产品页面
            for md_file in category_dir.glob("*.md"):
                if md_file.name == "index.md":
                    continue
                    
                product_code = md_file.stem
                print(f"处理产品页面: {product_code}")
                
                # 读取现有内容
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查是否已经有增强版链接
                if "📖 查看增强版技术参考" in content:
                    print(f"  {product_code} 已有增强版链接，跳过")
                    continue
                
                # 检查对应的增强版页面是否存在
                enhanced_file = self.enhanced_dir / f"{product_code}.md"
                if not enhanced_file.exists():
                    print(f"  {product_code} 没有对应的增强版页面，跳过")
                    continue
                
                # 在产品概述后添加增强版链接
                enhanced_link = f"""
## 📖 查看增强版技术参考

**[🔗 {product_code} 增强版技术参考](../enhanced-products/{product_code}.md)**

包含完整PDF内容、高质量技术图片和详细规格的增强版页面。

---
"""
                
                # 在第一个"##"标题后插入增强版链接
                lines = content.split('\n')
                insert_index = -1
                
                # 寻找第一个二级标题的位置
                for i, line in enumerate(lines):
                    if line.strip().startswith('## ') and '产品概述' in line:
                        # 找到产品概述后的位置
                        for j in range(i+1, len(lines)):
                            if lines[j].strip().startswith('## ') or lines[j].strip().startswith('---'):
                                insert_index = j
                                break
                        break
                
                # 如果没找到合适位置，在第一个"---"前插入
                if insert_index == -1:
                    for i, line in enumerate(lines):
                        if line.strip() == '---' and i > 5:  # 跳过开头的front matter
                            insert_index = i
                            break
                
                if insert_index > 0:
                    lines.insert(insert_index, enhanced_link)
                    content = '\n'.join(lines)
                    
                    # 写回文件
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"  ✅ {product_code} 产品页面已增强")
                else:
                    print(f"  ⚠️ {product_code} 未找到合适的插入位置")
    
    def enhance_enhanced_product_pages(self):
        """为增强版产品页面添加返回链接"""
        print("正在增强增强版产品页面...")
        
        if not self.enhanced_dir.exists():
            print("增强版产品目录不存在")
            return
        
        # 遍历所有增强版产品页面
        for md_file in self.enhanced_dir.glob("*.md"):
            if md_file.name == "index.md":
                continue
                
            product_code = md_file.stem
            print(f"处理增强版页面: {product_code}")
            
            # 读取现有内容
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否已经有导航链接
            if "🔙 返回产品摘要页面" in content:
                print(f"  {product_code} 已有导航链接，跳过")
                continue
            
            # 确定产品分类
            category = self.get_product_category(product_code)
            category_name = self.category_mapping[category]
            
            # 在页面开头添加导航链接
            navigation_section = f"""
## 🧭 页面导航

- 🔙 [返回产品摘要页面](../{category}/{product_code}.md)
- 📂 [返回{category_name}分类](../{category}/)
- 🏠 [返回主页](../index.md)
- 📚 [所有增强版技术参考](./index.md)

---
"""
            
            # 在第一个"##"标题前插入导航
            lines = content.split('\n')
            insert_index = -1
            
            # 寻找第一个二级标题的位置
            for i, line in enumerate(lines):
                if line.strip().startswith('## ') and i > 0:
                    insert_index = i
                    break
            
            if insert_index > 0:
                lines.insert(insert_index, navigation_section)
                content = '\n'.join(lines)
                
                # 写回文件
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  ✅ {product_code} 增强版页面已增强")
            else:
                print(f"  ⚠️ {product_code} 未找到合适的插入位置")
    
    def enhance_main_index_page(self):
        """为主页添加增强版技术参考的突出链接"""
        print("正在增强主页...")
        
        index_file = self.docs_dir / "index.md"
        if not index_file.exists():
            print("主页文件不存在")
            return
        
        # 读取现有内容
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有增强版链接
        if "📖 完整技术参考" in content:
            print("主页已有增强版链接，跳过")
            return
        
        # 在features部分添加增强版技术参考
        enhanced_feature = '''
  - icon: 📖
    title: 完整技术参考
    details: 包含所有产品完整PDF内容和高质量技术图片的详细参考文档，提供最全面的技术信息
    link: /enhanced-products/'''
        
        # 在最后一个feature后添加
        if "link: /technical/" in content:
            content = content.replace(
                "    link: /technical/",
                "    link: /technical/" + enhanced_feature
            )
            
            # 写回文件
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ 主页已增强")
        else:
            print("⚠️ 主页未找到合适的插入位置")
    
    def enhance_enhanced_index_page(self):
        """增强增强版产品索引页面"""
        print("正在增强增强版产品索引页面...")
        
        index_file = self.enhanced_dir / "index.md"
        if not index_file.exists():
            print("增强版产品索引页面不存在")
            return
        
        # 读取现有内容
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有快速导航
        if "🚀 快速导航" in content:
            print("增强版索引页面已有快速导航，跳过")
            return
        
        # 在概述后添加快速导航
        quick_nav = f"""
## 🚀 快速导航

### 📂 按分类浏览
- [🎯 3D霍尔传感器](../3d-hall/) | [📖 增强版](#-3d霍尔传感器)
- [🔄 磁编码器](../magnetic-encoder/) | [📖 增强版](#-磁编码器) 
- [⚡ 霍尔开关](../hall-switch/) | [📖 增强版](#-霍尔开关)
- [🚀 其他传感器](../other-sensors/) | [📖 增强版](#-其他传感器)

### 🔗 相关页面
- [🏠 返回主页](../index.md)
- [📋 产品对比](../product-comparison.md)
- [🔧 技术支持](../technical/)
- [📚 技术资料](../resources/)

"""
        
        # 在"## 产品列表"前插入快速导航
        if "## 产品列表" in content:
            content = content.replace("## 产品列表", quick_nav + "## 产品列表")
            
            # 写回文件
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ 增强版产品索引页面已增强")
        else:
            print("⚠️ 增强版产品索引页面未找到合适的插入位置")
    
    def run(self):
        """运行所有增强操作"""
        print("开始增强页面连接...")
        print("=" * 50)
        
        # 1. 增强分类索引页面
        self.enhance_category_index_pages()
        print()
        
        # 2. 增强产品页面
        self.enhance_product_pages()
        print()
        
        # 3. 增强增强版产品页面
        self.enhance_enhanced_product_pages()
        print()
        
        # 4. 增强主页
        self.enhance_main_index_page()
        print()
        
        # 5. 增强增强版产品索引页面
        self.enhance_enhanced_index_page()
        print()
        
        print("=" * 50)
        print("✅ 页面连接增强完成！")
        print()
        print("增强内容包括:")
        print("- 分类页面添加了指向增强版页面的链接")
        print("- 产品页面添加了指向对应增强版页面的链接")
        print("- 增强版页面添加了返回导航链接")
        print("- 主页添加了完整技术参考入口")
        print("- 增强版索引页面添加了快速导航")

if __name__ == "__main__":
    enhancer = PageConnectionEnhancer()
    enhancer.run()