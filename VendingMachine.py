# Below are the products that is inside my vending machine which are divided into 3 parts:
# Cold drinks, snacks, and hot beverages, which has a corresponding code, name, and price
Cold_drinks=[ # Inside this list, contains differentdictionaries, which is the information of the products.
{"product_code":"A1",         # Code of the product.
 "product_name":"Coke",       # Name of the product.
 "product_price": "5 AED" ,   # Price of the product
 "product_stock": 5,},        # Stock left of product.

{"product_code":"A2",         # Code of the product.
 "product_name":"Sprite",     # Name of the product.
 "product_price": "4 AED" ,   # Price of the product
 "product_stock": 2,},        # Stock left of product. 

{"product_code":"A3" ,        # Code of the product.
 "product_name":"Fanta",      # Name of the product.
 "product_price": "4 AED",    # Price of the product
 "product_stock": 5,},        # Stock left of product. 

{"product_code":"A4" ,        # Code of the product.
 "product_name":"Frappé",     # Name of the product.
 "product_price": "15 AED" ,  # Price of the product
 "product_stock": 3,},        # Stock left of product.

{"product_code":"A5" ,        # Code of the product.
 "product_name":"Water",      # Name of the product.
 "product_price": "2 AED",    # Price of the product
 "product_stock": 1,},        # Stock left of product.
]

snacks=[ #New list: snacks
{"product_code":"B1",         # Code of the product.
 "product_name":"Snickers",   # Name of the product.
 "product_price": "6 AED" ,   # Price of the product
 "product_stock": 5,},        # Stock left of product.

{"product_code":"B2",         # Code of the product.
 "product_name":"Doritos",    # Name of the product.
 "product_price": "8 AED" ,   # Price of the product
 "product_stock": 5,},        # Stock left of product.

{"product_code":"B3" ,        # Code of the product.
 "product_name":"Cookies",    # Name of the product.
 "product_price": "3 AED" ,   # Price of the product
 "product_stock": 4,},        # Stock left of product.

{"product_code":"B4" ,        # Code of the product.
 "product_name":"Cheetos",    # Name of the product.
 "product_price": "8 AED" ,   # Price of the product
 "product_stock": 5,},        # Stock left of product.

{"product_code":"B5" ,        # Code of the product.
 "product_name":"Gummies",    # Name of the product.
 "product_price": "2 AED" ,   # Price of the product
 "product_stock": 2,},        # Stock left of product.
]

Hot_beverages=[               #Third list, Hot beverages
{"product_code":"C1",         # Code of the product.
 "product_name":"Cafe Latte", # Name of the product.
 "product_price": "10 AED",   # Price of the product
 "product_stock": 3,},        # Stock left of product.

{"product_code":"C2",         # Code of the product.
 "product_name":"Cappuccino", # Name of the product.
 "product_price": "12 AED" ,  # Price of the product
 "product_stock": 2,},        # Stock left of product.

{"product_code":"C3" ,        # Code of the product.
 "product_name":"Karak Chai", # Name of the product.
 "product_price": "6 AED" ,   # Price of the product
 "product_stock": 4,},        # Stock left of product.

{"product_code":"C4" ,        # Code of the product.
 "product_name":"Hot milk",   # Name of the product.
 "product_price": "15 AED" ,  # Price of the product
 "product_stock": 3,},        # Stock left of product.

{"product_code":"C5" ,        # Code of the product.
 "product_name":"Macchiato",  # Name of the product.
 "product_price": "10 AED",   # Price of the product
 "product_stock": 3,},        # Stock left of product.
]

# Below are the opening statement of the vending machine, such as the title.
print("\n\t\t\tVending Machine Program\n") # With lines and spaces, to have a clean formatting.

print("\nCold Drinks\n") #Introducing the menu of Cold drinks

