import pdfplumber
import os
import re
from pathlib import Path

def read_pdf_text(file_path):
    """读取PDF文件内容"""
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF {file_path}: {str(e)}")
        return None

def find_datasheet_files():
    """查找所有datasheet文件"""
    base_dir = Path("docs/resources")
    datasheet_files = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith('.pdf') and ('datasheet' in file.lower() or '产品手册' in file):
                file_path = os.path.join(root, file)
                datasheet_files.append(file_path)
    
    return datasheet_files

def extract_model_number(filename):
    """从文件名提取型号"""
    # 匹配KTH/KTM开头的型号
    match = re.search(r'(KT[HM]\w+)', filename.upper())
    if match:
        return match.group(1)
    return None

def find_corresponding_md_file(model_number):
    """查找对应的markdown文件"""
    docs_dir = Path("docs")
    
    # 在各个子目录中查找
    subdirs = ['3d-hall', 'hall-switch', 'magnetic-encoder', 'other-sensors']
    
    for subdir in subdirs:
        subdir_path = docs_dir / subdir
        if subdir_path.exists():
            for md_file in subdir_path.glob('*.md'):
                if model_number.lower() in md_file.name.lower():
                    return md_file
    
    return None

def main():
    """主函数"""
    print("开始查找datasheet文件...")
    datasheet_files = find_datasheet_files()
    
    print(f"找到 {len(datasheet_files)} 个datasheet文件:")
    for file in datasheet_files:
        print(f"  - {file}")
    
    print("\n开始处理文件...")
    
    for datasheet_file in datasheet_files:
        print(f"\n处理文件: {datasheet_file}")
        
        # 提取型号
        model_number = extract_model_number(os.path.basename(datasheet_file))
        if not model_number:
            print(f"  无法从文件名提取型号: {datasheet_file}")
            continue
        
        print(f"  检测到型号: {model_number}")
        
        # 查找对应的markdown文件
        md_file = find_corresponding_md_file(model_number)
        if not md_file:
            print(f"  未找到对应的markdown文件: {model_number}")
            continue
        
        print(f"  找到对应的markdown文件: {md_file}")
        
        # 读取PDF内容
        pdf_content = read_pdf_text(datasheet_file)
        if not pdf_content:
            print(f"  无法读取PDF内容: {datasheet_file}")
            continue
        
        print(f"  成功读取PDF内容，长度: {len(pdf_content)} 字符")
        
        # 这里可以添加更新markdown文件的逻辑
        # 暂时只打印前500个字符作为预览
        print(f"  PDF内容预览: {pdf_content[:500]}...")

if __name__ == "__main__":
    main()