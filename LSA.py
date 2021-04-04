from math import gcd as gcd
from functools import reduce
from random import getrandbits, sample, seed, shuffle, choice
from time import time
from LSA_analyzer import *

# Encrypted characters
chars = r' .abcdefghijklmnopqrstuvwxyz0123456789?,:@/\#$ABCDEFGHIJKLMNOPQRSTUVWXYZ>!<";%^&*()-+*\~' + "'" + chr(9) + chr(10) + chr(13)
alice_key = getrandbits(3072)   # Main Key (Alice's version)
bob_key = alice_key             # Main Key (Bob's version)
key_save = alice_key

# Maximum cipher key: 12,287
# Minimum cipher key: 800. Values >= 800 have more than 222 coprimes
LARGEST = 0x2FFF
SMALLEST = 0x320


# Given cipher key, and running product 'c', find congruency generator 'z'
def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    GCD, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return GCD, x, y

# Generate cipher text for a character


def sender(k, character):
    global alice_key

    c = 1
    num = 0
    order = chars.index(character)
    i = (alice_key & 0x5F) | 3  # 3 > i > 111
    l = []
    while num <= order:
        if gcd(i, k) == 1:
            l.append(i)
            c = c * i % k
            num += 1
        i += 1
    _, z, _ = gcdExtended(c, k)

    c = 1
    sigma = 0
    for i in range(len(l)):
        c = c * l[i] % k
        if c * z % k == 1:
            sigma += 1
    return z, sigma

# Generate k from Main Key for each character
# Change key for each character
# Generate cipher text 'z' and 'sigma' for all characters


def encrypt(text):
    global alice_key
    global LARGEST
    global SMALLEST
    global key_save

    encryption = []
    for i in range(len(text)):
        k = (alice_key & LARGEST) | SMALLEST       # Make sure k is within acceptable range
        encryption.append(sender(k, text[i]))
        alice_key = alice_key >> 1
        if alice_key < LARGEST:
            alice_key = key_save
    return encryption

# Decipher one character


def decipher(k, z_sig):
    global chars
    global bob_key

    m = 1
    i = (bob_key & 0x5F) | 3
    check = 0
    index = 0
    z, sigma = z_sig
    while True:
        if gcd(i, k) == 1:
            m = m * i % k
            check = m * z % k
            if check == 1:
                sigma -= 1
                if sigma == 0:
                    return chars[index]
            index += 1
        i += 1
        if (k % 2 == 0) and (i % 2 == 0):
            i += 1

# Generate k from Main Key for each character
# Change key for each character
# Decipher text from 'z' and 'sigma' for each characters


def decode(encryption):
    global bob_key
    global LARGEST
    global SMALLEST
    global key_save

    text = ''
    for i in encryption:
        k = (bob_key & LARGEST) | SMALLEST        # Make sure k is within acceptable range
        text += decipher(k, i)
        bob_key = bob_key >> 1
        if bob_key < LARGEST:
            bob_key = key_save
    return text


if __name__ == '__main__':
    print()
    string = input("Enter your message for encryption: ")
    t0 = time()
    enc = encrypt(string)
    t1 = time()
    dec = decode(enc)
    t2 = time()
    print()
    print("Encryption of your message took: {} milliseconds".format(round((t1 - t0) * 1e3, 4)))
    print()
    print("Decryption of your message took: {} milliseconds".format(round((t2 - t1) * 1e3, 4)))
    print("Time per character: {} microseconds".format(round((t2 - t1) * 1e6 / len(string), 4)))
    print()
    print("Decrypted message is: \n{}".format(dec))
