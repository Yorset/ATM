# File for main menu (Options)

def main_menu():
    print("Welcome!")
    print("Please select an option:")
    print("1. Check Balance.")
    print("2. Save Money.")
    print("3. Withdraw Money.")
    print("4. Exit.")
    return int(input())


print(main_menu())
