import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for d in range(3, sqrt_n + 1, 2):
         if n % d == 0:
             return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    print("Prime" if isPrime(n) else "Not prime")

