#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
添加相关产品推荐脚本
为每个产品页面添加相关产品推荐，增强页面之间的连接
"""

import os
import re
from pathlib import Path
import random

class RelatedProductsAdder:
    def __init__(self, docs_dir="docs"):
        self.docs_dir = Path(docs_dir)
        self.enhanced_dir = self.docs_dir / "enhanced-products"
        
        # 产品分类目录
        self.category_dirs = {
            "3d-hall": self.docs_dir / "3d-hall",
            "magnetic-encoder": self.docs_dir / "magnetic-encoder",
            "hall-switch": self.docs_dir / "hall-switch", 
            "other-sensors": self.docs_dir / "other-sensors"
        }
        
        # 产品分类映射
        self.category_mapping = {
            "3d-hall": "3D霍尔传感器",
            "magnetic-encoder": "磁编码器", 
            "hall-switch": "霍尔开关",
            "other-sensors": "其他传感器"
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
    
    def get_all_products_by_category(self):
        """获取所有产品按分类分组"""
        products_by_category = {}
        
        for category, category_dir in self.category_dirs.items():
            if not category_dir.exists():
                continue
                
            products = []
            for md_file in category_dir.glob("*.md"):
                if md_file.name != "index.md":
                    products.append(md_file.stem)
            
            products_by_category[category] = products
        
        return products_by_category
    
    def get_related_products(self, current_product, current_category, products_by_category, max_related=6):
        """获取相关产品推荐"""
        related_products = []
        
        # 1. 同分类的其他产品（最多3个）
        same_category_products = [p for p in products_by_category.get(current_category, []) if p != current_product]
        if same_category_products:
            # 随机选择最多3个同分类产品
            selected_same = random.sample(same_category_products, min(3, len(same_category_products)))
            for product in selected_same:
                related_products.append((product, current_category, "同系列产品"))
        
        # 2. 其他分类的热门产品（最多3个）
        other_categories = [cat for cat in products_by_category.keys() if cat != current_category]
        for category in other_categories:
            category_products = products_by_category.get(category, [])
            if category_products:
                # 选择该分类的第一个产品作为代表
                selected_product = category_products[0]
                related_products.append((selected_product, category, f"推荐{self.category_mapping[category]}"))
        
        # 限制总数
        return related_products[:max_related]
    
    def add_related_products_to_page(self, md_file, current_product, current_category, products_by_category):
        """为产品页面添加相关产品推荐"""
        # 读取现有内容
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有相关产品推荐
        if "## 🔗 相关产品推荐" in content:
            print(f"  {current_product} 已有相关产品推荐，跳过")
            return False
        
        # 获取相关产品
        related_products = self.get_related_products(current_product, current_category, products_by_category)
        
        if not related_products:
            print(f"  {current_product} 没有找到相关产品")
            return False
        
        # 构建相关产品推荐部分
        related_section = "\n## 🔗 相关产品推荐\n\n"
        
        # 按分类分组显示
        categories_shown = set()
        for product, category, description in related_products:
            if category not in categories_shown:
                related_section += f"### {self.category_mapping[category]}\n\n"
                categories_shown.add(category)
            
            # 检查对应的增强版页面是否存在
            enhanced_file = self.enhanced_dir / f"{product}.md"
            enhanced_link = ""
            if enhanced_file.exists():
                enhanced_link = f" | [📖 增强版](../enhanced-products/{product}.md)"
            
            related_section += f"- [{product}](../{category}/{product}.md){enhanced_link} - {description}\n"
        
        related_section += "\n---\n"
        
        # 在"## 技术支持"前插入相关产品推荐
        if "## 技术支持" in content:
            content = content.replace("## 技术支持", related_section + "## 技术支持")
        else:
            # 如果没有技术支持部分，在文件末尾前插入
            lines = content.split('\n')
            # 找到最后一个"---"的位置
            insert_index = -1
            for i in range(len(lines)-1, -1, -1):
                if lines[i].strip() == '---':
                    insert_index = i
                    break
            
            if insert_index > 0:
                lines.insert(insert_index, related_section)
                content = '\n'.join(lines)
            else:
                content += "\n" + related_section
        
        # 写回文件
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    def add_related_products_to_enhanced_pages(self, current_product, current_category, products_by_category):
        """为增强版产品页面添加相关产品推荐"""
        enhanced_file = self.enhanced_dir / f"{current_product}.md"
        if not enhanced_file.exists():
            return False
        
        # 读取现有内容
        with open(enhanced_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有相关产品推荐
        if "## 🔗 相关产品推荐" in content:
            print(f"  {current_product} 增强版已有相关产品推荐，跳过")
            return False
        
        # 获取相关产品
        related_products = self.get_related_products(current_product, current_category, products_by_category)
        
        if not related_products:
            return False
        
        # 构建相关产品推荐部分
        related_section = "\n## 🔗 相关产品推荐\n\n"
        
        # 按分类分组显示
        categories_shown = set()
        for product, category, description in related_products:
            if category not in categories_shown:
                related_section += f"### {self.category_mapping[category]}\n\n"
                categories_shown.add(category)
            
            # 增强版页面优先链接到其他增强版页面
            enhanced_file_check = self.enhanced_dir / f"{product}.md"
            if enhanced_file_check.exists():
                related_section += f"- [{product} 增强版](./{product}.md) - {description}\n"
            else:
                related_section += f"- [{product}](../{category}/{product}.md) - {description}\n"
        
        related_section += "\n---\n"
        
        # 在文件末尾添加
        content += "\n" + related_section
        
        # 写回文件
        with open(enhanced_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    def run(self):
        """运行相关产品推荐添加"""
        print("开始添加相关产品推荐...")
        print("=" * 50)
        
        # 获取所有产品
        products_by_category = self.get_all_products_by_category()
        
        print(f"发现产品分类: {list(products_by_category.keys())}")
        for category, products in products_by_category.items():
            print(f"  {self.category_mapping[category]}: {len(products)} 个产品")
        print()
        
        # 为每个产品页面添加相关产品推荐
        total_updated = 0
        total_enhanced_updated = 0
        
        for category, products in products_by_category.items():
            category_dir = self.category_dirs[category]
            print(f"处理 {self.category_mapping[category]} 分类...")
            
            for product in products:
                md_file = category_dir / f"{product}.md"
                if md_file.exists():
                    print(f"  处理产品页面: {product}")
                    if self.add_related_products_to_page(md_file, product, category, products_by_category):
                        total_updated += 1
                        print(f"    ✅ {product} 产品页面已添加相关产品推荐")
                    
                    # 同时处理增强版页面
                    print(f"  处理增强版页面: {product}")
                    if self.add_related_products_to_enhanced_pages(product, category, products_by_category):
                        total_enhanced_updated += 1
                        print(f"    ✅ {product} 增强版页面已添加相关产品推荐")
            print()
        
        print("=" * 50)
        print("✅ 相关产品推荐添加完成！")
        print()
        print(f"统计信息:")
        print(f"- 更新的产品页面: {total_updated} 个")
        print(f"- 更新的增强版页面: {total_enhanced_updated} 个")
        print()
        print("添加的功能:")
        print("- 同系列产品推荐")
        print("- 跨分类产品推荐")
        print("- 增强版页面链接")
        print("- 智能分类展示")

if __name__ == "__main__":
    # 设置随机种子以确保可重复的结果
    random.seed(42)
    
    adder = RelatedProductsAdder()
    adder.run()