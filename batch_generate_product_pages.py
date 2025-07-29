#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量生成产品技术参考页面
基于PDF datasheet自动生成详细的产品介绍页面
"""

import os
import re
from pathlib import Path
import pymupdf4llm
import fitz
from pdf_to_md_final import convert_pdf_to_markdown_with_images, is_valid_image_advanced

class ProductPageGenerator:
    def __init__(self, resources_dir, docs_dir):
        self.resources_dir = Path(resources_dir)
        self.docs_dir = Path(docs_dir)
        self.product_categories = {
            '070501-BU1': {
                'name': '3D Hall传感器',
                'folder': '3d-hall',
                'description': '3D霍尔传感器系列产品'
            },
            '070502-BU2': {
                'name': '磁编码器',
                'folder': 'magnetic-encoder', 
                'description': '磁编码器系列产品'
            },
            '070503-BU3': {
                'name': 'Hall开关',
                'folder': 'hall-switch',
                'description': 'Hall开关系列产品'
            },
            '070504-BU4': {
                'name': '其他传感器',
                'folder': 'other-sensors',
                'description': '其他传感器系列产品'
            }
        }
    
    def find_all_pdf_files(self):
        """查找所有PDF文件"""
        pdf_files = []
        for root, dirs, files in os.walk(self.resources_dir):
            for file in files:
                if file.lower().endswith('.pdf'):
                    pdf_path = Path(root) / file
                    # 提取产品型号
                    product_model = self.extract_product_model(file)
                    if product_model:
                        # 确定产品类别
                        category = self.determine_category(str(pdf_path))
                        pdf_files.append({
                            'path': pdf_path,
                            'filename': file,
                            'model': product_model,
                            'category': category,
                            'relative_path': pdf_path.relative_to(self.resources_dir)
                        })
        return pdf_files
    
    def extract_product_model(self, filename):
        """从文件名提取产品型号"""
        # 常见的产品型号模式
        patterns = [
            r'(KT[HMP]\d+[A-Z]*\d*)',  # KTH1234, KTM5678, KTP112等
            r'(KTA[x]?\d+)',           # KTAx333等
        ]
        
        for pattern in patterns:
            match = re.search(pattern, filename, re.IGNORECASE)
            if match:
                return match.group(1).upper()
        return None
    
    def determine_category(self, pdf_path):
        """根据路径确定产品类别"""
        for category_code, category_info in self.product_categories.items():
            if category_code in pdf_path:
                return category_info
        return self.product_categories['070504-BU4']  # 默认分类
    
    def extract_key_info_from_pdf(self, pdf_path):
        """从PDF提取关键信息"""
        try:
            # 使用pymupdf4llm提取文本
            text_content = pymupdf4llm.to_markdown(str(pdf_path))
            
            # 提取关键信息
            info = {
                'voltage_range': self.extract_voltage_range(text_content),
                'temperature_range': self.extract_temperature_range(text_content),
                'package_type': self.extract_package_type(text_content),
                'key_features': self.extract_key_features(text_content),
                'applications': self.extract_applications(text_content),
                'specifications': self.extract_specifications(text_content)
            }
            
            return info, text_content
        except Exception as e:
            print(f"提取PDF信息失败 {pdf_path}: {e}")
            return {}, ""
    
    def extract_voltage_range(self, text):
        """提取工作电压范围"""
        patterns = [
            r'(\d+\.?\d*)\s*[-~]\s*(\d+\.?\d*)\s*V',
            r'VDD\s*=\s*(\d+\.?\d*)\s*[-~]\s*(\d+\.?\d*)\s*V',
            r'Supply\s+Voltage.*?(\d+\.?\d*)\s*[-~]\s*(\d+\.?\d*)\s*V'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return f"{match.group(1)}-{match.group(2)}V"
        return "详见规格书"
    
    def extract_temperature_range(self, text):
        """提取工作温度范围"""
        patterns = [
            r'(-?\d+)\s*°?C\s*[-~]\s*\+?(\d+)\s*°?C',
            r'Operating\s+Temperature.*?(-?\d+)\s*°?C\s*[-~]\s*\+?(\d+)\s*°?C',
            r'Temperature\s+Range.*?(-?\d+)\s*°?C\s*[-~]\s*\+?(\d+)\s*°?C'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return f"{match.group(1)}°C~+{match.group(2)}°C"
        return "详见规格书"
    
    def extract_package_type(self, text):
        """提取封装类型"""
        packages = ['SOT-23', 'TO-92', 'DFN', 'QFN', 'SOP', 'TSSOP', 'MSOP', 'SC-70']
        found_packages = []
        
        for package in packages:
            if package.lower() in text.lower():
                found_packages.append(package)
        
        return ', '.join(found_packages) if found_packages else "详见规格书"
    
    def extract_key_features(self, text):
        """提取关键特性"""
        features = []
        
        # 查找特性相关的关键词
        feature_patterns = [
            r'High\s+(?:Accuracy|Precision|Resolution)',
            r'Low\s+(?:Power|Noise|Drift)',
            r'Wide\s+(?:Range|Bandwidth)',
            r'Fast\s+(?:Response|Switching)',
            r'Temperature\s+Compensated',
            r'Rail-to-Rail',
            r'Single\s+Supply'
        ]
        
        for pattern in feature_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                features.append(pattern.replace('\\s+', ' ').replace('(?:', '').replace(')', ''))
        
        return features[:5]  # 最多返回5个特性
    
    def extract_applications(self, text):
        """提取应用场景"""
        applications = []
        
        # 查找应用相关的关键词
        app_patterns = [
            r'Position\s+(?:Sensing|Detection)',
            r'Current\s+(?:Sensing|Measurement)',
            r'Speed\s+(?:Sensing|Detection)',
            r'Angle\s+(?:Sensing|Measurement)',
            r'Proximity\s+(?:Sensing|Detection)',
            r'Motor\s+Control',
            r'Automotive',
            r'Industrial\s+Automation',
            r'Consumer\s+Electronics'
        ]
        
        for pattern in app_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                applications.append(pattern.replace('\\s+', ' ').replace('(?:', '').replace(')', ''))
        
        return applications[:6]  # 最多返回6个应用
    
    def extract_specifications(self, text):
        """提取技术规格"""
        specs = {}
        
        # 查找常见规格参数
        spec_patterns = {
            'Sensitivity': r'Sensitivity.*?(\d+\.?\d*)\s*(mV/mT|V/T)',
            'Resolution': r'Resolution.*?(\d+\.?\d*)\s*(bit|°)',
            'Accuracy': r'Accuracy.*?±?(\d+\.?\d*)\s*(%|°)',
            'Supply Current': r'Supply\s+Current.*?(\d+\.?\d*)\s*(mA|µA)',
            'Output': r'Output.*?(\d+\.?\d*)\s*(V|mA)'
        }
        
        for spec_name, pattern in spec_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                specs[spec_name] = f"{match.group(1)} {match.group(2)}"
        
        return specs
    
    def generate_product_page(self, pdf_info, extracted_info, markdown_content):
        """生成产品页面内容"""
        model = pdf_info['model']
        category = pdf_info['category']
        
        # 确定产品类型
        if 'Hall' in category['name'] or 'hall' in category['name'].lower():
            product_type = "霍尔传感器"
        elif 'encoder' in category['name'].lower() or '编码' in category['name']:
            product_type = "磁编码器"
        elif 'switch' in category['name'].lower() or '开关' in category['name']:
            product_type = "霍尔开关"
        else:
            product_type = "传感器"
        
        # 生成页面内容
        content = f"""# {model} - {product_type}

