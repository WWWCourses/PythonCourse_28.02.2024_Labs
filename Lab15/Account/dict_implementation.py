def deposit(account, amount):
    account['balance']+=amount

def withdraw(account, amount):
    if account['balance']<amount:
        print('Not enough balance!')
        return

    account['balance']-=amount

def print_details(account):
    print(f"{account['owner']}=>{account['balance']}")


if __name__=='__main__':
    accounts=[
        {
            'owner':'Maria',
            'balance':1300
        },
        {
            'owner':'Petar',
            'balance':100
        }
    ]


    for account in accounts:
        print_details(account)



