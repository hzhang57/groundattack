import re

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

# Example usage:
sample_text = """New negatives: Here are 128 confusing yet incorrect answer options based on the provided image description, question, and correct answer:
1. Listening to vinyl records
2. Watching band posters
3. Arranging the records
4. Admiring the curtains
5. Wearing the Santa hat
6. Cleaning the guitar
7. Adjusting the decorations
8. Reorganizing the bed
9. Changing the record
10. Adjusting the volume on the record player
11. Folding the curtains
12. Taking a nap on the bed
13. Chatting with friends
14. Playing with the Santa hat
15. Stacking the records
16. Sorting through band posters
17. Dusting the record player
18. Picking up the guitar pick
19. Listening to music through headphones
20. Dancing near the bed
21. Rearranging the furniture
22. Placing a record on the turntable
23. Adjusting the brightness of the room
24. Taking photos of the room
25. Browsing through social media
26. Singing along to a record
27. Sharing the music with someone
28. Critiquing posters on the wall
29. Sketching the room layout
30. Looking out the window through the curtains"""

# Test the function
parsed_dict = parse_numbered_list(sample_text)

# Print first few items to verify
for i in range(1, 6):
    if i in parsed_dict:
        print(f"{i}: {parsed_dict[i]}")

print(parsed_dict)
print(f"\nTotal items parsed: {len(parsed_dict)}")
