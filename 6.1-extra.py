def factorial(n):
    return n * factorial(n-1) if n != 0 else 1 

def fib(n):
    return (fib(n-1) + fib (n-2)) if n-2 >1 else 1

def countDown(n):
    if n == 0:
        return
    print(n)
    countDown(n-1)

def countUp(n):
    if n == 0:
        return n
    countUp(n-1)
    print(n)

countUp(10)