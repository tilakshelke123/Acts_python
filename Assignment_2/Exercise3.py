
def fuel_cost (distaance,km_per_litre,cost_per_litre ):
   
   return  (distaance/km_per_litre)*cost_per_litre

distaance= int(input("Enter the distaance :-"))
result = fuel_cost(distaance,km_per_litre = 20,cost_per_litre =30)
print("the cost of fuel cost is :-",result)