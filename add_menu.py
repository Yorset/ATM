# This is the menu displayed when adding money
# To select the denomination and mount of bills
# to save

def add_menu():
    atm_bills = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}
    switch = True
    while switch:
        print("Please select the denomination of the bill you will introduce")
        print("Then, select the amount of bills you will introduce")
        print(" When done, select 'Exit'")
        print("1. $100")
        print("2. $50")
        print("3. $20")
        print("4. $10")
        print("5. $5")
        print("6. $1")
        print("7. Exit")
        option = int(input())

        if option == 7:
            switch = False

        elif option == 1:
            bill_hundred = 100
            print("Enter the number of bills:")
            cant = int(input())
            atm_bills[bill_hundred] += cant
            print(atm_bills)
            print("Transaction completed successfully!")
            print(f"You saved: {bill_hundred * cant}.")

        elif option == 2:
            bill_fifty = 50
            print("Enter the number of bills:")
            cant = int(input())
            atm_bills[bill_fifty] += cant
            print(atm_bills)
            print("Transaction completed successfully!")
            print(f"You saved: {bill_fifty * cant}.")

        elif option == 3:
            bill_twenty = 20
            print("Enter the number of bills:")
            cant = int(input())
            atm_bills[bill_twenty] += cant
            print(atm_bills)
            print("Transaction completed successfully!")
            print(f"You saved: {bill_twenty * cant}.")

        elif option == 4:
            bill_ten = 10
            print("Enter the number of bills:")
            cant = int(input())
            atm_bills[bill_ten] += cant
            print(atm_bills)
            print("Transaction completed successfully!")
            print(f"You saved: {bill_ten * cant}.")

        elif option == 5:
            bill_five = 5  # <- EL BILLETE
            print("Enter the number of bills:")
            cant = int(input())
            atm_bills[bill_five] += cant
            print(atm_bills)
            print("Transaction completed successfully!")
            print(f"You saved: {bill_five * cant}.")

        elif option == 6:
            bill_one = 1
            print("Enter the number of bills:")
            cant = int(input())
            atm_bills[bill_one] += cant
            print(atm_bills)
            print("Transaction completed successfully!")
            print(f"You saved: {bill_one * cant}.")

        else:
            print("Wrong option.")
            print("Please Select a valid option.")

    return atm_bills
