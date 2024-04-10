d = {}
user_input = [1, 2, 3, 4, 4, 4, 5, 5]
# print(len(set(user_input)))

for el in user_input:
    # if el not in d:
    #     d[el] = 1
    # else:
    # d[el] = d[el] + 1
    d.setdefault(el, 0)
    d[el] += 1

for key, value in d.items():
    print(key, value)

unique = [v for v in d.values() if v == 1]
dup = [v for v in d.values() if v > 1]
print(len(unique), len(dup))
