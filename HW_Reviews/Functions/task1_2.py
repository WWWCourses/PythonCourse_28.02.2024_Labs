# --------------------------------- Задача 1. -------------------------------- #
# Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.

# Вход: [1, 2, 5, 9, 10], 5
# Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2
# Изход: Not found

def find_in_list(l, element):
	for idx in range(len(l)):
		if l[idx]==element:
			print(f'Position {idx}')
			return None

	print('Not found')

def find_in_list2(l:list[int], element:int):
	try:
		idx = l.index(element)
		print(f'Position {idx}')
	except ValueError:
		print('Not found')


find_in_list([1, 2, 5, 9, 10], 5)
find_in_list2([1, 2, 5, 9, 10], 5)
find_in_list2([1, 2, 5, 9, 10], 3)


# --------------------------------- Задача 2. -------------------------------- #
# Да се промени горната задача така, че тя да връща стойност и след това да се
# принтира резултатът в зависимост от върната стойност от функцията. Да се напише и още една функция, която да принтира резултатът от търсенето.
# Вход: [1, 2, 5, 9, 10], 5
# Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2
# Изход: Not found


# def find_in_list(l, element):
# 	for idx in range(len(l)):
# 		if l[idx]==element:
# 			return idx

# 	return -1

# def print_result(res):
# 	if res>=0:
# 		print(f'Position {res}')
# 	else:
# 		print('Not found')

# print_result( find_in_list([1, 2, 5, 9, 10], 5) )
# print_result( find_in_list([1, 2, 5, 9, 10], 3) )