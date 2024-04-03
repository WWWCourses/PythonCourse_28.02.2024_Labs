s = set([1,2,3])
fs = frozenset([2,3])

print( s>fs )

s.add(4)
print(s)
fs.add(4)