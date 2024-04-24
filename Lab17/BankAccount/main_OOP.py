from lib import ATM, BankAccount

def main():
    atm = ATM()


    maria_account = atm.get_account_by_name('Maria')
    pesho_account = atm.get_account_by_name('Pesho')

    # withdraw 500 in Maria's account:
    maria_account.withdraw(500)

    # deposit 500 in Pesho's account
    pesho_account.deposit(500)

    print(atm.accounts)

if __name__ == "__main__":
    main()