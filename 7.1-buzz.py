# Write a program that prints all the numbers from 1 to 100
# Except, when it gets to a multiple if 3, it prints "fizz" instead of the number
# and when it gets to a multiple of 5, it prints "buzz" instead of the number
# If something is a multiple of both 3 and 5, print "fizz buzz"

# Example (from 1 to 20)
"""
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz buzz
16
17
fizz
19
buzz
"""

# modify this loop
for i in range(1,20):
    m = ''
    m = m + 'fizz ' if i%3 == 0 else m
    m = m + 'buzz' if i%5 == 0 else m
    m = i if m == '' else m
    print(m)
