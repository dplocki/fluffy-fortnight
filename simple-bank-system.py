class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {(index + 1): value for index, value in enumerate(balance)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (not self.is_correct_account(account1) or
            not self.is_correct_account(account2) or
            self.balance[account1] < money):
            return False
        
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_correct_account(account):
            return False

        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (not self.is_correct_account(account) or 
            self.balance[account] < money):
            return False

        self.balance[account] -= money
        return True

    def is_correct_account(self, account):
        return account in self.balance

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
