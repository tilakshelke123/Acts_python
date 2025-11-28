num = int(input("Please enter the number"))
	
if num %5==0 and num % 3 ==0 :
 print("Fizz Buzz")
elif num%3 == 0 :
 print("Fizz")
elif num%5 == 0 :
 print("Buzz")
else:
 print("Invalid Input")