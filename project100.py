class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def BalanceEnquiry(self):
        print("your balance is 1000")        
    def CashWithdrawl(self,amount):
        if amount>=1000:
            print("Sorry! Can't withdraw money due to unsufficient amount")
        else:
            newAmount=1000-amount
            print("you have withdrawn amount" + str(amount)+"Your remaining balance is" + str(newAmount))

def main():
    CardNumber= input("insert your card number:-")
    pinNumber= input("enter your pin card:-")

    newUser=Atm(CardNumber,pinNumber)
    print("Choose your activity")
    print("1.BalanceEnquiry 2.withdrawl")
    activity=int(input("enter activity number:-"))

    if(activity==1):
        newUser.BalanceEnquiry()
    elif(activity==2):
        amount=int(input("enter the amount:-"))
        newUser.CashWithdrawl(amount)
    else:
        print("enter a vailed number")

if __name__ == "__main__":
    main()