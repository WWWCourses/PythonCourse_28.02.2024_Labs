# ----------------------------------- sets ----------------------------------- #
# set1 = { 1,2,3,3,2 }
# print( set1 )

### use case:
# data = [1,2,3,3,2]
# unique_data = list(set( data ))
# print( unique_data )


# ------------------------------- loop on sets ------------------------------- #
# for el in { 1,2,3,3,2 }:
#     print(el)

# ------------------------------- add elements ------------------------------- #
# set1 = { 1,2,3 }
# set1.add(4)
# set1.update([1,2,5,6])
# print(set1)


# ------------------------------ remove elements ----------------------------- #
# set1 = { 1,2,3 }
# # set1.discard(4)
# set1.remove(2)
# print(set1)

# -------------------------------- Sets Operations -------------------------------- #
# s1 = {1,2,3}
# s2 = {2,3,4}

# ### union
# # print( s1|s2 )
# print( s1.union(s2) )

# ### intersection
# print( s1.intersection(s2))


# ### difference
# print( s1.difference(s2))  #{1}
# print( s2.difference(s1))  #{4}

### subset
# s1 = {1,2,3,4}
# s2 = {1,2,3,4,5}
# print( s1<s2 )
# print( s2>s1 )
# print( s1>s2 )