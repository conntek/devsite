#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版产品页面生成器
专门为重要产品生成高质量的技术参考页面
"""

import os
import re
from pathlib import Path
import pymupdf4llm
import fitz
from pdf_to_md_final import convert_pdf_to_markdown_with_images

class EnhancedProductGenerator:
    def __init__(self, resources_dir, docs_dir):
        self.resources_dir = Path(resources_dir)
        self.docs_dir = Path(docs_dir)
        
        # 重点产品列表 - 需要生成详细页面的产品
        self.priority_products = {
            'KTP112': {
                'name': 'KTP112 - 高精度数字温度传感器',
                'category': 'other-sensors',
                'type': '温度传感器',
                'description': '高精度I²C数字温度传感器，具有可编程温度阈值和警报功能'
            },
            'KTH7801': {
                'name': 'KTH7801 - 汽车级高速磁编码器',
                'category': 'magnetic-encoder',
                'type': '磁编码器',
                'description': '汽车级高速高分辨率磁编码角度传感器'
            },
            'KTH7816': {
                'name': 'KTH7816 - 工业级高分辨率磁编码器',
                'category': 'magnetic-encoder', 
                'type': '磁编码器',
                'description': '工业级高速高分辨率磁编码角度传感器'
            },
            'KTM5800': {
                'name': 'KTM5800 - 30位超高精度磁编码器',
                'category': 'magnetic-encoder',
                'type': '磁编码器',
                'description': '30位超高分辨率XMR磁阻角度细分器'
            },
            'KTM5900': {
                'name': 'KTM5900 - TMR高精度磁编码器',
                'category': 'magnetic-encoder',
                'type': '磁编码器',
                'description': 'TMR技术高速高分辨率磁编码器'
            },
            'KTH4603': {
                'name': 'KTH4603 - 3D霍尔开关',
                'category': 'hall-switch',
                'type': '3D霍尔开关',
                'description': '三维霍尔效应开关传感器'
            },
            'KTH462NXX': {
                'name': 'KTH462NXX - 2D霍尔开关',
                'category': 'hall-switch',
                'type': '2D霍尔开关', 
                'description': '二维霍尔效应开关传感器'
            },
            'KTH31XX': {
                'name': 'KTH31XX - 线性霍尔传感器',
                'category': '3d-hall',
                'type': '线性霍尔传感器',
                'description': '高精度线性霍尔效应传感器系列'
            }
        }
    
    def find_product_pdfs(self, product_model):
        """查找特定产品的所有PDF文件"""
        pdf_files = []
        
        for root, dirs, files in os.walk(self.resources_dir):
            for file in files:
                if file.lower().endswith('.pdf'):
                    # 检查文件名是否包含产品型号
                    if product_model.lower() in file.lower():
                        pdf_path = Path(root) / file
                        pdf_files.append({
                            'path': pdf_path,
                            'filename': file,
                            'relative_path': pdf_path.relative_to(self.resources_dir),
                            'is_english': 'en' in file.lower() or 'datasheet' in file.lower(),
                            'is_chinese': 'cn' in file.lower() or '产品手册' in file
                        })
        
        return pdf_files
    
    def extract_comprehensive_info(self, pdf_files):
        """从多个PDF文件中提取综合信息"""
        all_content = ""
        key_info = {
            'features': [],
            'applications': [],
            'specifications': {},
            'voltage_range': '',
            'temperature_range': '',
            'package_types': [],
            'interfaces': [],
            'accuracy': '',
            'resolution': ''
        }
        
        for pdf_info in pdf_files:
            try:
                print(f"  📖 提取内容: {pdf_info['filename']}")
                content = pymupdf4llm.to_markdown(str(pdf_info['path']))
                all_content += f"\n\n## 来源: {pdf_info['filename']}\n\n{content}"
                
                # 提取关键信息
                self.extract_features(content, key_info)
                self.extract_applications(content, key_info)
                self.extract_specifications(content, key_info)
                self.extract_technical_params(content, key_info)
                
            except Exception as e:
                print(f"  ❌ 提取失败 {pdf_info['filename']}: {e}")
                continue
        
        return key_info, all_content
    
    def extract_features(self, content, key_info):
        """提取产品特性"""
        feature_patterns = [
            r'High\s+(?:Accuracy|Precision|Resolution|Speed|Performance)',
            r'Low\s+(?:Power|Noise|Drift|Consumption)',
            r'Wide\s+(?:Range|Bandwidth|Temperature)',
            r'Fast\s+(?:Response|Switching|Update)',
            r'Temperature\s+Compensated',
            r'Digital\s+(?:Output|Interface)',
            r'Programmable\s+(?:Threshold|Alert)',
            r'I2C\s+Interface',
            r'SPI\s+Interface',
            r'PWM\s+Output',
            r'Absolute\s+Position',
            r'Multi-turn',
            r'Single-turn',
            r'Contactless',
            r'Magnetic\s+(?:Sensing|Detection)',
            r'Hall\s+Effect',
            r'TMR\s+Technology',
            r'XMR\s+Technology'
        ]
        
        for pattern in feature_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if match not in key_info['features']:
                    key_info['features'].append(match)
    
    def extract_applications(self, content, key_info):
        """提取应用场景"""
        app_patterns = [
            r'Position\s+(?:Sensing|Detection|Measurement)',
            r'Angle\s+(?:Sensing|Detection|Measurement)',
            r'Temperature\s+(?:Sensing|Monitoring|Measurement)',
            r'Current\s+(?:Sensing|Measurement)',
            r'Speed\s+(?:Sensing|Detection)',
            r'Proximity\s+(?:Sensing|Detection)',
            r'Motor\s+Control',
            r'Servo\s+(?:Control|Motor)',
            r'Automotive\s+(?:Applications|Systems)',
            r'Industrial\s+(?:Automation|Control)',
            r'Consumer\s+Electronics',
            r'Medical\s+(?:Equipment|Devices)',
            r'Robotics?',
            r'HVAC\s+Systems',
            r'Power\s+Management',
            r'Battery\s+Management'
        ]
        
        for pattern in app_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if match not in key_info['applications']:
                    key_info['applications'].append(match)
    
    def extract_specifications(self, content, key_info):
        """提取技术规格"""
        spec_patterns = {
            'Supply Voltage': r'Supply\s+Voltage.*?(\d+\.?\d*)\s*[-~]\s*(\d+\.?\d*)\s*V',
            'Supply Current': r'Supply\s+Current.*?(\d+\.?\d*)\s*(mA|µA|uA)',
            'Resolution': r'Resolution.*?(\d+)\s*(bit|°|arc)',
            'Accuracy': r'Accuracy.*?±?(\d+\.?\d*)\s*(%|°|arc)',
            'Sensitivity': r'Sensitivity.*?(\d+\.?\d*)\s*(mV/mT|V/T|LSB/°)',
            'Operating Temperature': r'Operating\s+Temperature.*?(-?\d+)\s*°?C\s*[-~]\s*\+?(\d+)\s*°?C',
            'Update Rate': r'Update\s+Rate.*?(\d+\.?\d*)\s*(Hz|kHz|SPS)',
            'Interface': r'Interface.*?(I2C|SPI|PWM|UART|CAN)',
            'Package': r'Package.*?(SOT-\d+|QFN-\d+|DFN-\d+|TO-\d+|TSSOP|MSOP)'
        }
        
        for spec_name, pattern in spec_patterns.items():
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                if len(match.groups()) >= 2:
                    key_info['specifications'][spec_name] = f"{match.group(1)}-{match.group(2)}"
                else:
                    key_info['specifications'][spec_name] = match.group(1)
    
    def extract_technical_params(self, content, key_info):
        """提取技术参数"""
        # 电压范围
        voltage_match = re.search(r'(\d+\.?\d*)\s*[-~]\s*(\d+\.?\d*)\s*V', content)
        if voltage_match and not key_info['voltage_range']:
            key_info['voltage_range'] = f"{voltage_match.group(1)}-{voltage_match.group(2)}V"
        
        # 温度范围
        temp_match = re.search(r'(-?\d+)\s*°?C\s*[-~]\s*\+?(\d+)\s*°?C', content)
        if temp_match and not key_info['temperature_range']:
            key_info['temperature_range'] = f"{temp_match.group(1)}°C~+{temp_match.group(2)}°C"
        
        # 封装类型
        package_patterns = ['SOT-23', 'QFN', 'DFN', 'TO-92', 'TSSOP', 'MSOP', 'SC-70']
        for package in package_patterns:
            if package.lower() in content.lower() and package not in key_info['package_types']:
                key_info['package_types'].append(package)
        
        # 接口类型
        interface_patterns = ['I2C', 'SPI', 'PWM', 'UART', 'CAN', 'Analog']
        for interface in interface_patterns:
            if interface.lower() in content.lower() and interface not in key_info['interfaces']:
                key_info['interfaces'].append(interface)
    
    def generate_enhanced_page(self, product_model, product_info, key_info, full_content):
        """生成增强版产品页面"""
        
        # 页面头部
        content = f"""# {product_info['name']}

