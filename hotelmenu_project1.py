menu ={
    'pizza':499,
    'pasta':50,
    'burger':199,
    'salad':40,
    'coffee':80,
}

print("Welcome to our resturant, here's the menu:")
print("pizza:Rs499\n pasta:Rs50\n burger:Rs199\n salad:Rs40\n coffee:Rs80")

order_total=0

item_1 = input("Enter the name of item you wamt to order = ")
if item_1 in menu:
      order_total += menu[item_1]
      print("your item",item_1,"have been added to your order")
else:
    print("order item",item_1,"is not avaialable yet!")

another_order = input("Don you want to add another item? (yes/no)")
if another_order == "yes" :
   item_2 = input("Enter the name of  second item = ")
   if item_2 in menu :
       order_total += menu[item_2]
       print("item",item_2,"has been added to order")
   else:
       print("orderd item",item_2,"is not avaialable!")
print("The total amount of item to pay is",order_total)