import db

def input_accounts_data():
    pass

def get_accounts():
    return db.accounts

def get_account_by_name(name, accounts):
    account = [acc for acc in accounts if acc['owner']==name][0]
    return account

def withdraw(amount:float, account):
    if amount<=account['balance']:
        account['balance']-=amount

def deposit(amount, account):
    account['balance']+=amount

def main():
    accounts = get_accounts()
    # withdraw 500 in Maria's account:
    maria_account = get_account_by_name('Maria', accounts)
    withdraw(500, maria_account)

    # deposit 500 in Pesho's account
    pesho_account = get_account_by_name('Pesho', accounts)
    deposit(500, pesho_account)

    print(accounts)


if __name__ == "__main__":
    main()


