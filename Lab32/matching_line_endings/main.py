import re

rx = re.compile(r'\d\nL')

with open('./test.txt', mode='r') as f:
    test_string = f.read()


print(test_string)
m = rx.search(test_string)
if m:
    print('Match')
else:
    print('No match')
