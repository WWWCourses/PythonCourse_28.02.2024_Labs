# --------------------------------- Задача 3. -------------------------------- #
# Да се напише програма, която да пита потребителя да въведе едно число от
# клавиатурата и да покаже съответното число от редицата на Фибoначи. Задачата да се реши с рекурсивна функция.

# 1,1,2,3,5,8, ..
# F(1) = 1
# F(2) = 1
# F(n) = F(n-1) + F(n-2), where n > 2

# Вход: Enter the number 5
# Изход: The 5 th fib term is 5.


def get_user_number():
	while True:
		try:
			return int(input('Enter a number: '))
		except:
			pass

def fib(n):
	if n>2:
		return fib(n-1)+fib(n-2)
	else:
		return 1


user_number = get_user_number()
print(f'The {user_number}th fib term is {fib(user_number)}.')
