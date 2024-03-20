# ------------------------------- else in loops ------------------------------ #
# for num in range(1,6):
#     print(num)
#     if num==3:
#         break
# else:
#     print('OK') # will not be executed if breaked



# ------------------------------- Endless loop ------------------------------- #
# while True:
#     print('OK')

# --------------------------- while for user input --------------------------- #
# TASK:
# ask the user to enter a number (x).
# While the user enters x != number,ask him/her to enter again.

while True:
    try:
        x = int(input('x='))
        break
    except:
        print('Enter a number!!!')


print(f'bravo, x={x}')

