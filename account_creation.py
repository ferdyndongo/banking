import random
import sqlite3

iin = '400000'


def generate_number(n):
    generated_number = ""
    for i in range(n):
        generated_number += str(random.randint(0, 9))
    return generated_number


def last_digit(digits):
    """Return the last digit given by the luhn algorithm from a sequence of 15 digits."""

    digits = [int(d) for d in digits]
    for i in range(len(digits)):
        if (i + 1) % 2 != 0:
            digits[i] *= 2
    digits = [d - 9 if d > 9 else d for d in digits]
    for digit in range(0, 10):
        if (sum(digits) + digit) % 10 == 0:
            return str(digit)


def create_account():

    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS card;")
    cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
    ain = generate_number(9)
    while ain in [str(pk[0]) for pk in cur.execute("select id from card;")]:
        ain = generate_number(9)

    card_number = iin + ain + last_digit(iin + ain)
    card_pin = generate_number(4)
    card_balance = 0
    cur.execute("INSERT INTO card(id, number, pin, balance) VALUES(?, ?, ?, ?)", (ain, card_number, card_pin, card_balance))
    conn.commit()
    conn.close()
    print("\nYour card has been created")
    print(f"Your card number:\n{card_number}")
    print(f"Your card PIN:\n{card_pin}")

