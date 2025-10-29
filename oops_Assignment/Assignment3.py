# Create classes that capture bank customers and bank accounts.
#A customer has a first and last name. An account has a customer and a balance.
# Make objects for two accounts held by the same customer.

class Customers:
    
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname=lname
    
    def displayCust (self):
        print(f"{self.fname}")
        print(f"{self.lname}")
        
        
class Accounts:
    def __init__(self,customer,balance):
        self.customer= customer
        self.balance=balance
    
    
    def displayAcct (self):
       print(f"{self.customer}")
       print(f"{self.balance}") 
         
        
        
    
        
        
def main():
    tilak_dac= Customers("dac tilak","Shelke")
    savingAccount = Accounts("ccst Tilak",85000)
    currentAccount = Accounts("desd tilak",86000)
    
    # print(tilak_dac.displayCust())
    # print(savingAccount.displayAcct())
    # print(currentAccount.displayAcct())
    
    tilak_dac.displayCust()
    savingAccount.displayAcct()
    currentAccount.displayAcct()
    
    
if __name__ =='__main__':
 main()