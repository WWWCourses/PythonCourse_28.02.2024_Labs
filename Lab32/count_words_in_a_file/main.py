import re

def get_file_content(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def count_words_by_splitting():
    text = get_file_content('./example.txt')
    words = text.split(' ')
    print(words)

def count_words_by_allowed_symbols():
    text = get_file_content('./example.txt')
    rx = re.compile(r'[a-zA-z]+')

    words = rx.findall(text)
    print(words)


if __name__=="__main__":
    count_words_by_splitting()
    count_words_by_allowed_symbols()



