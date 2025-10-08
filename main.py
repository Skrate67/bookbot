import sys
from stats import get_text, get_num_words, get_num_chars

def main():
    try:
        relative_path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    write_report(relative_path)
    return

def write_report(path):
    text = get_text(path)
    num_words = get_num_words(text)
    sorted_chars = get_num_chars(text)
    char_count = ""
    for char in sorted_chars:
        char_count += f"{char["char"]}: {char["num"]} \n"

    report = f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{char_count}============= END ==============="""

    return print(report)

main()