#!/usr/bin/env python3
from account_creation import create_account
from account_login import log_into_account


def off():
    print("Bye")
    return '0'


action = ""
while action != '0':
    print("1. Create an account\n2. Log into account\n0. Exit")
    action = input()
    if action == '1':
        create_account()
    elif action == '2':
        action = log_into_account()
    elif action == '0':
        off()
