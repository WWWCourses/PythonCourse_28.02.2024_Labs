# --------------------------- List of dictonaries: --------------------------- #
# data = [
#     {
#         'name': 'Ivan',
#         'email':'ivan@gmail.com'
#     },
#     {
#         'name': 'Maria',
#         'email':'maria@gmail.com'
#     }
# ]

# print(f'User {data[1]['name']} mail is: {data[1]['email']}')

# ------------------------- Dictonary of dictionaries ------------------------ #
# data = {
#     'user1':{
#         'name': 'Ivan',
#         'email':'ivan@gmail.com'
#     },
#     'user2':{
#         'name': 'Maria',
#         'email':'maria@gmail.com'
#     }
# }
# print(f'User {data['user2']['name']} mail is: {data['user2']['email']}')

# ---------------------------- Dictionary methods ---------------------------- #
### Dictionaries are unordered collection
# l = [1,3,2]

# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }
# print(l)
# print(d)

# -------------------------------- Add element ------------------------------- #
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

# d['a'] = 4 #update
# d['d'] = 4 #add

# print(d)

# ------------------------------ update() method ----------------------------- #
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

# d.update({'a':9, 'd':4})
# d.update( [['a', 9],['d', 4]] )
# print(d)

# ------------------------------ Remove element ------------------------------ #
# l = [1,3,2]
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

### del
# del l[1]
# del d['c']

# print(l)
# print(d)

### pop
# l_el = l.pop(1)
# d_el = d.pop('c')
# print(l, l_el)
# print(d, d_el)

# -------------------------- Copy Dictionaries/List -------------------------- #
# Copy mutable structure (list, dict)
# d = {'a':1}
# copy_d = d # NOT A COPY
# d['a'] = 9
# print(d)
# print(copy_d)

# Copy immutable (numbers, string)
# x = 4
# copy_x = x
# x = 9

# print(x)      #9
# print(copy_x) # 4

### MAKE SHALLOW COPY
# d = {'a':1}
# copy_d = d.copy() # THIS IS A COPY
# d['a'] = 9
# print(d)
# print(copy_d)


# d = {'a': [1]}
# copy_d = d.copy()
# d['a'][0] = 9

# print(d)
# print(copy_d)

### Example
# data = [
#     {
#         'name': 'Ivan',
#         'email':'ivan@gmail.com'
#     },
#     {
#         'name': 'Maria',
#         'email':'maria@gmail.com'
#     }
# ]

# data_backup = data.copy()
### equivalent of above
# data_backup = []
# for el in data:
#     data_backup.append(el)

# data.pop(0)
# data[0]['name']='Pesho'
# print(data)
# print('*'*30)
# print(data_backup)

# --------------------------------- DEEP COPY -------------------------------- #
# import json
# data = [
#     {
#         'name': 'Ivan',
#         'email':'ivan@gmail.com'
#     },
#     {
#         'name': 'Maria',
#         'email':'maria@gmail.com',

#     }
# ]

# copy_data = json.loads(json.dumps(data))

# data[1]['name'] = 'Pesho'
# print(data)
# print(copy_data)



# -------------------------------- dict.keys() ------------------------------- #
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

# print( list(d.keyBs()) )
# d['f'] = d['b']
# del d['b']
# print( d.keys() )


# TASK: print all d keys=>values
# for key in d.keys():
# for key in d:
#     print( f'{key}=>{d[key]}' )

# ------------------------------- dict.values() ------------------------------ #
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

# # print( d.values() )
# for val in d.values():
#     print(val)

# ------------------------------- dict.items() ------------------------------- #
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

# print( d.keys() )
# print( d.values() )
# print( d.items() )

# TASK: print all d keys=>values
# for key,value in d.items():
#     print(f'{key}=>{value}')


# data = {
#     'user1':{
#         'name': 'Ivan',
#         'email':'ivan@gmail.com',
#         'address': {
#             'town': 'Sofia',
#             'country':'Bulgaria'
#         }
#     },
#     'user2':{
#         'name': 'Maria',
#         'email':'maria@gmail.com',
#         'address': {
#             'town': 'London',
#             'country':'UK'
#         }
#     }
# }


# print( data.values() )

# --------------------------- Sorting dictionaries --------------------------- #
# d = {
#     'a':1,
#     'c':3,
#     'b':2
# }

# d_sroted_keys = sorted(d)
# d_sroted_values = sorted(d.values())
# print(d_sroted_keys)     # ['a', 'b', 'c']
# print(d_sroted_values)   # ['a', 'b', 'c']


