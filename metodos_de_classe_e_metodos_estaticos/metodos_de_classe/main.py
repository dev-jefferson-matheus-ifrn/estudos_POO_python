from bank_account import BankAccount

bank_account = BankAccount("Jefferson")

print(bank_account.holder, bank_account.balance)
print()

bank_account.balance = 100
print(bank_account.balance, bank_account.holder)

bank_account2 = BankAccount.create_account_with_balance("Matheus")

print(bank_account2.holder, bank_account2.balance)
