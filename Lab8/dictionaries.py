### Lists are not always best data structure:
# student1_data = ['ivan', 23, 6]
# student2_data = ['petar', 19, 4]

# prnint( age )
# print( student1_data[1] )

# -------------------------- Dictionarieas overview -------------------------- #
# student1_data = {
#     'name':'ivan',
#     'age':23,
#     'score':6
# }

# print( student1_data['age'] )


# create empty dictionary
# d = {}
# d = dict()

# ---------------------------- Access dict element --------------------------- #
# bg_en= {
#     'ябълка':'apple',
#     'портокал':'orange'
# }

# emoji_to_eng = {
#     'smile': '😊',
#     'heart': '💚',
#     'smile': '!!!',
# }
# print( emoji_to_eng['smile'] )
# print( emoji_to_eng.get('anger', 'No such element') )






# --------------------------- List of dictionaries --------------------------- #




# -------------------------- Nested data structures -------------------------- #
data = {
    'user':{
        'name': 'ivan',
        'town': 'sofia'
    },
    'ids': [1,2,3]
}

# d = data['user']
# print(  d['name'] )

print( data['user']['name'] )
print( data['ids'][0] )



