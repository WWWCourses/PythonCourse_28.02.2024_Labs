class BankAccount:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"""
BankAccount:
 owner = {self.owner}
 balance = {self.balance}
"""

maria_account = BankAccount("Maria", 1_300)
pesho_account = BankAccount("Pesho", 100)

print(maria_account)
print(pesho_account)

# OUTPUT:
# BankAccount:
#  owner = Maria
#  balance = 1300
#BankAccount:
# owner = Pesho
# balance = 100