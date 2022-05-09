# !/usr/bin/python3
import base64

from Method import Fast_Modular_Exponentiation
from Generate_Key import generate_key


# transform to ASCII code
def m_encrypt(m): 
    m_encrypt = ''  
    n, e, d =generate_key()
    #print(f"Public Key({n},{e})")
    #print()
    print(f"Private Key({n},{d})")
    print()

    m = m.encode("utf-8")
    #
    # print(m)
    for i in m:
        #i 0-3
        #print(i)
        a = Fast_Modular_Exponentiation(i,e,n)
        a = hex(a)
        #print(a)
        m_encrypt += a
    print("The encrypted message >>")
    print(m_encrypt)

        
    
def c_decrypt(c,d,n):
    c_decrypt = ""
    c = c.strip()

    mess = c.split("0x")
    #print(mess)
    for i in mess:
        if i != "": 
            i = int(i,16)
            de_mess = Fast_Modular_Exponentiation(i,d,n)
            de_mess = chr(de_mess)
            c_decrypt += de_mess
    print("The decrypted message >>")
    print(c_decrypt)
