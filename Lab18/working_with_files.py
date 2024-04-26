# f = open('./Data/example.txt', 'r')
# # # lines = f.readlines()
# # print(list(f))
# # f.close()

# for l in f:
#     print(l.strip())


# f = open('./Data/example.txt', 'w')
# data = [1,2,3]
# f.writelines([f'{str(el)}\n' for el in data])
# f.close()

with open('./Data/example.txt', 'w' )  as f:
    data = [9,2,3]
    f.writelines([f'{str(el)}\n' for el in data])






