class BankAccount:
    def __init__(self) -> None:
        self.__bank="HBL Bank"  # Encapsulated attribute
        self.__name="Danial Rashid"  # Encapsulated attribute
        self.__balance=5000  # Encapsulated attribute
        self.__Pin=5151  # Encapsulated attribute
        self.tax_rate = 0.05  # Encapsulated attribute
    
    def changePin(self):
        self__old=int(input("Enter your 4 digit Old PIN: "))
        if self__old==self.__Pin:
            self.__Pin=int(input("Enter your 4 digit New PIN: "))
        else:
            print("PIN not Match")    

    def deposit(self):
        self.__pin=int(input("Enter your 4 digite PIN: "))
        if self.__pin==self.__Pin:
           self.__dep=float(input("Enter Deposit Amount: "))
           print("*******************Deposite Amount Info***************************")
           print("Your Old Balance is Rs: ",self.__balance)
           self.__balance +=self.__dep
           print("Your Deposited Amount is Rs: ",self.__dep)
           print("Your New Balance is Rs: ",self.__balance)
           print("**********************************************")
        #    return print(f"Your New Balance after deposit {self.__dep} Rs :",self.__balance)
        else:
            return print("Invalid PIN")
        
    def withdrawal(self):
        self.__pin=int(input("Enter your 4 digite PIN: "))
        if self.__pin==self.__Pin:
           self.__with=float(input("Enter withdrawal Amount: "))
           if self.__with < self.__balance:

            print("*****************Withdrawal Amount Info*******************")
            print("Your Old Balance is Rs: ",self.__balance)
            tax__amount = self.__with * self.tax_rate
            total__withdrawal = self.__with + tax__amount
            self.__balance -= total__withdrawal
            print("Your withdrawal Amount is Rs: ",self.__with)
            print("Tax on Amount is Rs: ",tax__amount)
            print("Your New Balance is Rs: ",self.__balance)
            print("**********************************************")
            # return print(f"Your withdrawal amount is {self.__with} Rs and your remaining balance is: ",self.__balance)
           else:
              return print("Insufficient balance")
              
        else:
            return print("invalid pin")
        
    def accountinfo(self):
        print("////////Account Info//////////")
        print("Bank Name: ",self.__bank)
        print("Customer Name: ",self.__name)
        print("Your Balance: ",self.__balance)
        print("///////////////////////////")

    
    def tax(self):
        pass

# Main program
def main():
    obj = BankAccount()
    while True:
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Change PIN")
        print("4. Account Info")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.deposit()
        elif choice == 2:
            obj.withdrawal()
        elif choice == 3:
            obj.changePin()
        elif choice == 4:
            obj.accountinfo()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

