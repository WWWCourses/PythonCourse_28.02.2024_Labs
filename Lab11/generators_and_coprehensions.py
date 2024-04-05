l = [1,2,3]

# list comprehension
print( type([el**2 for el in l]) )

# set comprehension
print( type({el**2 for el in l}) )

# generator comprehension
print( type((el**2 for el in l)) )


# non-lazy evaluation
for x in [el**2 for el in l]:
    print(x)

# lazy evaluation
for x in (el**2 for el in l):
    print(x)
