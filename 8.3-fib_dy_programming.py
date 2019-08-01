fib_dic = {}

def fib(n):
    a,b,keya,keyb = 0,0,str(n-1),str(n-2)
    if n-2 > 1:
        if keya in fib_dic.keys():
            a = fib_dic[keya]
        else:
            a  = fib(n-1)
            fib_dic[keya] = a
        if keyb in fib_dic.keys():
            b = fib_dic[keyb]
        else:
            b = fib(n-2)
            fib_dic[keyb] = b
        return a + b
    else:
        return 1

def fibonacci(x):
    a = 0
    b = 1
    for _ in range(x - 2):
        temp = b
        b += a
        a = temp
    return b

for _ in range(1000):
    fib(100)