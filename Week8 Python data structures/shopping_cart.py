# Create a shopping cart programme that will continously ask the user for food and the price of that product.
# Have an exit clause if the user wishes to stop adding more items to their cart.
# At the end show the food items and the total cost to the user.

foods = []
prices = []
total = 0

while True:
  food = input("Enter a food to buy or press q to quit: ")
  if food.lower() == 'q':
    break
  else:
    price = float(input(f"Enter the price for {food}: "))
    foods.append(food)
    prices.append(price)

print("........ YOUR CART......")      

for food in foods: 
  print(food)
  
for price in prices:
  total += price
  
print(f"Your total is: R{total}")
  