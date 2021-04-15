from account_creation import last_digit
from account_operation import get_balance, add_income, do_transfer, close_account
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


def check_card(card_number):
    """Check the validity of a credit card."""

    if last_digit(card_number[:-1]) != card_number[-1]:
        print("Probably you made a mistake in the card number. Please try again!")
        return False
    elif card_number not in [n[0] for n in cur.execute("select number from card;")]:
        print("Such a card does not exist.")
        return False
    else:
        return True


def log_into_account():

    print("\nEnter your card number:")
    card_number = input()
    print("Enter your PIN:")
    card_pin = input()
    if check_card(card_number):
        if card_pin != [p[0] for p in cur.execute("select pin from card where number = ?", (card_number,))][0]:
            print("\nWrong card number or PIN!")
        else:
            print("\nYou have successfully logged in!")
            to_do = ""
            while to_do != '5':
                print("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                to_do = input()
                if to_do == '1':
                    get_balance(card_number)
                elif to_do == '2':
                    add_income(card_number)
                elif to_do == '3':
                    print("\nTransfer")
                    print("Enter card number:")
                    card_to = input()
                    if check_card(card_to):
                        do_transfer(card_number, card_to)
                elif to_do == '4':
                    close_account(card_number)
                    break
                elif to_do == '5':
                    print("\nYou have successfully logged out!")
                elif to_do == '0':
                    print("Bye!")
                    conn.close()
                    return '0'
