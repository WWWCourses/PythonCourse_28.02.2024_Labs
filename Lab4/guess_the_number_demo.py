from random import randint
from traceback import print_tb


computer_number = randint(1,10)
print(f'computer_number={computer_number}')



# If the user guess is equal to the machine number => print out a congratulation message!
# If the user guess is less than the machine number => print out "your guess is less than my number. Try again!"
# If the user guess is greater than the machine number => print out "your guess is greater than my number. Try again!"

user_number = int( input('Enter a number: ') )
print( f'user_number = {user_number}')

if user_number == computer_number:
    print('Bravo')
elif user_number < computer_number:
    print('your guess is less than my number. Try again!')
else:
    print('your guess is greater than my number. Try again!')

