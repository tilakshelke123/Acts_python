def Calculator():
    
   Num1 = int(input("Enter the Num1 :- "))
   Num2 = int(input("Enter the Num2 :- "))
   print("The Available Operator are  :- +  -  *  /  " )
   operator = input ("Enter the Operator :- ")
   
   if operator == "+":
    print("the Addition is ",Num1+Num2)   
   elif operator == "-":
       print("The Subtraction is ", Num1-Num2)
   elif operator == "*":
       print("The Multiplication is ", Num1 * Num2)
   elif operator == "/":
       if(Num2 != 0):
           print("The division is :", Num1/Num2)
       else:
           print("Num2 is 0 value . so it gives an Exception Duivide by zero Exception ")
           return
   else:
       print(" you have enetered Wrong Choice ")
   
       return 

Calculator()