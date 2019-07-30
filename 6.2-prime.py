#BEGINNING OF PRIME.PY
#work on this when you are done with other work
#
#implement this function, isPrime(n)
#which should return True if n is prime
#and False otherwise
#examples:
#   isPrime(1) returns False
#   isPrime(5) returns True
#   isPrime(28) returns False
#

import math

def isPrime(n):
    for i in range(2,math.floor(n**.5) + 1):
        if n % i == 0:
            return False
    return True



#implement generatePrimes(n)
#which should return a list containing all the primes up to n
#Examples:
#   generatePrimes(1) should return []
#   generatePrimes(5) should return [2,3,5]
#   generatePrimes(20) should return [2,3,5,7,11,13,17,19]

def generatePrimes(n):
    arr = []
    for i in range(2,n + 1):
        if isPrime(i):
            arr.append(i)
    return arr

def _generatePrimes(n):
    arr = list(range(2,n+1))
    for e in arr:
        if e != 0:
            for i in range(e *2,n+1,e):
                arr[i -2] = 0
    return arr


_generatePrimes(1000000)

#bad
#num  |10    |100   |1000  |10000 |100000|1000000
#time |0.496 |0.655 |0.419 |0.524 |1.992 |38.813

#good
#num  |10    |100   |1000  |10000 |100000|1000000
#time |0.219 |0.527 |0.507 |0.602 |0.645 |2.305

#END OF PRIME.PY