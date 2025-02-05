# Function created just for calculating the total amount
# of money in the atm. Will be used into the withdraw function


def calculate_total_atm_amount():
    bill = {100: 3, 50: 6, 20: 10, 10: 50, 5: 30, 1: 50}  # <- Pending confirmation of how to integrate variable
    atm_total = 0
    for key, value in bill.items():
        atm_total += key * value
    return atm_total


print(calculate_total_atm_amount())
