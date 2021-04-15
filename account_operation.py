import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


def get_balance(card_number):
    card_balance = [balance[0] for balance in cur.execute("select balance from card where number = ?", (card_number,))][0]
    print(f"\nBalance: {card_balance}")
    return card_balance


def add_income(card_number):
    print("Enter income:")
    income = int(input())
    card_balance = [balance[0] for balance in cur.execute("select balance from card where number = ?", (card_number,))][0]
    card_balance += income
    cur.execute("update card set balance = ? where number = ?", (card_balance, card_number))
    conn.commit()
    print("Income was added!")


def do_transfer(card_from, card_to):
    if card_from == card_to:
        print("You can't transfer money to the same account!")
    else:
        print("Enter how much money you want to transfer:")
        money = int(input())
        balance_from = [balance[0] for balance in cur.execute("select balance from card where number = ?", (card_from,))][0]
        if money > balance_from:
            print("Not enough money!")
        else:
            balance_from -= money
            cur.execute("update card set balance = ? where number = ?", (balance_from, card_from))
            conn.commit()
            balance_to = [balance[0] for balance in cur.execute("select balance from card where number = ?", (card_to,))][0]
            balance_to += money
            cur.execute("update card set balance = ? where number = ?", (balance_to, card_to))
            conn.commit()
            print("Success!")


def close_account(card_number):
    cur.execute("delete from card where number = ?", (card_number,))
    conn.commit()
    print("\nThe account has been closed!")
    conn.close()
