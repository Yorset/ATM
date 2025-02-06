"""
common/atm_screens.py
"""
from utils import console_utils
from common import atm_enum


def home_screen() -> atm_enum.UserOptions:
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
    # Aqui rescatamos el valor ingresado por el ususario
    # y lo transformamos en un numero
    input_option = int(input("Option:"))
    # el numero lo pasamos a un indice de la enumeracion
    option = atm_enum.UserOptions(input_option)
    # retornamos la opcion
    return option


def save_money_screen():
    """
    ATM | save money screen
    """
    print("---------------------------------------")
    print("Please select the denomination of the bill you will introduce")
    print("Then, select the amount of bill you will introduce")
    print(" When done, select 'Exit'")

    bill_list = list(atm_enum.Bill)

    for index, bill, in enumerate(bill_list, start=0):
        print(f"{index + 1}. ${bill.value}")

    print("---------------------------------------")
    input_option = int(input("Option:"))

    option = bill_list[input_option - 1]
    return option
