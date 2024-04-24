import db

class User:
    def __init__(self, name='Anonymous') -> None:
        # self.name = name
        self.setName(name)

    @classmethod
    def input_name(cls):
        name = input('Enter your name:')
        return name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class ATM:
    def __init__(self) -> None:
        self.accounts = [BankAccount(acc['owner'], acc['balance']) for acc in db.accounts]

    def __str__(self):
        pass

    def create_account(self):
        pass
        # user = User()
        # user_name = user.input_name()
        # user.setName(user_name)

        # user_name = User.input_name()


    def print_accounts(self):
        for acc in self.accounts:
            print(acc)

    def get_accounts(self):
        return db.accounts

    def get_account_by_name(self, name):
        account = [acc for acc in self.accounts if acc.owner==name][0]
        return account

class BankAccount:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'owner={self.owner}; balance={self.balance}'

    def withdraw(self, amount:float):
        if amount<=self.balance:
            self.balance-=amount

    def deposit(self, amount:float):
        self.balance+=amount


if __name__ == '__main__':
    atm = ATM()


    maria_account = BankAccount("Maria", 1_300)
    pesho_account = BankAccount("Pesho", 100)

    maria_account.withdraw(500)
    pesho_account.deposit(500)

    atm.print_accounts()