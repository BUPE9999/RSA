
def extended_eucleadian(p, q):
    """
    Extended Eucleadian Algorithm.

    :param int: 1st Number.
    :param int: 2nd Number.

    :returns: tuple [gcd(p,q), a, b] such that d = extended_eucleadian(p, q), px + qy = gcd(p,q)
    :rtype: tuple<int>
    """
    if p == 0:
        return q, 0, 1
    else:
        gcd, x, y = extended_eucleadian(q % p, p)
        return gcd, y - (q // p) * x, x


def modular_Inverse(a, b):
    """
    Generating modular inverse of given numbers (a,b)
    :param int: first number
    :param int 2nd number

    :returns: modular Inverse of two numbers
    :rtpe:int
    """
    return extended_eucleadian(a, b)[1]


def modular_exponentiation(a, b, m):
    """
    The fast modular exponentiation algorithm.

    :param int: 1st Number (base)
    :param int: 2nd Number (exponenet)
    :param int: 3rd Number (number with which mod to be taken)

    :returns: Modular Exponentiation (A^B mod C)
    :rtype: int
    """

    Y = 1
    while b > 0:
        if b % 2 == 0:
            a = (a * a) % m
            b = b//2
        else:
            Y = (a * Y) % m
            b = b - 1
    return Y


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

def miller_rabin(n, k=5):
    """
    Miller-Rabin Primality Test.

    :param int: number to be tested
    :param int: Integer k

    :returns: A return value of False means n is certainly not prime. A return value of True means n is very likely a prime
    :rtype: boolean
    """

    p = n-1
    S = 0
    while(p % 2 != 0):
        p = p//2
        S += 1

    if modular_exponentiation(k, p, n) == 1:
        return True
    else:
        for i in range(1,S):
            if n - 1 == pow(k, pow(2,i) * p):
                return True
        return False
    return False
    """
    from random import randrange
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1

    while s % 2 == 0:  # findng r such that 2^s * r + 1 for some r >= 1
        r += 1
        s //= 2
    for _ in range(k):
        x = modular_exponentiation(randrange(2, n - 1), s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            '''Keep squaring x while one of the following doesn't happen 
                (i) d does not reach n-1 
                (ii) (x^2) % n is not 1 
                (iii) (x^2) % n is not n-1'''
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    """
    """
    d = p = n-1
    S = 0
    while True:
        if p % 2 != 0:
            break
        p = p//2
        S += 1
        d = p % 2
    if modular_exponentiation(a,d,n) == 1:
        return True
    for i in range(1,S):
        ff = modular_exponentiation(a,2**i*d,n)
        if ff == n-1:
            return True
    return False
    """


def getBigRandomPrime(b):
    """
    Get Big Random Prime Number
    This method calcualte a random number of specified length and then using
    miller rabin method check if primilarity.

    :param int: Number of bits of the prime Number
    :returns: Big Prime Number
    :rtpe: int
    """
    from random import getrandbits

    while True:
        p = getrandbits(b)

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
                  241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
        if any(p % x == 0 for x in primes):
            continue
        if miller_rabin(p):
            return p


def generate_keys(b):
    """
    Generate Public and Private Keys

    :returns: Public and private Keys
    """
    p = getBigRandomPrime(b)
    q = getBigRandomPrime(b)
    e = 3
    n = p*q

    pi_n = (p-1)*(q-1)

    while not (extended_eucleadian(e, pi_n)[0] == 1):
        e = e+1

    d = modular_Inverse(e, pi_n) % pi_n
    return n, e, d


def encrypt(keys, message):
    """
    Encrypt the message.

    It will encrypt the message suing RSA algorithm.

    :param tuple<int>: public key (e,n)
    :param string: Message to be encrypted

    :returns: cipher text
    :rtype: string
    """
    e, n = keys
    result = [str(modular_exponentiation(ord(c), e, n)) for c in message]
    return " ".join(result)


def decrypt(keys, cipher):
    """
    Decrypt the message.

    It will decrypt the message suing RSA algorithm.

    :param tuple<int>: private key (d,n)
    :param string: Message to be encrypted

    :returns: Message
    :rtype: string
    """
    d, n = keys
    result = [chr(modular_exponentiation(int(c), d, n))
              for c in cipher.split(' ')]

    return ''.join(result)


def main():
    """
    Main Function of the modeule.

    """

    from cs50 import get_int, get_string

    def user_input_for_result():
        res = 0
        while True:
            res = get_int(
                "What do you want to do with this:\n1:Print on console\n2:Save to File\nChoose One: ")
            if res not in [1, 2]:
                print("Error!! Please input in Range")
            else:
                break
        return res

    def encryption():
        """
        Method responsible for taking inputs and calling encrypt fucntion.
        """
        message = get_string("Enter your message:\n")
        print("Enter Public Key")
        e = get_int("Enter e: ")
        n = int(input("Enter n: "))

        cipher = encrypt((e, n), message)
        res = user_input_for_result()
        if res == 1:
            print(cipher)
        else:
            with open("encrypted_message.txt", 'w') as file:
                file.write(cipher)

    def decryption():
        """
        Method responsible for taking inputs and calling decrypt fucntion.
        """
        cipher = input("Enter the cipher:\n")
        print("Enter Private Key")
        d = int(input("Enter d: "))
        n = int(input("Enter n: "))

        message = decrypt((d, n), cipher)
        res = user_input_for_result()
        if res == 1:
            print(message)
        else:
            with open("decrypted_message.txt", 'w') as file:
                file.write(message)

    def print_keys(n, e, d):
        """
        Method repsonsible for printing private and public keys.
        """
        res = user_input_for_result()
        if res == 1:
            print("Public Key:\n"+"n ->", str(n) + "\n e ->", str(e))
            print("Private Key:\n" + "d -> ", str(d))
        else:
            with open("public_key.txt", 'w') as file:
                file.write("n -> "+str(n)+"\n e -> "+str(e))
            with open("private_key.txt", 'w') as file:
                file.write("d -> "+str(d))

    """
    Main Part of Program
    """

    print("RSA Cryptosystem".center(50))
    inputted_value = 0
    while True:
        inputted_value = get_int(
            "1:Encrypt\n2:Decrypt\n3:GenerateKeys\nChoose one: ")
        if inputted_value not in [1, 2, 3]:
            print("Error!! Please Input in Range:")
        else:
            break

    if inputted_value == 1:
        encryption()
    elif inputted_value == 2:
        decryption()
    else:
        n, e, d = generate_keys(2048)
        print_keys(n, e, d)


###########################################################


if __name__ == '__main__':
    main()
