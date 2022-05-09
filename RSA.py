
import random
from math import gcd
from math import isqrt
from functools import reduce

#a**b mod m
def FME(a,b,m): 
    a = int(a)
    b = int(b)
    m = int(m)

    # set a result
    res = 1
    while b != 0:
        if b % 2 == 1:
            b -= 1
            res = (res * a) % m
            continue
        b >>= 1
        a = (a * a) % m
    return res


#s is step, d is remaining odd value
def MR(p):

    # p-1 = 2^s*d, so that get s and ds
    f = p - 1
    s = 0
    while f % 2 == 0:
        f //= 2
        s += 1

    d = f

    # if s = 0, p is even, it means (p-1)%2 != 0, p-1 is a odd number, p is a even number
    if s == 0:
        return False

        
    if p == 2:
        return True

    
    # random generate a
    a = random.randint(0, p-1)

    # test if a**d (mod p) is 1
    if FME(a,d,p) == 1:
        return True
    else:
        # test if a**((2**i)*d) mod p is -1
        for i in range(s-1):
            if FME(a, (2**i)*d, p) == p-1:
                return True
        return False


def EEA(a,b):
    if a < b:
        r = a
        a = b
        b = r

    x1 = 1
    x2 = 0
    x3 = a

    y1 = 0
    y2 = 1
    y3 = b
    while True:      
        if y3 == 1:
            return y2 % a
        elif y3 == 0:
            return "no"  
        else:
            Q = x3 // y3
            r1 = x1 - Q * y1
            r2 = x2 - Q * y2
            r3 = x3 - Q * y3
            x1 = y1
            x2 = y2
            x3 = y3
            y1 = r1
            y2 = r2
            y3 = r3



def encrypt(m): 
    encrypt = '' 
    n, e, d =generate_key()

    # we got private key
    print(" ")
    print("private key: ")
    print("n: ",n)
    print(" ")
    print("d: ",d)
    print(" ")

    m = m.encode("utf-8")
    for i in m:
        # got i
        a = FME(i,e,n)

        # make a be a number based 16, so that could be handled as a really big number
        a = hex(a)

        # encrypt like a long string to store all values of list a
        encrypt += a
    # we got the message after encrypting
    print("encrypted message : ")
    print(encrypt)

def decrypt(c,d,n):
    decrypt = ""
    c = c.strip()

    #we use mess to put all c values together
    mess = c.split("0x")
    # got message to decrypt
    for i in mess:
        if i != "": 
            i = int(i,16)
            de_mess = FME(i,d,n)

            # transfer by ASCII
            de_mess = chr(de_mess)
            decrypt += de_mess
    
    print(" ")
    print("The decrypted message: ")
    print(decrypt)
    print(" ")
            

def chineese_remainer_for_decryption(c, a, b, d):

    dp = FME(d,1,(p-1))
    dq = FME(d,1,(q-1))
    mp = FME(c, dp, p)
    mq = FME(c, dq, q)

    mc, yp,yq = EEA(p, q)
    
    return ((mp * q * yq) + (mq * p * yp)) % (p * q)

            
            
def prime_number():
    while True:
        n = random.getrandbits(1024)   
        if n % 2 != 0 :
            if MR(n):                
                return n
            else:
                return prime_number()


def generate_key():
    p = prime_number()
    q = prime_number()

    # got n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # got e
    e = random.randint(1,phi)
    while gcd(e,phi) != 1:
        e = random.randint(1,phi)

    d = EEA(phi, e)

    return (n, e, d)



def main():

    print("what to encrypt?")
    # encrypt
    m = input()
    encrypt(m)

    # decrypt  
    print("Decrypt:")
    print(" ")
    n = input("n :")
    print(" ")
    d = input("d :")
    print(" ")
    print("Cipher : ")
    cipher = input()
    decrypt(cipher,d,n)


if __name__ == '__main__':
    main()
