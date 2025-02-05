"""
common/atm_operations.py
"""

from typing import Dict
from utils import console_utils
from common import atm_enum


def current_balance(currents_bills: Dict[int, int]) -> None:
    """
    method for view current balance from ATM
    """
    console_utils.clean_console()

    atm_total = 0

    for key, value in currents_bills.items():
        atm_total += key * value

    print(f"Your current balance is: {atm_total}")
    input("Press any key to continue")


def save_money(
    type_bill: atm_enum.Bill,
    currents_bills: Dict[int, int]
) -> None:
    """
    method for save balance from ATM
    """
    print(type_bill, currents_bills)
