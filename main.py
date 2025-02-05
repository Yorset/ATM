"""
main.py
"""

# bill = {100: 3, 50: 6, 20: 10, 10: 50, 1: 50}  <- ATM availability
from common import atm_screens, atm_enum


def main():
    """
    main.py
    """

    while True:
        user_option = atm_screens.home_screen()
        print()
        if user_option == atm_enum.UserOptions.CHECK_BALANCE:
            print(atm_enum.UserOptions)

        if user_option == atm_enum.UserOptions.SAVE_MONEY:
            print(atm_enum.UserOptions)

        if user_option == atm_enum.UserOptions.WITHDRAW_MONEY:
            print(atm_enum.UserOptions)

        if user_option == atm_enum.UserOptions.EXIT:
            print(atm_enum.UserOptions)


main()
