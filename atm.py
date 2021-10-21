class Atm(object):
    def __init__(self,withdrawal,balance) :
        self.withdrawal = withdrawal
        self.balance= balance
        #self.transfer = transfer
    def withdrawn(self):
        print("ruppees withdrawn")
    def transferred(self):
        print("money transferred") 
    def balanceQuery(self):
        print("your bank balance is 40,000₹")
pin=input("Enter your pin code= ")

withdraw=int(input("withdraw cash= "))
transfer=input("transfer cash to= ")
transferMoney= int(input("transfer how much money = "))
atm=Atm(withdraw,40000) 
print("your bank balance is 400000")
print(atm.withdrawal)
print(atm.withdrawn()) 
print(transferMoney,"₹ transferred to",transfer)

print("now your bank balance is",atm.balance - withdraw - transferMoney)
#transfer=input("transfer the money to whom= ")





