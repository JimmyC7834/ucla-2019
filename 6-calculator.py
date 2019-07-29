#BEGINNING OF CALCULATOR


# 1) use if-statements to complete this calculator program with 4 operations
# Example run (what it should look like):
#       0 - add
#       1 - subract
#       2 - multiply
#       3 - divide
#   Enter a number to choose an operation:
#   1
#   Enter your first input: 10
#   Enter your second input: 4
#   10 - 4 = 6

# 2) add a fifth operation, power, that does a to the power of b
# 3) add a sixth operation, square root, that only asks for 1 input number and outputs its sqrt
# 4) seventh operation, factorial(a), one input
# 5) eighth operation, fibonacci(a), one input
# 6) talk to instructors when finished

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def power(x,y):
    return x**y

def sqrt(x,_):
    return x*(.5)

def factorial(x,_):
    ans = x
    for i in range(1 ,x-1):
        ans *= (x - i)
    return ans

def fibonacci(x,_):
    a = 0
    b = 1
    for _ in range(x - 2):
        temp = b
        b += a
        a = temp
        print(b)
    return b

OPS = {
    '0':add,
    '1':subtract,
    '2':multiply,
    '3':divide,
    '4':power,
    '5':sqrt,
    '6':factorial,
    '7':fibonacci
}

while True:
    for i,v in OPS.items():
        print(' ',i,' - ',v.__name__)
    print("Enter a number to choose an operation: \n")
    op = input()
    if int(op) in range(8):
        break
    else:
        print(" invalid input \n")

a = int(input("Enter your first input: "))
b = int(input("Enter your second input: "))

print('answer: ',OPS[op](a,b))


#END OF CALCULATOR