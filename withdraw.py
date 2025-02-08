# Function to withdraw money
# I need this function to access the dictionary of the ATM
# with the bills denominations and amounts of each one
# then take the bills in order from biggest to smalles deno
# till completion of the withdraw amount.

from atm_total_amount import calculate_total_atm_amount


def withdraw():
    bill = {100: 3, 50: 6, 20: 10, 10: 50, 1: 50}  # <- Pending how to use this variable
    sorted_bills = sorted(bill.keys(), reverse=True)
    atm_total = calculate_total_atm_amount()

    print("Please enter the amount you would like to withdraw.")
    desired_amount = int(input())

    if desired_amount > atm_total:
        print("Transaction error. Amount entered is incorrect.")
        print(f"Please enter a correct amount. Your balance is: {atm_total}.")
        # Pending to fix, prints error but keeps running.
        # I need it to cancel, go back to withdraw menu and ask for
        # new valid desired amount. (possible fix "return none")
    
    elif desired_amount <= atm_total:
        dispensed_bills = {}

        for bill_value in sorted_bills:
            num_bill_to_dispense = min(bill[bill_value], desired_amount // bill_value)

        print ("Transaction completed successfully!")
        print (f"Your new balance is: {atm_total}")
