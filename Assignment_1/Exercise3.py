

empName = str(input("Enter th empName:-"))
empSal = int(input("Enter the sal :-"))
incrPercent = int(input("Enter the percent :-"))





print("The value the empName is :-",empName)
print("The value the sal  is :-",empSal)

print("The the sellPrice is :-",incrPercent)



print("The emp details :- ",empName , empSal, incrPercent)

increment = (incrPercent/100)*empSal
increaseSal = increment+empSal

print(f"dear {empName} your is {empSal} rs and ypu have increment of {incrPercent}, ")
print(f"so Congrtaulation you now have your new salary as {increaseSal} rs ")