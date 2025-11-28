# fibonacci series 
Num = int(input("Enter the  Number :-"))
a=0
b=1
count=0
for i in range(Num):
     print(a ,end=" ")
     a,b=b,a+b
     count +=1