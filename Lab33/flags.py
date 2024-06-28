import re

# Example 1
# rx = re.compile(r'^line\s*\d', re.MULTILINE|re.IGNORECASE)
# test_strings = [
#     '''Line 1
# # Line 2
# Line 3''',
# ]
# for string in test_strings:
#     res = rx.findall(string)
#     print(res)




# Example 2
rx = re.compile(r'''^
                (?=.*\d) # match a digit anywhware in string
                (?=.*[A-Z]) # match a A-Z anywhware in string
                (?=.*[a-z]) # match a a-z anywhware in string
                (?=.*[^\w\d\s:])
                ([^\s]){8,16}
                $
                ''', re.X)

test_strings = [
    '_}24I:9t58Tu?m@e',
    '|YlzEc|1',
    '#m_4xF%t"Bu5jeb$',
    'Password1!',
    '12345678aA',
    '^@},^@},^@},',
    '12345678aA@ '
]
for string in test_strings:
    m = rx.search(string)
    if m:
        print(f'{string} => Valid Password')
    else:
        print(f'{string} => NOT Valid Password')
