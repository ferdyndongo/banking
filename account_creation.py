import random
can = []
iin = '400000'
accounts = {}


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
    global can
    global accounts
    ain = generate_number(9)
    while ain in can:
        ain = generate_number(9)
    can.append(ain)
    card_number = iin + ain + last_digit(iin + ain)
    card_pin = generate_number(4)
    balance = 0
    accounts[card_number] = {'pin': card_pin, 'balance': balance}
    print("Your card has been created")
    print(f"Your card number:\n{card_number}")
    print(f"Your card PIN:\n{card_pin}")
