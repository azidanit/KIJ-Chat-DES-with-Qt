import math
import random

def generate_prime(n):
    while True:
        r = random.randint(2 ** (n - 1), 2 ** n)
        # DeBouvelles prime theory
        r = math.ceil(r / 6)
        p = 6 * r - 1
        if isPrime(p):
            return p
        p = 6 * r + 1
        if isPrime(p):
            return p

# Python3 program Miller-Rabin primality test
# Source : https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
# modular exponentiation (x^y) % p
def power(x, y, p):
    res = 1;

    x = x % p;
    while (y > 0):

        if (y & 1):
            res = (res * x) % p;

        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;


def millerTest(d, n):
    a = 2 + random.randint(1, n - 4);
    x = power(a, d, n);

    if (x == 1 or x == n - 1):
        return True;

    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    # Return composite
    return False;


# k is an input parameter that determines accuracy level.
# Higher value of k indicates more accuracy.
def isPrime(n, k=10):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

    for i in range(k):
        if (millerTest(d, n) == False):
            return False;

    return True;
