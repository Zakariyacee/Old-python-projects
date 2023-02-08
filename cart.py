from operator import index


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.__cart = []


    def add_to_cart(self, item):
        self.__cart.append(item)

    def remove_from_cart(self,index):
        self.__cart.pop(index)

    def calculatetotal(self):
        total = 0
        for item in self.__cart:
            total += item.price

        return total
    
    def displaycart(self):
        for i in range(0, len(self.__cart)):
            print(1, self.__cart[i].name)


shop = Shop()
shop.add_to_cart(Item("Me", 1999))
shop.displaycart()

print("Welcome to our store!")
while True:
    shop.displaycart()
    shop.calculatetotal()

    print("Press a to add item to your cart")
    print("Press r to remove item from your cart")
    print("Press x to exit")
    user_input = input("Please enter your command here: ")
    
    if user_input == "x":
        break
    elif user_input == "a":
        itemname = input("Please enter the item name: ")
        price = int(input("Please emter item price: "))
        shop.add_to_cart(Item(itemname, price))
    elif user_input == "r":
        index = int(input("Please enter the index of the item you want removed: "))
        shop.remove_from_cart(index)
    else:
        Print("Please enter a valid command.")
