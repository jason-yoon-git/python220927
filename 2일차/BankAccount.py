# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화 메서드
    def __init__(self, id, name, balance):
        # self.id = id
        # self.name = name 
        # self.balance = balance 
        # 수정후 __* private 이름규칙
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        # self.balance += amount 
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        # self.balance -= amount
        self.__balance -= amount
    #결과 문자열
    def __str__(self):
        # return "{0} , {1} , {2}".format(self.id, \
        #     self.name, self.balance)
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

account1.balance = 15000000
print(account1)
# print(account1.__balance)
#외부에서는 _클래스명__변수명
print(account1._BankAccount__balance)