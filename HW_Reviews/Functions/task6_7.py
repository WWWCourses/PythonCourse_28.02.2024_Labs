# --------------------------------- Задача 6. -------------------------------- #
# Да се напише програма, която да сортира списък от tuples използвайки Lambda.

# input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# sorted_list = sorted(input_list, key=lambda t:t[1])

# # def sort_key(t):
# # 	# print(t)
# # 	return t[1]
# # sorted_list = sorted(input_list, key=sort_key)

# print(f'Sorted: {sorted_list}')


# --------------------------------- Задача 7. -------------------------------- #
# Да се напише програма, която да сортира списък от речници използвайки Lambda.
from pprint import pprint

input_list = [
	{
		'product':'Bread',
		'price':2
	},
	{
		'product':'Wine',
		'price':3
	},
	{
		'product':'Beer',
		'price':1
	}
]

sorted_list = sorted(input_list, key=lambda d: d['price'])

pprint(sorted_list)
