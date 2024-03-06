# --------------------------------- f-strings -------------------------------- #
# user_name = 'Ada Byron'

# print( 'Hello ' + user_name + '!')
# print( 'Hello {user_name}!' )
# print( f'Hello {user_name}!' )

# x = 1
# output = f"""
# x = {x}
# """

# print(output)

# x = 5
# y = 10
# result = x+y

# # print(f'{x+y} = result')  #x+y = 15
# print(f'x+y = {result}')  #x+y = 15
# print(f'{x}+{y} = {result}')  #10+5 = 15


# print( 22 + 10 / 5 )
# print( f'{22 + 10 / 5}' )


# -------------------------- string.format() method -------------------------- #
# x = 5
# y = 10
# result = x+y

# print(f'{x}+{y} = {result}')  #10+5 = 15
# print( '{}+{} = {}'.format(x,y,result) )
# print( '{}+{} = {}'.format(1+1,2+2,3+3) )


# value = 83.335333333
# print( '%.2f' % value)
# print( '{:.2f}'.format(value))
# print( f'{value:.2f}')

# print(value)

# # budget = 1000
# # print( budget/12)


# --------------------------------- Examples --------------------------------- #
# # Task: { }’s favorite sports is { }.
# name = 'Pesho'
# sport = 'tennis'

# print( '{}’s favorite sports is {}'.format(name, sport))
# print( f'{name}’s favorite sports is {sport}')



# ---------------------- Format Specificators (Language) --------------------- #

### Format aligned
# x = 1
# print( f'|{x:>10}|' )
# print( f'|{x:<10}|' )
# print( f'|{x:^10}|' )
# print( f'|{x:-^10}|' )
# print( f'|{x:-<10}|' )
# print( f'|{x:->10}|' )


# |---name---|---age---|
# |---Ada----|---23----|

# name = 'Ada'
# age = 23
# print(f'|{'name':-^10}|{'age':-^9}|')
# print(f'|{name:-^10}|{age:-^9}|')



