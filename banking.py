#!/usr/bin/env python3

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
