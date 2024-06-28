import re


# --------------------------------- Example 1 -------------------------------- #
# text = "I love cats. He love dogs."
# pattern = re.compile(r"(?:cat|dog)s")


# result = pattern.findall(text)
# print(result)

# --------------------------------- Example 2 -------------------------------- #

# text = """
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """

# # Using capturing group to get names and ages
# pattern = re.compile(r"(\w+)\s(\w+):\s?(\d+)\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("First Name:", match[0])
#     print("Last Name:", match[1])
#     print("Age:", match[2])



# --------------------------------- Example 3 -------------------------------- #
# text = """
# Ivan Ivanov: 30 years old;
# Petar Petrov:25 years old;
# """

# # Using capturing group to get names and ages
# pattern = re.compile(r"(?:\w+)\s\w+:\s?(?:\d+)\s")
# matches = pattern.findall(text)

# for match in matches:
#     print("Group 1:", match[0])
#     print("Group 2:", match[1])

# --------------------------------- Example 4 -------------------------------- #
# rx = re.compile( r'(?:straw|rasp)berries' )

# test_strings = [
#     'straw berries',       # not
#     'I love strawberries', # ok
#     'I love rasp berries', # not
#     'I love raspberries',  # ok
#     'I love berries',      # not
# ]

# for string in test_strings:
#     m = rx.search(string)
#     if m:
#         print(f'{string} # ok ')
#     else:
#         print(f'{string} # not ')



# --------------------------------- Example 5 -------------------------------- #
# test_strings = [
#   "a123a",   # ok
#   "a123ab",  # not
#   "caaac",    # ok
#   "ff",      # ok
# ]

# rx = re.compile(r'^([a-z]).*\1$')


# for string in test_strings:
#     m = rx.search(string)
#     if m:
#         print(f'{string} # ok ')
#     else:
#         print(f'{string} # not ')


# --------------------------------- Example 6 -------------------------------- #

text = """
Ivan Ivanov: 30 years old;
Petar Petrov:25 years old;
"""

# Using capturing group to get names and ages
pattern = re.compile(r"(?P<first>\w+)\s(?P<second>\w+):\s?(?P<age>\d+)\s")
m = pattern.search(text)

print("First Name:", m.group('first'))
print("Last Name:", m.group('second'))
print("Age:", m.group('age'))