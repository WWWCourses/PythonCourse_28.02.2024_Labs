import re


# --------------------------------- Example 1 -------------------------------- #
# text = "I love cats. He love dogs."
# pattern = re.compile(r"(?:cat|dog)s")


# result = pattern.findall(text)
# print(result)

# --------------------------------- Example 2 -------------------------------- #
# import re

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
text = """
Ivan Ivanov: 30 years old;
Petar Petrov:25 years old;
"""

# Using capturing group to get names and ages
# TODO: why capture like ....
pattern = re.compile(r"(?:\w+\s(\w+)):\s?\d+\s")
matches = pattern.findall(text)

for match in matches:
    print("Group 1:", match[0])
    print("Group 2:", match[1])
