
prices = {"apple": 30, "banana": 10, "bread": 45, "milk": 60}


item_name = input("Enter item name: ").lower()
qty = int(input("Enter quantity: "))


if item_name in prices:
    total_cost = prices[item_name] * qty


    if total_cost > 500:
        discount = 0.15 * total_cost
    elif total_cost > 200:
        discount = 0.10 * total_cost
    else:
        discount = 0

    final_cost = total_cost - discount
    print(f"Total cost before discount: ₹{total_cost}")
    print(f"Discount applied: ₹{discount}")
    print(f"Final cost: ₹{final_cost}")
else:
    print("Item not available")