[返回产品目录](../index.md)

## 产品概述

**{product_model}**是{product_info['description']}。该产品采用先进的传感技术，具有优异的性能指标和可靠性，专为各种工业和消费电子应用而设计。

"""
        
        # 核心特性
        content += "### 核心特性\n\n"
        if key_info['voltage_range']:
            content += f"- **工作电压**: {key_info['voltage_range']}\n"
        if key_info['temperature_range']:
            content += f"- **工作温度**: {key_info['temperature_range']}\n"
        if key_info['package_types']:
            content += f"- **封装类型**: {', '.join(key_info['package_types'])}\n"
        if key_info['interfaces']:
            content += f"- **接口类型**: {', '.join(key_info['interfaces'])}\n"
        
        # 添加提取的特性
        for feature in key_info['features'][:8]:  # 最多8个特性
            content += f"- **{feature}**: 先进技术特性\n"
        
        # 主要应用
        if key_info['applications']:
            content += "\n### 主要应用场景\n\n"
            for app in key_info['applications'][:8]:  # 最多8个应用
                content += f"- {app}\n"
        
        # 技术规格表
        if key_info['specifications']:
            content += "\n---\n\n## 技术规格\n\n| 参数 | 规格 | 备注 |\n|------|------|------|\n"
            for spec_name, spec_value in key_info['specifications'].items():
                content += f"| {spec_name} | {spec_value} | 典型值 |\n"
        
        # 产品特色
        content += f"\n---\n\n## 产品特色\n\n### 技术优势\n\n**{product_model}**采用业界领先的传感技术，具有以下技术优势：\n\n"
        
        if 'Temperature' in product_model or 'KTP' in product_model:
            content += """- **高精度测量**: 采用先进的数字温度传感技术，提供高精度温度测量