for i in Cold_drinks: # For loop to print the list of cold drinks in an organized format.
    # It prints the product name, price, code, and stock.
    print(f"Product: {i['product_name']}\t\t Price: {i['product_price']}\t Code: {i['product_code']} \tStocks: {i['product_stock']}\n")
    
print("\nSnacks\n") #Introducing the menu of snacks.

for i in snacks: # For loop to print the list of snacks in an organized format.
    # It prints the product name, price, code, and stock.
    print(f"Product: {i['product_name']}\t Price: {i['product_price']}\t Code: {i['product_code']} \tStocks: {i['product_stock']}\n")

print("\nHot beverages\n") #Introducing the menu of hot beverages.
    
for i in Hot_beverages: # The same as the for loop for drinks and snacks, but for hot beverages.
    # It prints the product name, price, code, and stock.
    print(f"Product: {i['product_name']}\t Price: {i['product_price']}\t Code: {i['product_code']} \tStocks: {i['product_stock']}\n")

purchased_item= [] # An empty list for purchased item.
total= [] # An empty list to put total amount.


anykey= input("\nPress any key to proceed...\n") #The user will input anything to continue.

# The main function that will take input (money) from users, and ask for the code of the product.
# This function also contains and deducts money for each purchase.
# As well as majority of the how the whole vending machine works is this main function.
def main(): 
     
    # Asking users for the amount of money they have and be inputted in the machine.
    balance = int(input("\nInsert your money (Enter amount):\n"))
    
# Below is the number of products in stocks, if the stock goes 0, the product is sold out.
    A1_stock =5 # Stocks of A1.
    A2_stock =2 # Stocks of A2.
    A3_stock =5 # Stocks of A3.
    A4_stock =3 # Stocks of A4.
    A5_stock =1 # Stocks of A5.
    
    B1_stock =5 # Stocks of B1.
    B2_stock =5 # Stocks of B2.
    B3_stock =4 # Stocks of B3.
    B4_stock =5 # Stocks of B4.
    B5_stock =2 # Stocks of B5.
    
    C1_stock =3 # Stocks of C1.
    C2_stock =2 # Stocks of C1.
    C3_stock =4 # Stocks of C1.
    C4_stock =3 # Stocks of C1.
    C5_stock =3 # Stocks of C1.
      
    while True: # A while loop that will keep on repeating until the user enters q.
        #Asking users for the product code of the product they want.
        buy = input("\nEnter the code of the product you wish to purchase, press q to proceed to payment.\n")

