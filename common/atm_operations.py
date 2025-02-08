"""
common/atm_operations.py
"""

from typing import Dict
from utils import console_utils
from common import atm_enum


def current_balance(currents_bills: Dict[atm_enum.Bill, int]) -> int:
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

    if current_bill_cant is None:
        print("Error: Incorrect amount.")
        print("Please enter a valid amount.")
        input("Press any key to continue")
        return currents_bills

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

    if withdraw_amount > get_total_bills(currents_bills):
        print("Error: Incorrect amount.")
        print(f"Your current balance is: {get_total_bills(currents_bills)}")
        print("Please enter a valid amount.")
        input("Press any key to continue")
        return currents_bills

    for bill_value in get_bills(currents_bills):
        bill = atm_enum.Bill(bill_value)
        bills_to_dispense = withdraw_amount // bill_value
        num_bill_to_dispense = min(
            currents_bills[bill],
            bills_to_dispense
        )
        withdraw_amount = withdraw_amount - (num_bill_to_dispense * bill_value)
        currents_bills[bill] = currents_bills[bill] - num_bill_to_dispense
        print(f"Quantity bills of {bill.value}: {num_bill_to_dispense}")
        if withdraw_amount <= 0:
            break

    print("Transaction completed successfully!")
    print(f"Your new balance is: {get_total_bills(currents_bills)}")
    input("Press any key to continue")

    # new_total = atm_total - withdraw_amount
    # variable = 0
    return currents_bills


def get_bills(currents_bills: Dict[atm_enum.Bill, int]) -> list[int]:
    """
    method to withdraw balance from ATM
    """
    return sorted(
        [atm_enum.Bill(key).value for key in currents_bills],
        reverse=True
    )


def get_total_bills(currents_bills: Dict[atm_enum.Bill, int]) -> int:
    """
    method to withdraw balance from ATM
    """
    return sum(
        bill.value * count for bill,
        count in currents_bills.items()
    )