[返回产品目录](../index.md)

## 产品概述

**{model}**是一款高性能的{product_type}，采用先进的传感技术，具有优异的性能和可靠性。该产品专为各种工业和消费电子应用而设计。

### 核心特性

- **工作电压**: {extracted_info.get('voltage_range', '详见规格书')}
- **工作温度**: {extracted_info.get('temperature_range', '详见规格书')}
- **封装类型**: {extracted_info.get('package_type', '详见规格书')}
"""
        
        # 添加关键特性
        if extracted_info.get('key_features'):
            for feature in extracted_info['key_features']:
                content += f"- **{feature}**: 高性能特性\n"
        
        # 添加应用场景
        if extracted_info.get('applications'):
            content += "\n### 主要应用场景\n\n"
            for app in extracted_info['applications']:
                content += f"- {app}\n"
        
        # 添加技术规格
        if extracted_info.get('specifications'):
            content += "\n---\n\n## 技术规格\n\n| 参数 | 规格 | 单位 |\n|------|------|------|\n"
            for spec_name, spec_value in extracted_info['specifications'].items():
                parts = spec_value.split(' ', 1)
                value = parts[0] if parts else spec_value
                unit = parts[1] if len(parts) > 1 else ""
                content += f"| {spec_name} | {value} | {unit} |\n"
        
        # 添加相关文档
        content += f"""\n---\n\n## 相关文档\n\n- [📄 {model} 产品手册](../resources/{pdf_info['relative_path']})
