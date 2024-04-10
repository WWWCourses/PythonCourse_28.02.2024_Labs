data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_data = []
# for t in data:
#     sorted_data.append((t[1], t[0]))
#
# sorted_data.sort()
#
# data = []
# for t in sorted_data:
#     data.append((t[1], t[0]))
# print(data)
print(sorted(data, key=lambda x: x[1]))
