import random
can = []
iin = '400000'
check_digit = '8'
accounts = {}


def generate_number(n):
    generated_number = ""
    for i in range(n):
        generated_number += str(random.randint(0, 9))
    return generated_number


def create_account():
    global can
    global accounts
    ain = generate_number(9)
    while ain in can:
        ain = generate_number(9)
    can.append(ain)
    card_number = iin + ain + check_digit
    card_pin = generate_number(4)
    balance = 0
    accounts[card_number] = {'pin': card_pin, 'balance': balance}
    print("Your card has been created")
    print(f"Your card number:\n{card_number}")
    print(f"Your card PIN:\n{card_pin}")
