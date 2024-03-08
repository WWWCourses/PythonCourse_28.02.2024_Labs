# --------------------------- expressions => value --------------------------- #
# print( 2+2 )

# x = 3
# print( x )


# ------------------------------------ if ------------------------------------ #
# Example 1:
# if 2:
#     print('Hi')

# print( bool('') )
# print( bool(0) )
# print( bool(-0.0000000000) )
# print( bool(-0.0000000001) )

# user_age = 12
# country = 'BG'

# if user_age >= 18:
#     print('Welcome')

# if country=='BG':
#     print('Здравей')


# ---------------------------------- if-else --------------------------------- #
# user_age = 23

# if user_age >= 18:
#     print('Welcome')
# else:
#     print('Go home')

# print('END')


# ------------------------------ if -elif - else ----------------------------- #
# TASK:
# if x is even => print('Even')
# if x is odd  => print('Odd')
# if x is zero  => print('Zero')


# x = 5

# if x != 0:
#     if x%2==0:
#         print('Even')
#     else:
#         print('Odd')
# else:
#     print('Zero')


# if x == 0:
#     print('Zero')
# elif x%2==0:
#     print('Even')
# else:
#     print('Odd')


# x = 2

# if x>0:print('Positive');print('END IF')

# print('End Program')


# if 3:
#     print('Hi')

# ----------------------------- Logical Operators ---------------------------- #
# Logical AND (and)
# print( 2 + 3 )
# print( 2 and 3 )


# print( True and False)   # F
# print( False and True)   # F
# print( False and False)  # F
# print( True and True)    # T

# x and y: if x is false, then x, else y
# print( 0 and 2 ) # 0
# print( 2 and 0 ) # 0

# print( '' and 3.5-2.5-0.5 ) # ''


# user_age = 19
# country = 'BG'

# # If user as addult and is from Bulgaria
# if user_age>=18 and country=='EN':
#     print('Welcome')



# Logical OR
# print( True or False )  # True
# print( False or False ) # False
# print( False or True )  # True
# print( True or True )   # True


# # If user as addult or is from EN = > say 'Welcome'
# user_age = 19
# country = 'BG'

# if user_age>=18 or country=='EN':
#     print('Welcome')


# x or y: if x is false, then y, else x

# if user_name=='':
#     user_name = 'Anonymous'


# user_name = ''
# user_name or (user_name:='Anonymous')

# print(user_name) #


# Logical NOT
# print( not True )
# print( not False )

# print( not 2 )
# print( not '' )

# print(9 < 1000)     # True
# print("9" < "1000") # False

# print("9" < "1") # ?
# print("a" < "A") # False
# # print(97 < 65)   #

# user_age = 0

# if not 0<user_age<120:
#     pass

# print('End')


# ----------------------------- Ternary Operator ----------------------------- #
# user_age = 34
# # user_status = ''

# # if user_age>=18:
# #     user_status = 'Adult'
# # else:
# #     user_status = 'Child'

# # variable =  value1 if <expr> else value2
# user_status = 'Adult' if user_age>=18 else 'Child'

# print(user_status)

# print( bool( 2 if 4>5 else 1 ) )
# if 2 if 4>5 else 1:
#     print('Hi')

