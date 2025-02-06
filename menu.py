# File for main menu (Options)

# Is this actually needed or can we deleted since
# you already have this menu much better under common?? -> @yigs <-

def main_menu():
    print("Welcome!")
    print("Please select an option:")
    print("1. Check Balance.")
    print("2. Save Money.")
    print("3. Withdraw Money.")
    print("4. Exit.")
    return int(input())


print(main_menu())
