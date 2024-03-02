# x = 5
# y = 5.0
# z = True
# a = '5'
# b = "5.0"


# RAM:
# x: 0x123 => 00000101 (5)
# y: 0x125 => 01010101 (5.0)
# z: 0x135 => 00110101 (True)
# a: 0x118 => 11010101 ('5')

# ----------------------------------- print ---------------------------------- #
# print(1,2,3, sep=',')

# ---------------------------------- integer --------------------------------- #
# print( 23 )
# print( +23 )
# print( -23 )
# print( 1 )
# print( 173284738 )
# print( 2_7_3_284_738 )


# print(1_000.5_7)
# print( 01.01 )

# --------------------------------- Concepts --------------------------------- #
# 2+3  => operatin "Addition"
# +    => operator
# 2, 3 => operands

# ---------------------------------- string ---------------------------------- #

# print( 2 + 3 )
# print( '2'+'3' )


# --------------------------- Arithmetic Operations -------------------------- #

# print( 5/3 )

# print( 5//3 ) # 1

# print( 5%3 ) # 2

# --------------------------- Comparison operation --------------------------- #

# user_age = 21

# print( user_age>=18 )
# if user_age>=18:
#     print('Welcome')
# else:
#     print('You can not use our service!')


# print( 5==9 )
# print( 5!=9 )


# ----------------------------- Logical Operators ---------------------------- #
# and, or, not

user_age = 12
user_country = 'BG'

# print( user_age>=18 )
# print( user_country=='BG')

print( user_age>=18 and user_country=='BG' )

# if  user_age>=18 and user_country=='BG':
#     print('Здравей')