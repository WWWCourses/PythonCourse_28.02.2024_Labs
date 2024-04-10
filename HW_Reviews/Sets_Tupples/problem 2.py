A = set([1, 2, 3])
B = set([2, 3, 4])

result = set()
result.add(frozenset(A - B))
result.add(frozenset(B))
result.add(frozenset(B - A))
result.add(frozenset(A - B).union(B - A))
result.add(frozenset(A & B))
result.add(frozenset(A | B))
print(result)
