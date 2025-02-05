"""
common/atm_enum.py
"""
from enum import Enum


class UserOptions(Enum):
    """
    CLASS ENUM
    """

    # Recordar que las enumeraciones en python funcionan en base a una tupla
    # y estos valores seran inmutables durante la ejecucion
    # y para acceder a los indices revisar la leccion de las tuplas
    # Spoiler: usar parentesis -> atm_enum.UserOptions(int)

    CHECK_BALANCE = 1
    SAVE_MONEY = 2
    WITHDRAW_MONEY = 3
    EXIT = 4


class Bill(Enum):
    """
    CLASS ENUM
    """

    HUNDRED = 100
    FIFTY = 50
    TWENTY = 20
    TEN = 10
    FIVE = 5
    ONE = 1
