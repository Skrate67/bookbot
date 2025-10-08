def sort_on(items):
     return items["num"]

def get_text(file_path):
    with open(file_path) as f: #get book text
        file_contents = f.read() #create file contents
    return file_contents

def get_num_words(file):
    get_book_words = file.split() #split into list
    num_words = len(get_book_words) #count list entries
    return num_words

def get_num_chars(file):
        chars = {}
        for char in file:
            if char.isalpha():
                chars[char.lower()] = chars.get(char.lower(), 0) + 1 #.get(char, 0) + 1 increments chars entry (default 0) for each char
        sorted_chars = [{"char": c, "num": n} for c, n in chars.items()]
        sorted_chars.sort(reverse=True, key=sort_on)
        return sorted_chars