- **可编程功能**: 支持可编程温度阈值和警报功能
- **数字接口**: 标准I²C数字接口，易于系统集成
- **低功耗设计**: 优化的电路设计，适合电池供电应用
"""
        elif 'KTM' in product_model or 'encoder' in product_info['type'].lower():
            content += """- **超高分辨率**: 提供业界领先的角度分辨率
- **绝对位置**: 真正的绝对位置编码，无需参考点
- **高速响应**: 支持高速旋转应用
- **抗干扰**: 优异的抗磁场干扰能力
"""
        elif 'Hall' in product_info['type'] or 'KTH' in product_model:
            content += """- **高灵敏度**: 优异的磁场检测灵敏度
- **低功耗**: 超低功耗设计，适合便携设备
- **宽工作范围**: 宽电压和温度工作范围
- **高可靠性**: 无机械接触，长寿命设计
"""
        
        # 应用指南
        content += "\n### 设计建议\n\n"
        if 'Temperature' in product_model or 'KTP' in product_model:
            content += """1. **电源设计**: 使用稳定的电源，建议加入去耦电容
2. **I²C总线**: 正确配置上拉电阻，注意总线时序
3. **热设计**: 考虑自热效应，合理设计散热
4. **软件集成**: 实现温度补偿和校准算法
"""
        elif 'encoder' in product_info['type'].lower():
            content += """1. **机械安装**: 确保磁铁与传感器同轴安装