# An if-elif-else chain that process the code, smart suggestion, balance handling, and stock handling. More information below.
        
        if buy == "A1":                             # If the user inputs A1,
            print("\nYou added Coke in your cart")  # prints a statement,
            suggestion = input("\nwould you like to add Doritos with your coke?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B2 to add Doritos\n")# The machine will suggest a code to input.
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 5                            # and deducts 5 to the balance.
            purchased_item.append("Coke--5 AED")    # Add item to purchased item.
            total.append(5)                         # Add price to total empty list.
            A1_stock -= 1                           # Every product bought, will deduct stock by 1.
            if A1_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out, so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "A2":                           # If the user inputs A2,
            print("\nYou added Sprite in your cart\n")# prints a statement,
            suggestion = input("\nwould you like to add Cheetos with your Sprite?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B4 to add Cheetos\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 4                            # and deducts 4 to the balance.
            purchased_item.append("Sprite--4 AED")  # Add item to purchased item.
            total.append(4)                         # Add price to total empty list.
            A2_stock -= 1                           # Every product bought, will deduct stock by 1.
            if A2_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "A3":                           # If the user inputs A3,
            print("\nYou added Fanta in your cart\n")   # prints a statement,
            suggestion = input("\nwould you like to add Doritos with your Fanta?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B2 to add Doritos\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 4                            # and deducts 4 to the balance.
            purchased_item.append("Fanta--4 AED")   # Add item to purchased item.
            total.append(4)                         # Add price to total empty list.
            A3_stock -= 1                           # Every product bought, will deduct stock by 1.
            if A3_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
        
        elif buy == "A4":                           # If the user inputs A4,
            print("\nYou added Frappé in your cart\n")  # prints a statement,
            suggestion = input("\nwould you like to add Snickers with your Frappé?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B1 to add Snickers\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 15                           # and deducts 3 to the balance.
            purchased_item.append("Frappé--15 AED") # Add item to purchased item.
            total.append(15)                        # Add price to total empty list.
            A4_stock -= 1                           # Every product bought, will deduct stock by 1.
            if A4_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "A5":                           # If the user inputs A5,
            print("\nYou added Water in your cart\n")   # prints a statement,
            balance -= 2                            # and deducts 2 to the balance.
            purchased_item.append("Water--2 AED")   # Add item to purchased item.
            total.append(2)                         # Add price to total empty list.
            A5_stock -= 1                           # Every product bought, will deduct stock by 1.
            if A5_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "B1":                           # If the user inputs B1,
            print("\nYou added Snickers in your cart\n")# prints a statement,
            suggestion = input("\nwould you like to add Water with your Snickers?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter A5 to add Water\n")  # The machine will suggest a code to input.
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 6                            # and deducts 6 to the balance.
            purchased_item.append("Snickers--6 AED")# Add item to purchased item.
            total.append(6)                         # Add price to total empty list.
            B1_stock -= 1                           # Every product bought, will deduct stock by 1.
            if B1_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "B2":                           # If the user inputs B2,
            print("\nYou added Doritos in your cart\n") # prints a statement,
            suggestion = input("\nwould you like to add Coke with your Doritos?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter A1 to add Coke\n")   # The machine will suggest a code to input.
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 8                            # and deducts 8 to the balance.
            purchased_item.append("Doritos--8 AED") # Add item to purchased item.
            total.append(8)                         # Add price to total empty list.
            B2_stock -= 1                           # Every product bought, will deduct stock by 1.
            if B2_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "B3":                           # If the user inputs B3,
            print("\nYou added Cookies in your cart\n") # prints a statement,
            suggestion = input("\nwould you like to add Cafe Latte with your Cookies?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter C1 to add Cafe Latte\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 3                            # and deducts 3 to the balance.
            purchased_item.append("Cookies--3 AED") # Add item to purchased item.
            total.append(3)                         # Add price to total empty list.
            B3_stock -= 1                           # Every product bought, will deduct stock by 1.
            if B3_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "B4":                           # If the user inputs B4,
            print("\nYou added Cheetos in your cart\n") # prints a statement,
            suggestion = input("\nwould you like to add Sprite with your Cheetos?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter A2 to add Sprite\n") # The machine will suggest a code to input. 
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 8                            # and deducts 8 to the balance.
            purchased_item.append("Cheetos--8 AED") # Add item to purchased item.
            total.append(8)                         # Add price to total empty list.
            B4_stock -= 1                           # Every product bought, will deduct stock by 1.
            if B4_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "B5":                           # If the user inputs B5,
            print("\nYou added Gummies in your cart\n") # prints a statement,
            suggestion = input("\nwould you like to add Water with your Gummies?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter A5 to add Water\n") # The machine will suggest a code to input. 
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 2                            # and deducts 2 to the balance.
            purchased_item.append("Gummies--2 AED") # Add item to purchased item.
            total.append(2)                         # Add price to total empty list.
            B5_stock -= 1                           # Every product bought, will deduct stock by 1.
            if B5_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "C1":                               # If the user inputs C1,
            print("\nYou added Cafe latte in your cart\n")  # prints a statement,
            suggestion = input("\nwould you like to add Cookies with your Cafe Late?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B3 to add Cookies\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 10                               # and deducts 10 to the balance.
            purchased_item.append("Cafe latte--10 AED") # Add item to purchased item.
            total.append(10)                            # Add price to total empty list.
            C1_stock -= 1                             # Every product bought, will deduct stock by 1.
            if C1_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "C2":                               # If the user inputs C2,
            print("\nYou added Cappuccino in your cart\n")  # prints a statement,
            suggestion = input("\nwould you like to add Snickers with your Cappuccino?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B1 to add Snickers\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 12                               # and deducts 12 to the balance.
            purchased_item.append("Cappuccino--12 AED") # Add item to purchased item.
            total.append(12)                            # Add price to total empty list.
            C2_stock -= 1                             # Every product bought, will deduct stock by 1.
            if C2_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "C3":                               # If the user inputs C3,
            print("\nYou added Karak Chai in your cart\n")  # prints a statement,
            suggestion = input("\nwould you like to add Cookies with your Karak Chai?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B3 to add Cookies\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 6                                # and deducts 6 to the balance.
            purchased_item.append("Karak Chai--6 AED")  # Add item to purchased item.
            total.append(6)                             # Add price to total empty list.
            C3_stock -= 1                             # Every product bought, will deduct stock by 1.
            if C3_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "C4":                               # If the user inputs C4,
            print("\nYou added Hot Milk in your cart\n") # prints a statement,
            suggestion = input("\nwould you like to add Gummies with your Hot Milk?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B5 to add Gummies\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 15                               # and deducts 15 to the balance.
            purchased_item.append("Hot Milk--15 AED")# Add item to purchased item.
            total.append(15)                            # Add price to total empty list.
            C4_stock -= 1                             # Every product bought, will deduct stock by 1.
            if C4_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("\nSorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.
            
        elif buy == "C5":                               # If the user inputs C5,
            print("\nYou added Macchiato in your cart\n")   # prints a statement,
            suggestion = input("\nwould you like to add Cookies with your Macchiato ?\n[1]Yes [2]No\n")
            if suggestion == "1" :                  # a suggestion input where if the users agree,
                print("\nEnter B3 to add Cookies\n")# The machine will suggest a code to input.  
            else:                                   # if the users doesn't agree,
                pass                                # The machine will continue the code.
            balance -= 10                               # and deducts 5 to the balance.    
            purchased_item.append("Macchiato--10 AED")  # Add item to purchased item.
            total.append(10)                            # Add price to total empty list.
            C5_stock -= 1                             # Every product bought, will deduct stock by 1.
            if C5_stock < 1:                        # When the stocks are gone, it will end the code. 
                print("Sorry, this specific product has sold out so we've proceeded to payment.\n")
                break                               # End the loop, cannot purchase anymore.    
            
        elif buy == "q":                        # If the user inputs q,
            print("Proceeding to payment..\n")  # prints a statement,
            break                               # End the loop.
        
        else: # Else statement  
            #Anything that is not listed code above, is an invalid code.
            print("Code invalid, try again..\n")
   
    if balance < 0: # =If final balance will be a negative, the product won't be dispense.
        #It will restart and have an insufficient amount balance.
        print ("Sorry, the amount of money you've inserted is not enough. Try again.\n")
        main() # Goes back to the loop again.
    
    else: # Else statement
        #If every has no problem, then it will give you the change you will recieve.
        print("Change---", balance, "AED\n") 

main() #Calling the main function.

def receipt(): # New function that revolves around the receipt.
    print(*purchased_item, sep = "\n") # purchase_item, was an empty list, but using .append(), it contains the products that are bought. Using a specific format.

    Sum = sum(total) # The total empty list, which will contain the total cost of product bought, also using .append().
    print("\nTotal---" ,Sum,"AED\n")  # Printing the total cost of all the products bought

receipt() #Calling the function. 

from datetime import date # Importing datetime from default modules in python.

today = date.today()      # A variable that stores date today.
print("\nToday's date:", today) # Printing the date time today.

print("\nThank you for availing in Python Vending Machine!!\n") #Printing an ending statement