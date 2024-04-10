# Задача 1. Напишете програма, която чете цели числа въведени от потребителя и ги
# съхранява в списък. Програма трябва да продължи да чете стойности, докато
# потребителят не въведе 0. След това тя трябва да покаже всички стойности, въведени от
# потребителя (с изключение на 0), подредени от най-малката до най-голямата стойност,
# като на всеки ред се появява по една стойност. Използвайте или метода за сортиране,
# или функцията за сортиране на списъци.

numbers = []
while True:
    number = int(input())
    if number == 0:
        break
    numbers.append(number)

numbers.sort()

for item in numbers:
    print(item)

print(numbers)
