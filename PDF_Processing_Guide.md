# PDF 内容提取与 Markdown 更新指南

本指南旨在说明如何使用 Python 脚本从 PDF 文件中提取文本内容，并根据提取的内容自动更新相关的 Markdown 文件。

## 准备工作

在开始之前，请确保您已经安装了必要的 Python 库。本项目主要依赖 `PyMuPDF`（即 `fitz`）。

您可以通过 pip 安装它：

```bash
pip install PyMuPDF
```

## 步骤一：从 PDF 提取文本

我们可以使用一个简单的 Python 脚本来读取 PDF 文件并提取其所有文本内容。

### 核心代码

这是一个 Python 脚本示例，可以提取指定 PDF 文件的文本并将其打印到控制台。

```python
import fitz  # PyMuPDF
import sys

def extract_text_from_pdf(pdf_path):
    """_summary_
    从给定的 PDF 文件中提取所有文本。

    Args:
        pdf_path (str): PDF 文件的路径。

    Returns:
        str: 提取的文本内容。
    """_e
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error opening or reading PDF file: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]
        extracted_text = extract_text_from_pdf(pdf_file)
        if extracted_text:
            print(extracted_text)
    else:
        print("Usage: python extract_pdf_text.py <path_to_pdf>")
```

### 使用方法

1.  将以上代码保存为 `extract_pdf_text.py`。
2.  在命令行中运行以下命令：

    ```bash
    python extract_pdf_text.py "path/to/your/document.pdf"
    ```

    例如，要提取 `KTM5800_EN.pdf` 的内容，您可以运行：

    ```bash
    python extract_pdf_text.py "docs/resources/产品规格书（英文版）/KTM5800_EN.pdf"
    ```

## 步骤二：更新 Markdown 文件

在获取了 PDF 的文本内容后，您可以手动或通过脚本来更新对应的 Markdown 文件。

### 手动更新

1.  复制从 PDF 中提取的关键信息。
2.  打开对应的 Markdown 文件（例如 `docs/magnetic-encoder/KTM5800.md`）。
3.  将新信息粘贴到文件中，并根据 Markdown 语法进行格式化。

### 自动化更新（示例）

您可以编写一个更复杂的脚本来自动化此过程。以下是一个概念性示例，说明如何读取 PDF 内容并更新 Markdown 文件中的特定部分。

```python
import re

# 假设这是从 PDF 提取的文本
pdf_text = "... some text from PDF ... Resolution: 30-bit ... more text ..."

# 读取 Markdown 文件内容
md_file_path = 'docs/magnetic-encoder/KTM5800.md'
with open(md_file_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# 使用正则表达式查找并替换分辨率信息
# 这是一个简化的例子，实际应用中可能需要更复杂的逻辑
new_resolution = "30-bit"
updated_md_content = re.sub(r"(分辨率：).+?(\n)", f"\\g<1>{new_resolution}\\2", md_content)

# 将更新后的内容写回 Markdown 文件
with open(md_file_path, 'w', encoding='utf-8') as f:
    f.write(updated_md_content)

print(f"Successfully updated {md_file_path}")
```

## 整合流程

为了实现完全自动化，您可以将上述两个步骤整合到一个脚本中。该脚本将：

1.  接收 PDF 文件路径和对应的 Markdown 文件路径作为输入。
2.  调用 `extract_text_from_pdf` 函数提取文本。
3.  解析提取的文本以获取关键数据（例如，使用正则表达式）。
4.  读取 Markdown 文件。
5.  将新数据更新到 Markdown 内容中。
6.  将更新后的内容写回 Markdown 文件。

这个自动化流程可以大大提高文档更新的效率和准确性。