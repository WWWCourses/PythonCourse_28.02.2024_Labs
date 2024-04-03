# l = [1,2,3]
# for el in l:
#     print(el)

# get l iterator:
# l_iter = iter(l)
# l_iter = l.__iter__()
# el1 = next(l_iter)
# el2 = l_iter.__next__()
# el3 = next(l_iter)
# print(el1,el2, el3)

# r = range(3)
# r_iter = iter(r)
# print( next(r_iter) )
# print( next(r_iter) )
# print( next(r_iter) )

# from itertools import count

# for el in count(3,9):
#     print(el)


# -------------------------- Create custom iterable -------------------------- #
class FiveNumbers:
    def __init__(self) -> None:
        self.num = 1
        self.count = 5

    def __iter__(self):
        return self

    def __next__(self):
        while self.count>0:
            self.count-=1
            return self.num
        raise StopIteration

fn = FiveNumbers()
for el in fn:
    print(el)