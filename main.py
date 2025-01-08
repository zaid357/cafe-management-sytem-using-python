menu = {
  'pizza': 60,
  'burger': 50,
  'fries': 20,
  'coke': 10,
  'sprite': 10,
  'fanta': 10,
  'tea': 20,
  'coffee': 25,
  'pancake': 30,
}

print("Welcome to the resturant!")
print("Here is the menu")

print("pizza: Rs60\nPasta: Rs40\nBurger: Rs50\nFries: Rs20\nCoke: Rs10\nSprite: Rs10\nFanta: Rs10\nTea: Rs20\nCoffee: Rs25\nPancake: Rs30")
Order_total=0
while True:
  Order=input("What would you like to order? ")
  if Order in menu:
    Order_total+=menu[Order]
    print("Your order total is Rs",Order_total)
  else:
    print("Sorry, we don't have that item.")
  Continue=input("Would you like to order anything else? ")
  