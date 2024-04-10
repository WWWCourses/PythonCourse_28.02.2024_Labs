l = [1, 2, 3, 1]
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(my_set)
print(set(l))

print(type({1, 2, 3, 4, 5, 1, 2, 3, 4, 5}))
print(type(set(l)))

my_set.add(6)
my_set.discard(111)
my_set.update([6, 7, 8, 9])
print(my_set)
my_set = {"John", "Alex", "Jack"}
print(my_set.pop())
my_set.clear()
print(my_set)

s1 = {1, 2, 3, 4}
s2 = {1, 2, 4}
print(s1 | s2)
print(s1.union(s2))

s3 = s1.intersection(s2)
print(s1 & s2)
print(s1.intersection(s2))
print(s1, s2)

print(s1 == s2)
print(s1 > s2)
print(s2 < s1)

print(tuple(s1))
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2 + (7, 6, 1) + tuple([11, "Hello", True]))
i = 0
while i < len(t1):
    print(t1[i])
    i += 1

my_set = frozenset(s1)
d = {my_set: "Hello"}
print(d)
