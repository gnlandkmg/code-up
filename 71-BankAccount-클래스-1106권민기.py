class BankAccount:
    def __init__(self,acnt):
        self.acnt = acnt
        self.balance = 0
    def deposit(self,amt):
        print(f"{self.acnt} 통장에 {amt}원이 입금됨")
        self.balance += amt
        print(f"현재 남은 잔액은 {self.balance}원\n")
        return self.balance
    def withdraw(self,amt):
        print(f"{self.acnt} 통장에 {amt}원이 출금됨")
        self.balance -= amt
        print(f"현재 남은 잔액은 {self.balance}원\n")
        return self.balance
    def check(self):
        print(f"{self.acnt} 통장의 현재 남은 잔액은 {self.balance}원\n")
    def transter(self,target,amt):
        if amt >self.balance:
            print("잔액부족")
        else:
            target.balance -= amt
            self.balance += amt
            print(f'{self.acnt}님이 {target.acnt}니께 {amt}원 송금하였습니다.')
            print(f"{self.acnt} 통장의 현재 남은 잔액은 {self.balance}원\n")

a = BankAccount('123-456')
a.deposit(10000)
a.withdraw(5000)

b = BankAccount('456-789')
b.deposit(2000)

a.check()
a.transter(b,100)
b.check()
a.check()