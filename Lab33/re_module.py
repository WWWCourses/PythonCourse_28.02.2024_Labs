import re

# ------------------------ search method and function ------------------------ #

# test_string = "123abc456"


# # using regex object method:
# rx = re.compile(r'abc')
# m = rx.search(test_string, 0, 6)

# print(m)

# # using re module function:
# m = re.search(r'abc', test_string[:6])
# print(m)


# ----------------------------------- match ---------------------------------- #

# test_string = "123abc456"

# rx = re.compile(r'\d')
# m = rx.match(test_string)
# print(m)

# # the same as
# rx = re.compile(r'^\d')
# m = rx.search(test_string)
# print(m)


# ---------------------------------- findall --------------------------------- #
# text = "123abc456abcabc"
# rx = re.compile(r'abc')

# res = rx.findall(text)
# print(res)


# ------------------------------------ sub ----------------------------------- #
# TASK: remove all digits from string
# text = "123abc456abcabc"
# rx = re.compile(r'\d')
# text_replaced = rx.sub('', text)

# print(text_replaced)


# ------------------------------- Match Object ------------------------------- #
text = "123abc456abcabc"
rx = re.compile(r'(\d+)([a-z]+)')

m = rx.search(text)
print(m.group(1))
print(m.group(2))
print(m.groups())
print(m.start())
print(m.end())