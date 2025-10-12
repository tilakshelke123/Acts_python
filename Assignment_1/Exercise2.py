

stockName = str(input("Enter the stockName:-"))
buyPrice = int(input("Enter the buyPrice :-"))
sellPrice = int(input("Enter the sellPrice :-"))
noOfunit = int(input("Enter the numOfUnit :-"))




print("The value the stockName is :-",stockName)
print("The value the buyPrice  is :-",buyPrice)

print("The the sellPrice is :-",sellPrice)
print("The value the numOfUnit is :-",noOfunit)

profit = (sellPrice - buyPrice)* noOfunit
print("The Profit is :-",profit)

