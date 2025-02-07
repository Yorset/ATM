"""
main.py
"""

from common import atm_screens, atm_enum, atm_operations


def main():
    """
    main.py
    """
    atm_balance = {
        atm_enum.Bill.HUNDRED: 3,
        atm_enum.Bill.FIFTY: 6,
        atm_enum.Bill.TWENTY: 10,
        atm_enum.Bill.TEN: 50,
        atm_enum.Bill.FIVE: 10,
        atm_enum.Bill.ONE: 50
    }  # <- ATM availability

    while True:
        user_option = atm_screens.home_screen()
        if user_option == atm_enum.UserOptions.CHECK_BALANCE:
            atm_operations.current_balance(atm_balance)

        if user_option == atm_enum.UserOptions.SAVE_MONEY:
            option_save_money = atm_screens.save_money_screen()
            atm_balance = atm_operations.save_money(
                option_save_money,
                atm_balance
            )

        if user_option == atm_enum.UserOptions.WITHDRAW_MONEY:
            amount_to_withdraw = atm_screens.withdraw_money_screen()
            atm_balance = atm_operations.withdraw(
                amount_to_withdraw,
                atm_balance
            )
            print(atm_enum.UserOptions)

        if user_option == atm_enum.UserOptions.EXIT:
            print(atm_enum.UserOptions)

        input("INVALID OPTION: press any key to continue")  # This is wrong,
        # gotta be fixed.
        # When initially pressing any key to continue and getting out of 'if's
        # It will bring up this "invalid option", which should not.


main()
