#6) Take a number from the user and calculate the sum of all even from 1 to that number
Num = int(input("Enter the  Number :-"))
sum = 0
 
for i in range(Num):
  if(i%2==0):
     sum +=i
print(sum)
      
   
   

