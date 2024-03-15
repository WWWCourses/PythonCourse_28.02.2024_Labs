# ------------------------------ Why using loops ----------------------------- #
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for each value in [1,2,3,4,5]:
# for x in [1,2,3,4,5]:
#     print(x)


# for x in range(1,6):
#     print(x)

# print('END')


# --------------------------------- Examples --------------------------------- #
# # TASK: print 'hi' 5 times
# for _ in range(5):
#     print('hi')


# ------------------------------ range Function ------------------------------ #
# range(start, stop, step)
# range(stop) =>start=0, step=1

# for x in range(5, 1, -1):
#     print(x, end=",")  # 5, 4, 3, 2,

# TASK: print numbers 10, 8, 6, 4, 2
# for x in range(10, 0,-2):
#     print(x)


# ----------------------------- for on sequences ----------------------------- #
# text = 'abcd'
# for l in text:
#     print(l)

# ----------------------------- nested for loops ----------------------------- #
# text = 'abc'

# for l in text:
#     for num in range(1,4):
#         print(l+str(num), end=", ")
#     print()


# # a1, a2, a3, b1, b2, b3, c1, c2, c3,

# # a1, a2, a3,
# # b1, b2, b3
# # c1, c2, c3


# TASK: write loop which will print:
# 1a, 1b, 1c
# 2a, 2b, 2c
# 3a, 3b, 3c

# text = 'abc'
# for num in range(1,4):
#     for l in text:
#         print(str(num)+l, end=", ")
#     print()

# --------------------------------- Continue --------------------------------- #
# for num in range(5):
#     if num==3:
#         print('@@@@@@')
#         continue

### example 2:
# text = 'abc'
# for num in range(1,4):
#     if num%2==0:
#         continue

#     for l in text:
#         print(str(num)+l, end=", ")

#     print()

# 1a, 1b, 1c
# 3a, 3b, 3c


# ----------------------------------- break ---------------------------------- #
# for num in range(5):
#     if num==3:
#         print('Three')
#         break
#     print(num)

# print('END')

# example 2:
# text = 'abc'
# for num in range(1,4):
#     if num%2==0:
#         break

#     for l in text:
#         print(str(num)+l, end=", ")

#     print()

# for x in range(5):
#     #TODO: impplement later
#     pass



# -------------------------------- while loop -------------------------------- #
### Notes:
# if you need N iterations => for loop
# if you know a condition for iterations => while loop


### TASK: generate random even number
## NOT GOOD and BUGGY solution (must use while loop):
import random
for _ in range(100):
    random_number = random.randint(1,100)
    print(random_number)
    if random_number%2==0:
        print('OK')
        break

















