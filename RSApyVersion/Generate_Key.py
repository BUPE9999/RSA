# !/usr/bin/python3
# --coding:utf-8--

import random
from math import gcd
from Method import Extended_Euclidean_Algorithm
from Method import Miller_Rabin_Test


def generate_prime_number():
    while True:
        n = random.getrandbits(516)   
        if n % 2 != 0 :
            #print(n)
            if Miller_Rabin_Test(n):                
                return n
            else:
                return generate_prime_number()
            



def generate_E(fn):
    e = random.randint(1,fn)
    while gcd(e,fn) != 1:
        e = random.randint(1,fn)
    return e
    

def generate_key():
    p = generate_prime_number()
    q = generate_prime_number()
    #p = 463
    #q = 547

    n = p * q
    fn = (p - 1) * (q - 1)

    #e = 65535
    e = generate_E(fn)
    d = Extended_Euclidean_Algorithm(fn, e)

    return (n, e, d)






