# !/usr/bin/python3
# --coding:utf-8--

import random
from math import isqrt
from functools import reduce

def Extended_Euclidean_Algorithm(a,b):
    if a < b:
        r = a
        a = b
        b = r
    x1, x2, x3 = 1, 0, a
    y1, y2, y3 = 0, 1, b
    while True:
        if y3 == 0:
            return "None"        
        elif y3 == 1:
            return y2 % a
        else:
            Q = x3 // y3
            r1, r2, r3 = x1 - Q * y1, x2 - Q * y2, x3 - Q * y3
            x1, x2, x3 = y1, y2, y3
            y1, y2, y3 = r1, r2, r3


#a**b mod m
def Fast_Modular_Exponentiation(a,b,m): 
    a = int(a)
    b = int(b)
    m = int(m)
    result = 1
    while b != 0:
        if b % 2 != 0:
            b -= 1
            result = (result * a) % m
            continue
        b >>= 1
        a = (a * a) % m
    return result


#s is step, d is remaining odd value
def Miller_Rabin_Test(p):
    # find s and d
    if p == 2:
        return True
    
    fn = p - 1
    s = 0
    while fn % 2 == 0:
        fn //= 2
        s += 1
    d = fn

    # s = 0 -> p is even
    if s == 0:
        return False

    
    # random generate a
    a = random.randint(0, p-1)

    # a**d test if a**d (mod p) is 1
    if Fast_Modular_Exponentiation(a,d,p) == 1:
        return True
    else:
        # a**((2**i)*d) test
        for i in range(s):
            if Fast_Modular_Exponentiation(a, (2**i)*d, p) == p-1:
                return True
        return False


def chineese_remainer_for_decryption(c, a, b, d):
    """
    Chineese Remainder Theorem for RSA Decryption.

    :param int: cipher
    :param int: 1st Prime
    :param int: 2nd Prime
    :param int: decryption key

    :returns: m  =  decrypted message
    :rtype: int
    """
    dp = d % (p-1)
    dq = d % (q-1)
    mp = modular_exponentiation(c, dp, p)
    mq = modular_exponentiation(c, dq, q)

    _, yp,yq = extended_eucleadian(p, q)

    return ((mp * q * yq) + (mq * p * yp)) % (p * q)

if __name__ =='__main__':
    result = "1"
    for i in range(511):
        a = random.choice("01")
        result += a
    print(result)
    result = int(result,2)
    print(result)