import numpy as np

# a = np.arange(1,10)
# l = list(range(1,10))

# print(a)
# print(l)

# --------------------------------- 1D Array --------------------------------- #
# Indexing
# print( l[3])
# print( a[3])
# print( a[-2] ) #?

# Slicing
# print( a[2:6:2] )
# print( a[5:] )
# print( a[::-1] )
# print( l[::-1] )

# --------------------------------- 2D Array --------------------------------- #
# ml = [
#     [1,2,3],
#     [4,5,6]
# ]

# ma = np.array( ml )

# print(ml)
# print(ma)

# print( ml[1][1])
# print( ma[1][1]) # NOT MEMORY EFFICIENT!!!
# print( ma[1,1])  # BEST PRACTICE

# print( ma[-1,1]) #

# m = np.arange(1,17).reshape(4,4)
# print(m)

# print( m[1::2, 1] )  #[6,14]

# print( m[-2:, 3])
# [ 9 10 11 12]
# [13 14 15 16]

# print( m[-2::-1, ::-2] )
# -2::-1=> -2, -3, -4

# [ 9 10 11 12]
# [ 5  6  7  8]
# [ 1  2  3  4]

# ----------------------------- Advanced Indexing ---------------------------- #
# a1 = np.arange(1,6)
# print(a1)

# Boolean Indexing
# print( a1>3 ) # [F, F, F, T, T]
            # [1 2 3 4 5]
# print( a1[ [False, False, True, True, False ] ]) # [3 4]

# example:
# a1 = np.arange(1,11)
# print(a1)

# evens = a1[ a1%2==0 ]
# print(evens)
# x = 8
# if x%2==0:
#     print('Even')


# a1 = np.arange(1,5)

# a2d = np.arange(1,10).reshape(3,3)
# print(a2d)


# mask = a2d%2==0
# print(mask)

# a2d_evens = a2d[ mask ]
# print( a2d_evens )


# Integer Array Indexing
# a1 = np.arange(1,10)
# print(a1)

# [1 2 3 4 5 6 7 8 9]
# print( a1[ [0,0] ] )  # [1,1]
# print( a1[ [0,1,0,1,8] ] )  # [1,2,1,2,9]


# TASK:
# Define the scores array
# scores = np.array([
#     [4, 1],
#     [2, 0],
#     [3, 0],
#     [5, 1],
#     [6, 1]
# ])

# # Define the categories
# categories = ['bad', 'good']

# good_mask  = scores[:,1]==1
# # print( good_mask)
# print( scores[good_mask,0] )


# bad_scores = scores[ scores[:,1]==0, 0]
# print(bad_scores)
# # good_scores = [4,5,6]
# # bad_scores =  [2,3]


# TASK:
# let's have a numpy array of repeated values 0, 1 or 2:
# indexes = np.array([0, 2, 1, 2, 0, 1, 2])

# # and an array of colors:
# colors = np.array(['red', 'green', 'blue'])

# print( colors[ [0,0,0] ]) # []

# colors_map = colors[ indexes ]
# print( colors_map)