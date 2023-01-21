import sqlite
import datetime
MENU_PROMPT = """ 

Please choose one of these options:

1) Add a new purchase
2) See all purchases
3) Find a purchase by name
4) Find purchase by date
5) Add deposit
6) Check all deposits
7) Delete a purchase
8) See your biggest purchase
9) See your smallest purchase

Your selection:
"""

def menu():
    connection = sqlite.connect()
    
    sqlite.create_tables(connection)   

    while (user_input := input(MENU_PROMPT)) != 10:
        print()
        # Add purchases to tables
        if user_input == "1":
            name = input("Enter purchase type:")
            money_spent = float(input("How much was your purchase?:$ "))
            date_purchase = input("What was the date of the purchase? YYYY-MM-DD: ")

            sqlite.add_purchase(connection, name, money_spent, date_purchase)
            print("---------------------------------------------------------")
            # Re-print purchases
            purchases = sqlite.get_all_purchase(connection)

            for purchase in purchases:
                print(purchase)
            print("-----------------------------------------------------------")
            # Use Update to change the price of any item
            
            check = input("Does amount look correct? Y/N: ")

            if check.upper() == "N":
                id = input("What is the purchase id? ")
                amount = float(input("What is the correct amount?: "))
                sqlite.update_purchase(connection, amount, id)

            else:
                pass

            
            
            
        elif user_input == "2":
            purchases = sqlite.get_all_purchase(connection)

            for purchase in purchases:
                print(purchase)

        elif user_input == "3":
            name = input("What is the name of the purchase you are looking for? ")
            purchases = sqlite.get_purchase_by_name(connection, name)

            for purchase in purchases:
                print(purchase)

        elif user_input == "4":
            date = input("What date would you like to see purchases from? YYYY-MM-DD: ")
            purchases = sqlite.get_purchase_date(connection, date)
        
            for purchase in purchases:
                print(purchase)
        elif user_input == '5':
            deposit = float(input("How much is deposited? $ "))
            deposit_date = input("What is date of deposit? YYYY-MM-DD: ")
            sqlite.add_deposit(connection, deposit, deposit_date)
        
        elif user_input == "6":
            deposits = sqlite.get_all_deposits(connection)
            for deposit in deposits:
                print(deposit)
        
        elif user_input == "7":
            # List all the purchases
            purchases = sqlite.get_all_purchase(connection)

            for purchase in purchases:
                print(purchase)
            print("------------------------------------------")
            
            purchase_id = input("What is is the purchase id that you'd like to delete? ")
            sqlite.delete_purchase(connection, purchase_id)

        elif user_input == "8":
            print("This was your biggest expense")
            max_purchase = sqlite.max_purchase(connection)
            for purchase in max_purchase:
                print(purchase)

        elif user_input == "9":
            print("This was your smalles purchase")
            min_purchase = sqlite.min_purchase(connection)
            for purchase in min_purchase:
                print(purchase)


        else:
            print("Invalid input, please try again")

menu()


