"""
common/atm_screens.py
"""
from utils import console_utils
from common import atm_enum


def home_screen():
    """
    ATM | home screen
    """
    console_utils.clean_console()
    print("---------------- ATM ------------------")
    print("1. Check Balance.")
    print("2. Save Money.")
    print("3. Withdraw Money.")
    print("4. Exit.")
    print("---------------------------------------")
    input_option = int(input("Please select an option:"))
    option = atm_enum.UserOptions[input_option]
    return option
