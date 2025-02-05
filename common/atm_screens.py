"""
common/atm_screens.py
"""
from utils import console_utils


def home_screen() -> int:
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
    user_option = int(input("Please select an option:"))

    return user_option
