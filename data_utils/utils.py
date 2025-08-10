import re
import os
from typing import Tuple, Dict
from PIL import Image

def save_image_to_folder(image: Image.Image, folder_path: str, index: int, prefix: str = "img_", ext: str = "jpg", format: str = None):
    """
    Saves a PIL Image to the specified folder.
    
    Args:
        image:       The PIL Image object to save.
        folder_path: The path to the folder where the image will be saved.
        filename:    The name of the file (e.g. "my_image.jpg"). 
                     If None, defaults to "image.<ext>".
        format:      Optional format override (e.g. "JPEG", "PNG"). 
                     If None, inferred from filename extension or image.format.
    """
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Determine filename
    # fallback extension
    ext = (format or image.format or "PNG").lower()
    filename = f"{prefix}{index:05d}.{ext}"

    # Full path
    save_path = os.path.join(folder_path, filename)

    # Save
    image.save(save_path, format=format)
    print(f"Saved image to {save_path}")
    return filename

def split_question_into_query_and_options_0(text):
    """
    Given a string of the form:
      "<Question text>\nOptions: A: optA, B: optB, C: optC, …"
    returns (question, options_dict) where
      question is the text before "Options:",
      options_dict maps 'A'→"optA", 'B'→"optB", etc.
    """
    # 1. Split into question and options
    try:
        question_part, options_part = text.split('Options:', 1)
    except ValueError:
        raise ValueError("Input must contain 'Options:'")

    question = question_part.strip()

    # 2. Use regex to find all "Key: Value" pairs
    pattern = r'([A-Z]):\s*(.*?)(?=(?:,\s*[A-Z]:)|$)'
    matches = re.findall(pattern, options_part)

    # 3. Build the dict, stripping any trailing commas/spaces
    options = {
        key: val.strip().rstrip(',')
        for key, val in matches
    }

    return question, options

def split_question_into_query_and_options_1(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Extracts the question and options from a given text.

    Parameters:
    -----------
    text : str
        The input string containing a question and options.

    Returns:
    --------
    Tuple[str, Dict[str, str]]
        A tuple containing:
        - The question string.
        - A dictionary mapping option letters to option texts.
    """
    # Extract the question text after 'Question:' up to the next line break
    question_match = re.search(r'Question:\s*(.*?)\s*(?=\r?\n)', text, re.IGNORECASE)
    question = question_match.group(1).strip() if question_match else ''

    # Extract the block of text after 'Choices:' as the options block
    options_block_match = re.search(r'Choices:\s*(.*)', text, re.IGNORECASE | re.DOTALL)
    options_block = options_block_match.group(1).strip() if options_block_match else ''

    # Parse each line in the options block for option letter and text
    options: Dict[str, str] = {}
    for line in options_block.splitlines():
        line = line.strip()
        if not line:
            continue
        # Match formats like "(A) text", "A) text", "A. text", etc.
        opt_match = re.match(r'^\(?\s*([A-Za-z])\s*\)?[\.\):]?\s*(.+)$', line)
        if opt_match:
            key = opt_match.group(1)
            value = opt_match.group(2).strip()
            options[key] = value

    return question, options



def split_question_into_query_and_options_2(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Given a text with a question followed by an "Options:" section,
    returns a tuple (question, options_dict), where:
      - question is the question string (without the "Options:" part)
      - options_dict maps each option letter (e.g. "A") to its code snippet.
    """
    # 1. Split off the question
    parts = text.split("\nOptions:", 1)
    question = parts[0].strip()
    options_block = parts[1] if len(parts) > 1 else ""

    # 2. Normalize separators between options
    #    In the example, options are sometimes separated by ", B:" etc.
    #    We insert a newline before each "<Letter>:"
    options_block = re.sub(r',\s*([A-Za-z]:)', r'\n\1', options_block)

    # 3. Extract each option letter and its content
    pattern = re.compile(r'([A-Za-z]):\s*(.*?)(?=(?:\n[A-Za-z]:)|\Z)', re.DOTALL)
    options: Dict[str, str] = {
        m.group(1): m.group(2).strip()
        for m in pattern.finditer(options_block)
    }

    return question, options


def split_question_into_query_and_options_3(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Extracts the question and options from a text block of the form:
      [optional hint lines]
      Question: <question text>
      (A) <option A>
      (B) <option B>
      (C) <option C>
      (D) <option D>
    Returns:
      - question: the question string (without the "Question:" prefix)
      - options: dict mapping "A", "B", "C", "D" to their corresponding texts
    """
    question = ''
    options: Dict[str, str] = {}

    # Process line by line
    for line in text.splitlines():
        line = line.strip()
        # Extract question
        if line.lower().startswith('question:'):
            question = line[len('Question:'):].strip()
            continue
        # Extract options of the form "(X) value"
        m = re.match(r'^\(([A-Za-z])\)\s*(.+)$', line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()
            options[key] = value

    return question, options


def remap_options_to_indices(options):
    """
    Given options like {'A': ..., 'B': ..., …},
    returns {0: optionA, 1: optionB, …}.
    """
    return {ord(letter) - ord('A'): text
            for letter, text in options.items()}



