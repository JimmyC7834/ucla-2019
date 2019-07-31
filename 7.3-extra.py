# Write a script that asks for an amount of change
# (as in money you get back when paying for something in cash)
# Then tells you how many of each type of coin to use to make that amount
#   Example:
#       How much change do you need?
#       83
#       3 quarters, 0 dimes, 1 nickel, 3 pennies
import math

COINVALUES = {
    'quarters':25,
    'dimes':10, 
    'nickels':5, 
    'pennies':1 
}

saved_changes = {}

def _change(changeAmount):
    print('unknown')
    change = {
        'quarters':0, #25
        'dimes':0, #10
        'nickels':0, #5
        'pennies':0 #1
    }
    for k,v in COINVALUES.items():
        changeAmount,change[k] = changeAmount%v,math.floor(changeAmount/v)
    return change

def change(changeAmount):
    if changeAmount in saved_changes.keys():
        print('known')
        return saved_changes[changeAmount]
    c = _change(int(changeAmount))
    saved_changes[changeAmount] = c
    return c

changeAmount = ''
while changeAmount != 'quit':
    changeAmount = input("How much change do you need?\n")
    if changeAmount == 'print datas':
        for i in saved_changes.items():
            print(i)
    else:
        print(change(changeAmount))

