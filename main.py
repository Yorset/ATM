"""
main.py
"""

from common import atm_screens, atm_enum, atm_operations


def main():
    """
    main.py
    """
    atm_balance = {
        100: 3,
        50: 6,
        20: 10,
        10: 50,
        5: 10,
        1: 50
    }  # <- ATM availability

    while True:
        user_option = atm_screens.home_screen()
        if user_option == atm_enum.UserOptions.CHECK_BALANCE:
            atm_operations.current_balance(atm_balance)

        if user_option == atm_enum.UserOptions.SAVE_MONEY:
            option_save_money = atm_screens.save_money_screen()
            atm_operations.save_money(option_save_money, atm_balance)

        if user_option == atm_enum.UserOptions.WITHDRAW_MONEY:
            print(atm_enum.UserOptions)

        if user_option == atm_enum.UserOptions.EXIT:
            print(atm_enum.UserOptions)

        input("INVALID OPTION: press any key to continue")


main()
