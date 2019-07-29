''' example:
color = input("What is your favorite color?\n")
if color == "blue":
    print("Nice! Me too!")
elif color == "red":
    print("Meh. That's ok.")
else:
    print("You have terrible taste.")
'''

import wordList

name = input("what is your name? ")
print('Hi, ',name,', nice to meet you \n')
age = input("how old are you? ")
print('So you\'re ',age,' years old. \n')

while True:
    status = input(name+', how are you? ')
    status = status.replace(' ','')
    if status in wordList.goodWords:
        print('cool, see you next time')
        break
    elif status in wordList.badWords:
        print('sorry for hearing that, see you next time')
        break
    print('I don\'t understand what you are saying... \n')

