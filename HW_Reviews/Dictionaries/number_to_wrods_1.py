numbers = [
	['', 'едно', 'две', 'три', 'четири', 'пет', 'шест',  'седем', 'осем', 'девет'],
	['','','двадесет',  'тридесет',  'четиридесет',  'петдесет', 'шестдесет',  'седемдесет', 'осемдесет', 'деветдесет'],
	['','сто', 'двеста', 'триста', 'четиристотин', 'петстотин', 'шестстотин', 'седемстотин', 'осемстотин', 'деветстотин'],
	['', 'хиляда', 'две хиляди', 'три хиляди', 'четири хиляди', 'пет хиляди', 'шест хиляди', 'седем хиляди', 'осем хиляди', 'девет хиляди']
]

exceptions = ['десет', 'единадесет',  'дванадесет',  'тринадесет',  'четиринадесет',  'петнадесет',  'шестнадесет',  'седемнадесет',  'осемнадесет',  'деветнадесет']


x = number = 3222
i = 0

digits = []
output = ''

while number%10:
	digit = number%10
	digits.append(digit)
	number = number//10

	if i==0:
		# цифра еденици:
		output = 'и '+numbers[i][digit]
	elif i==1 and digit==1:
		# цифра десетици = 1:
		output = 'и '+exceptions[digits[-1]]
	else:
		output = numbers[i][digit] + ' ' + output

	i+=1

print(f'{x} = {output}')
