# TASK:
# ask user to enter 3 student names and their math scores
# Find the student with max score

# students: ivan | stoyan | petar
# score   :   5  |      3 |    6


# for i in range(3):
#     student = 'ivan'

# print(student)


# ------------------------------ What are lists ------------------------------ #
# student1 = 'ivan'
# student2 = 'stoyan'
# student3 = 'petar'

# # index        0          1        2
# students = ['ivan', 'stoyan', 'petar']

# x = 9
# # RAM:
# #     students   :0x421 => (0x123,0x233,0x531)
# #     students[0]:0x123 => ('ivan')
# #     students[1]:0x233 => ('stoyan')
# #     students[2]:0x531 => ('petar')
# #               x:0x280 => (9)

# --------------------------- Mutable vs Immutable --------------------------- #
# x = 'abc'           # immutable
# l = ['a','b','c']   # mutable

# x[0] = 'b'
# print(x[0])
# l[0] = 'b'
# print(l[0])

# RAM:
#     x[0]: 000=>'a'
#     l[0]: 200=>'a'




# --------------------------------- Examples --------------------------------- #
# l = [1,2,3]
# print(l)
# print(l[0])


# l = ['ivan', 3]
# print(f'{l[0]} has {l[1]}')

# l[0] = l[0].title()
# l[1] += 1

# print(f'{l[0]} has {l[1]}')

# l = [1,2]
# x = 9
# print( 2+2 )
# print( l[0] )
# print( x )


# ---------------------------------- Indexing --------------------------------- #
# list[integer]

l = [1,2,3]
# i = 0
# print( l[ i ])
# print( l[ 0 ])
# print( l[ i+0 ])
# print( l[1+1] )
# print( l[2] )
# print( l[3] )

# print( l[0] )
# print( l[-1] )
# print( l[-2] )
# print( l[-3] )




# # ------------------------------- List of List ------------------------------- #
# l = [1, [2,3], 4 ]
# # print( len(l) )
# x = l[1]
# print( x[1] )
# print( l[1][1] )
# # print( l[ 1,1 ] ] )

# l = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(l)
# print( l[2][0])   # 7

# ------------------------------- id() function ------------------------------ #
# x = 1
# y = x  # copy
# print( id(x) ) # 140665504622536 (i:)
# print( id(y) ) # 140665504622536
# x = 2
# # print( id(x) ) # 140665504622568
# print( x,y )


# x = [1]
# y = x

# print( id(x) ) # 140265501280576 => m
# print( id(y) ) # 140265501280576

# x[0] = 9

# print(x)
# print(y)

# print( id(x) ) # 139698814769096
# print( id(l) ) # 139950655670592

# # RAM:
# #     x: 139698814769096 => 1
# #     l: 139950655670592 => ?
# #  l[0]: 139950655670592 =>



# -------------------------------- copy lists -------------------------------- #
# data = ['ivan', 3]
# # copy = data # this is NOT A COPY
# copy = data[:]
# data[1] = 6

# print(data)
# print(copy)


# ------------------------------ len() function ------------------------------ #
# print( len('abc') )
# print( len([1,[2,3],4]) )
# print( len( range(3) ) )


# ---------------------------------- Slicing --------------------------------- #
# l[start:end:step]
# l[start:end],             step=>1
# l[start:],                end=>-1, step=>1
# l[:end],                  start=>0, step=>1
# l[:],                     start=>0, end=>-1, step=>1

# l = [1,2,3,4,5]
# print( l[0:1])
# # print( l[0:2] )     # [1, 2]
# # print( l[0:2:1] )   # [1, 2]
# # print( l[0:2:2] )   # [1]

# # print( l[:])      # copy
# # print( l[::-1])   # reversed: [5, 4, 3, 2, 1]


# # l1 = l[1::2]
# # print(l1) # [2,4]

# # get the last 2 elements
# l1 = l[-2:]
# print(l1)     # [5,4]

# --------------------------------- append() --------------------------------- #
# l = [1,2,3]
# l.append(9) # inplace

# print( l )

# l.insert(0, 9)

# print(l)









