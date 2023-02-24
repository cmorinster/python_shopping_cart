
def grocery_order1():
    grocery_order = {}
    prompt = ''
    item = ''
    total = 0.00
    item_r = ''
    
    
    print("Welcome to Cafe Chris!\n")
    while prompt.upper() != "DONE":
        
        prompt = input("What would you like to do?\nAdd Items?  (Type: Add)\nDelete Items?  (Type: Delete)\nSee Current List?  (Type: List)\nCheck Out?  (Type: Done)\n")
        if prompt.upper() == "ADD":
            item = input("What item would you like to add?\n")
            price = input(f"What is the price of the {item}?\n")
            grocery_order[item.upper()] = price
            
        elif prompt.upper() == "DELETE":
            while True:
                item_r = input("what item would you like to remove?\n")
                if grocery_order.get(item_r.upper()) != None:
                    del grocery_order[item_r.upper()]
                    print(f"{item_r.capitalize()} removed\n")
                    break
                else:
                    print(f"{item_r.capitalize()} not found on shopping list\n")
        elif prompt.upper() == "LIST":
            print("Cafe Chris Order:\n\n")
            for item1, price1 in grocery_order.items():
                if len(item1)>7:
                    print(f"{item1.capitalize()}\t\t\t${price1}\n")
                else:
                    print(f"{item1.capitalize()}\t\t\t\t${price1}\n")
                
                
    name = input("Can I have a name for the order?\n")
    print("Cafe Chris Order:\n\n")
    print("Item:\t\t\t\tPrice:")
    for item2, price2 in grocery_order.items():
        if len(item2)>7:
            print(f"{item2.capitalize()}\t\t\t${price2}\n")
        else:
            print(f"{item2.capitalize()}\t\t\t\t${price2}\n")
        total = total + float(price2)
    tax = total*0.05
    total = tax + total
    print(f"Tax:\t\t\t\t${tax:.2f}")
    print(f"Total:\t\t\t\t${total:.2f}\n")
    print(f"Thank You {name} for your Order")
    print("We will call your name when the order is ready!")
          
          
    
        
        
        
        
                    

grocery_order1()