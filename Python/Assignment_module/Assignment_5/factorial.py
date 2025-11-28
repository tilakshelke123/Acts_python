
def Check_factorial (num):
    fact =1
  
    
    for i in range(1,num+1):
        fact= fact*i
    
    return fact   
    
num = int(input("Enter the Num :-"))
result = Check_factorial(num)
print("the Fcatorial is :-",result)