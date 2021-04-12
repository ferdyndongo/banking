from account_creation import accounts


def log_into_account():
    print("\nEnter your card number:")
    card_number = input()
    print("Enter your PIN:")
    pin = input()
    if card_number not in accounts or pin != accounts[card_number]['pin']:
        print("\nWrong card number or PIN!")
    else:
        print("\nYou have successfully logged in!")
        to_do = ""
        while to_do != '2':
            print("1. Balance\n2. Log out\n0. Exit")
            to_do = input()
            if to_do == '1':
                print(f"Balance: {accounts[card_number]['balance']}")
            elif to_do == '2':
                print("\nYou have successfully logged out!")
            elif to_do == '0':
                return '0'
