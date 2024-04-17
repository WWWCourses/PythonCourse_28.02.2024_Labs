class Account:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self, amount):
        if self.balance<amount:
            print('Not enough balance!')
            return

        self.balance-=amount

    def print_details(self):
        print(f"{self.owner}=>{self.balance}")


if __name__=='__main__':
    accounts=[
        Account('Maria', 1300),
        Account('Petar', 100)
    ]


    for account in accounts:
        account.print_details()



