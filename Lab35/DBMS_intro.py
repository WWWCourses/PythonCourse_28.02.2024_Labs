import json

def get_user_data():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    return name,age

def write_user_data(name, age, filename='./user_data.json'):
    with open(filename, 'w') as f:
        data = (name, age)
        json.dump(data, f)


if __name__=="__main__":
    name, age = get_user_data()
    print(name)
    print(age)

    write_user_data(name, age)


