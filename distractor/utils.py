import re

def remove_unicode_escapes(text):
    # Pattern to match \u followed by exactly 4 hexadecimal digits
    pattern = r'\\u[0-9a-fA-F]{4}'
    
    # Remove all matches
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text

def remove_label(text):

    """ 

    去除字符串开头的标号，例如 "(数字)" 后可能跟有空格，并返回剩余部分。

    """

    # 使用正则表达式匹配开头的标号格式

    # ^ 匹配字符串开头，\(\d+\) 匹配形如 (4) 的标号，\s* 匹配可能存在的空格

    return re.sub(r'^\(\d+\)\s*', '', text)


def parse_numbered_strings_line_by_line(text):
    """
    Alternative approach: parse line by line for simpler cases.

    Args:
        text (str): Input text containing numbered strings

    Returns:
        dict: Dictionary with numbers as keys and text as values
    """
    result = {}

    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Match pattern: (number) followed by text
        match = re.match(r'\((\d+)\)\s*(.+)', line)
        if match:
            number = int(match.group(1))
            text_content = match.group(2).strip()
            result[number] = remove_unicode_escapes(text_content)

    return result


def parse_numbered_list(text):
    """
    Parse a string containing numbered list items and return a dictionary.
    
    Args:
        text (str): Input string containing numbered list items
        
    Returns:
        dict: Dictionary with numbers as keys and strings as values
    """
    result = {}
    
    # Split the text into lines
    lines = text.strip().split('\n')
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Use regex to match the pattern: number followed by dot and space, then the text
        match = re.match(r'^(\d+)\.\s*(.+)$', line.strip())
        
        if match:
            number = int(match.group(1))
            text_content = match.group(2).strip()
            result[number] = text_content
    
    return result
