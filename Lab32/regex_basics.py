import re


# --------------------------------- Example 1 -------------------------------- #
# rg = re.compile(r'a\d*a')
# test_strings = [
#     'aa',           # ok
#     'a12a',         # ok
#     'a1a',          # ok
#     '2a1a'          # ok
# ]

# for test_string in test_strings:
#     m = rg.search(test_string)
#     if m:
#         print(f'{test_string} match!')
#     else:
#         print(f'{test_string} did not match!')


# ---------------------------------- Anchors --------------------------------- #

# Example 1
# rx = re.compile(r'^abc$')
# test_strings = [
#     'abc',     # ok
#     'abc123',  # not
#     '123abc'   # ok
# ]

# Example 2
# rx = re.compile(r'^l.+2$')
# test_strings = [
#     '''line1
# line2''',

# ]

# for test_string in test_strings:
#     m = rx.search(test_string)
#     if m:
#         print(f'{test_string} match!')
#     else:
#         print(f'{test_string} did not match!')


# ------------------------------- Word Boundary ------------------------------ #
# \b =>  between \w and \W characters
# \d = [0-9]
# \D = [^0-9] (any non-digit symbol)
# \w  = [a-zA-Z0-9_]
# \W  = [^a-zA-Z0-9_]

# Example 1
# rx = re.compile(r'\b')
# test_strings = [
#     '',     # not
#     'a',    # ok (2)
#     'aa',   # ok (2)
#     'a!a',  # ok (4)
# ]


# test_strings = [
#     '',    # 0
#     'a',   # 2
#     '@',   # 0
#     '@a',  # 2
#     'aa',  # 2
#     'a!',  # 2
#     'a,a', # 4
#     'a_a', # 2
# ]
# rx = re.compile(r'\b');


rx = re.compile(r'\bcat\b',re.I)
test_strings = [
    'caterpilar',
    'cats',
    'cat',
    'Look at the Cat! He loves cats. She has a cat.'
]
for string in test_strings:
    res = rx.findall(string)
    print(res)



