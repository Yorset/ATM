"""
    utils/console_utils.py
"""

import os
import platform


def clean_console():
    """
    Clean the console from your OS.
    """
    host_plataform = platform.system()  # Detecta el sistema operativo

    if host_plataform == "Windows":
        os.system("cls")  # Comando para Windows
    else:
        os.system("clear")  # Comando para macOS y Linux
