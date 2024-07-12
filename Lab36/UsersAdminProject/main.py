from db import DB

def get_user_data():
    name = input('Enter your name: ')
    passwd = int(input('Enter your pass: '))
    return name,passwd


def register_user()->bool:
    name, passwd = get_user_data()
    try:
        obj_id = db.insert_user(name, passwd)
        return True
    except Exception as e:
        print(f'Registration error: {e}')
        return False


def login_user():
    name, passwd = get_user_data()
    # get document with given name


if __name__=='__main__':
    db = DB()
    # db.list_collections('alabala')

    # if register_user():
    #     print('User is registered!!')
    # else:
    #     print('User NOT registered!')


    lo


