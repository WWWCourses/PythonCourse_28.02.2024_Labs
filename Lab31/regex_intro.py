import re

test_strings = [
    'ala bala',

]

pattern = re.compile(r'a.*a')
for test_str in test_strings:
    result = pattern.findall(test_str)
    print(f'{test_str}: {result}')


