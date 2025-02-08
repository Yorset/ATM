"""
common/atm_operations.py
"""

from typing import Dict
from utils import console_utils
from common import atm_enum


def current_balance(currents_bills: Dict[atm_enum.Bill, int]) -> None:
    """
    method for view current balance from ATM
    """
    console_utils.clean_console()

    atm_total = 0

    for key, value in currents_bills.items():
        atm_total += key.value * value  # <- changed by adding '.value' to key.

    print(f"Your current balance is: {atm_total}")
    input("Press any key to continue")

    return atm_total


def save_money(
    type_bill: atm_enum.Bill,
    currents_bills: Dict[atm_enum.Bill, int]
) -> Dict[atm_enum.Bill, int]:
    """
    method for save balance from ATM
    """
    input_bill_cant = int(input(
        f"Input the number of bills (${type_bill.value}): "
    ))
    current_bill_cant = currents_bills.get(type_bill)

    currents_bills[type_bill] = current_bill_cant + input_bill_cant
    print(currents_bills)
    print("-------------------------")
    print(type_bill, currents_bills)
    return currents_bills


def withdraw(
    withdraw_amount: int,
    currents_bills: Dict[atm_enum.Bill, int]
) -> Dict[atm_enum.Bill, int]:
    """
    method to withdraw balance from ATM
    """

    atm_total = sum(
        bill.value * count for bill,
        count in currents_bills.items()
    )

    if withdraw_amount > atm_total:
        print("Error: Incorrect amount.")
        print(f"Your current balance is: {atm_total}")
        print("Please enter a valid amount.")
        input("Press any key to continue")
        return currents_bills

    for bill in currents_bills:
        bills_to_dispense = withdraw_amount // bill.value
        num_bill_to_dispense = min(currents_bills[bill], bills_to_dispense)
        print(num_bill_to_dispense)

    print("Transaction completed successfully!")
    print(f"Your new balance is: {atm_total}")
    input("Press any key to continue")

    # new_total = atm_total - withdraw_amount
    # variable = 0
    return None
