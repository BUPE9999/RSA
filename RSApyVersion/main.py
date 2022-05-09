
# !/usr/bin/python3

from Encrypt import m_encrypt
from Encrypt import c_decrypt

# message < 16
if __name__ =='__main__':
    print("what do you need?")
    print("A.Encrypt            B.Decrypt           C.Quit")
    s = input("Please make a choice from A,B,C:")
    # encrypt
    if s == "A" or s == "a":
        print("Type the message >>>")
        m = input()
        m_encrypt(m)
    # decrypt  
    elif s == "B" or s == "b":
        print("Please enter your private key!")
        n = input("n :")
        d = input("d :")
        print("Type the message >>>")
        m = input()
        c_decrypt(m,d,n)
    #do nothing
    elif s == "C" or s == "c":
        quit()


