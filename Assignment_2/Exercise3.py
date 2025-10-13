
def fuel_cost (distaance,km_per_litre =50,cost_per_litre=60 ):
   
   return  (distaance/km_per_litre)*cost_per_litre

distaance= int(input("Enter the distaance :-"))
result = fuel_cost(distaance)

print("the cost of fuel cost is :-",result)
