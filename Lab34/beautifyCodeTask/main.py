import re

def get_input_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def write_to_file(input_text, filename):
    with open(filename, 'w') as f:
        f.write(input_text)


def beautify_text(input_text):
    comment_lines_re = re.compile(r'^\s*#.*$', re.MULTILINE)
    whitespaces_re = re.compile(r'\s+')

    replaced = comment_lines_re.sub('', input_text)
    replaced = whitespaces_re.sub('\n',replaced)

    return replaced


if __name__=="__main__":
    input_text = get_input_text('./example.txt')
    beautyfied = beautify_text(input_text)
    write_to_file(beautyfied, filename="beautified.txt" )


