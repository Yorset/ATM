"""
common/atm_enum.py
"""
from enum import Enum


class UserOptions(Enum):
    """
    CLASS ENUM
    """

    CHECK_BALANCE = 1
    SAVE_MONEY = 2
    WITHDRAW_MONEY = 3
    EXIT = 4