2. **磁铁选择**: 选择合适强度和尺寸的永磁体
3. **信号处理**: 实现适当的数字滤波和校准
4. **系统集成**: 考虑温度补偿和误差校正
"""
        else:
            content += """1. **电路设计**: 合理设计电源和信号调理电路
2. **PCB布局**: 注意信号完整性和EMI设计
3. **机械安装**: 确保传感器正确定位和固定
4. **软件处理**: 实现信号处理和校准算法
"""
        
        # 相关文档
        content += "\n---\n\n## 相关文档\n\n"
        
        # 查找相关PDF文件
        pdf_files = self.find_product_pdfs(product_model)
        for pdf_info in pdf_files:
            if pdf_info['is_chinese']:
                content += f"- [📄 产品手册 (中文)](../resources/{pdf_info['relative_path']})\n"
            elif pdf_info['is_english']:
                content += f"- [📋 Datasheet (English)](../resources/{pdf_info['relative_path']})\n"
            else:
                content += f"- [📖 技术文档](../resources/{pdf_info['relative_path']})\n"
        
        content += """- [🔧 应用指南](../technical/)
- [🛠️ 评估板资料](../resources/)
- [💻 开发工具](../technical/)
- [📊 可靠性报告](../technical/)
- [📞 技术支持](../resources/#技术支持)

---

## 技术支持

如需技术支持、样品申请或定制化服务，请联系我们

### 支持服务
- 技术咨询和选型指导
- 样品申请和评估
- 定制化解决方案
- 应用电路设计支持
- 批量供货服务
- 现场技术支持

### 联系方式
- 技术热线: 400-xxx-xxxx
- 邮箱: support@ktsense.com
- 在线支持: [技术论坛](../technical/)

---

*最后更新: 2024年*
*版本: v2.0*
"""
        
        return content
    
    def process_priority_product(self, product_model):
        """处理重点产品"""
        if product_model not in self.priority_products:
            print(f"❌ {product_model} 不在重点产品列表中")
            return False
        
        product_info = self.priority_products[product_model]
        print(f"\n🎯 处理重点产品: {product_model}")
        
        # 查找PDF文件
        pdf_files = self.find_product_pdfs(product_model)
        if not pdf_files:
            print(f"  ❌ 未找到 {product_model} 的PDF文件")
            return False
        
        print(f"  📁 找到 {len(pdf_files)} 个PDF文件")
        
        # 提取综合信息
        key_info, full_content = self.extract_comprehensive_info(pdf_files)
        
        # 生成增强页面
        page_content = self.generate_enhanced_page(product_model, product_info, key_info, full_content)
        
        # 保存页面
        category_folder = self.docs_dir / product_info['category']
        category_folder.mkdir(parents=True, exist_ok=True)
        
        output_file = category_folder / f"{product_model}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"  ✅ 生成增强页面: {output_file}")
        return True
    
    def process_all_priority_products(self):
        """处理所有重点产品"""
        print("🚀 开始处理重点产品...")
        
        success_count = 0
        total_count = len(self.priority_products)
        
        for product_model in self.priority_products.keys():
            if self.process_priority_product(product_model):
                success_count += 1
        
        print(f"\n🎉 重点产品处理完成!")
        print(f"✅ 成功: {success_count}/{total_count}")
        
        return success_count

def main():
    """主函数"""
    resources_dir = "docs/resources"
    docs_dir = "docs"
    
    generator = EnhancedProductGenerator(resources_dir, docs_dir)
    
    print("=== 增强版产品页面生成器 ===")
    print(f"重点产品数量: {len(generator.priority_products)}")
    
    # 处理所有重点产品
    success_count = generator.process_all_priority_products()
    
    print(f"\n📊 处理结果:")
    print(f"✅ 成功生成: {success_count} 个增强页面")
    print(f"📝 重点产品: {list(generator.priority_products.keys())}")

if __name__ == "__main__":
    main()