- [📋 {category['name']}系列文档](../resources/)
- [📖 技术文档](../technical/)
- [📊 应用指南](../technical/)
- [🔧 评估板资料](../resources/)
- [🛠️ 设计工具](../technical/)
- [📞 技术支持](../resources/#技术支持)

---

## 详细技术信息

以下是从产品规格书中提取的详细技术信息：

{markdown_content[:2000]}...

> 💡 **提示**: 完整的技术规格和应用信息请参考 [产品规格书](../resources/{pdf_info['relative_path']})

---

## 技术支持

如需技术支持、样品申请或定制化服务，请联系我们

### 支持服务
- 技术咨询和选型指导
- 样品申请和评估
- 定制化解决方案
- 应用电路设计支持
- 批量供货服务

---

*最后更新: 2024年*
"""
        
        return content
    
    def process_all_pdfs(self):
        """处理所有PDF文件"""
        pdf_files = self.find_all_pdf_files()
        print(f"找到 {len(pdf_files)} 个PDF文件")
        
        processed_count = 0
        skipped_count = 0
        
        for pdf_info in pdf_files:
            try:
                print(f"\n处理: {pdf_info['model']} ({pdf_info['filename']})")
                
                # 检查是否已存在对应的产品页面
                category_folder = self.docs_dir / pdf_info['category']['folder']
                product_file = category_folder / f"{pdf_info['model']}.md"
                
                if product_file.exists():
                    print(f"  ⚠️  产品页面已存在: {product_file}")
                    skipped_count += 1
                    continue
                
                # 提取PDF信息
                extracted_info, markdown_content = self.extract_key_info_from_pdf(pdf_info['path'])
                
                # 生成产品页面
                page_content = self.generate_product_page(pdf_info, extracted_info, markdown_content)
                
                # 确保目录存在
                category_folder.mkdir(parents=True, exist_ok=True)
                
                # 保存产品页面
                with open(product_file, 'w', encoding='utf-8') as f:
                    f.write(page_content)
                
                print(f"  ✅ 生成产品页面: {product_file}")
                processed_count += 1
                
            except Exception as e:
                print(f"  ❌ 处理失败: {e}")
                skipped_count += 1
                continue
        
        print(f"\n=== 处理完成 ===")
        print(f"成功处理: {processed_count} 个产品")
        print(f"跳过/失败: {skipped_count} 个产品")
        print(f"总计: {len(pdf_files)} 个PDF文件")
        
        return processed_count, skipped_count
    
    def update_index_files(self):
        """更新各分类的index文件"""
        for category_code, category_info in self.product_categories.items():
            category_folder = self.docs_dir / category_info['folder']
            index_file = category_folder / 'index.md'
            
            if not category_folder.exists():
                continue
            
            # 查找该分类下的所有产品文件
            product_files = []
            for md_file in category_folder.glob('*.md'):
                if md_file.name != 'index.md':
                    product_model = md_file.stem
                    product_files.append(product_model)
            
            if not product_files:
                continue
            
            # 生成index内容
            index_content = f"""# {category_info['name']}

{category_info['description']}

## 产品列表

"""
            
            for product in sorted(product_files):
                index_content += f"- [{product}](./{product}.md)\n"
            
            index_content += "\n---\n\n[返回产品目录](../index.md)\n"
            
            # 保存index文件
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(index_content)
            
            print(f"更新分类索引: {index_file} ({len(product_files)} 个产品)")

def main():
    """主函数"""
    resources_dir = "docs/resources"
    docs_dir = "docs"
    
    generator = ProductPageGenerator(resources_dir, docs_dir)
    
    print("开始批量生成产品技术参考页面...")
    processed, skipped = generator.process_all_pdfs()
    
    print("\n更新分类索引文件...")
    generator.update_index_files()
    
    print(f"\n🎉 批量处理完成!")
    print(f"✅ 成功生成 {processed} 个产品页面")
    print(f"⚠️  跳过 {skipped} 个文件")

if __name__ == "__main__":
    main()