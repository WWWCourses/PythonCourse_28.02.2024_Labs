import re


# --------------------------------- Example 1 -------------------------------- #
# findall and capturing groups demo
# TASK: extract name and phone number for BG codes (+359)
# input_text = """
# ivan: +359 88 123456
# maria: +42 123456
# john: 76438787438
# anna:+359 9883249
# dummy:+359 9kkkkkk49
# """

# name_tel_re = re.compile(r'^(\w+):\s*(\+359[\s\d]+)$', re.MULTILINE)
# matches = name_tel_re.findall(input_text)


# print(matches)

# for name, tel in matches:
#     print(f'{name}-{tel}')



