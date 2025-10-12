
unit = int(input("Enter the unit :- "))
singleUnitcost = 100

purchased_Amount = unit * singleUnitcost

print("purchased amoiunt :-",purchased_Amount)

if(purchased_Amount >1000):
   discount = purchased_Amount*0.1
   total = purchased_Amount-discount
   print(" total with discount2 :",total)

else:
   total=purchased_Amount
   print("total:-",total)