# --------------------------------- Задача 4. -------------------------------- #
# Да се напише програма, която да пита потребителя да въведе число от
# клавиатурата и да пресметне факториелът на това число. Да се използва рекурсия.

# n! = n*(n-1)!
# 0! = 1

# Вход: Enter the number 5
# Изход: Factorial of 5 is 120


def get_user_number():
	while True:
		try:
			return int(input('Enter a number: '))
		except:
			pass

def fact(n):
	if n>0:
		return n*fact(n-1)
	else:
		return 1


user_number = get_user_number()
print(f'Factoriel of {user_number} is {fact(user_number)}')
