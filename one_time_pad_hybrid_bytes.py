from random import getrandbits
from time import time
from PIL import Image
import io

alice_key = getrandbits(3072)  # Main Key (Alice's version)
bob_key = alice_key  # Main Key (Bob's version)
key_save = alice_key

MINIMUM = 0x1000


# Generate k from Main Key for each character
# Change key for each character
# Generate cipher text 'z' and 'sigma' for all characters
def encrypt(path):
    global alice_key
    global MINIMUM
    global key_save

    with open(path, "rb") as image:
        f = image.read()
        msg = bytearray(f)

    encryption = []
    for c in msg:
        encryption.append(sender(c))
        alice_key = alice_key >> 1
        if alice_key < MINIMUM:
            alice_key = key_save
    return encryption


# Generate cipher text for a character
def sender(byte):
    global alice_key
    i = (alice_key & 0xFFF) | 3  # 3 > i > 111
    cipher = i + byte
    cipher = cipher ^ i
    return cipher


# Generate k from Main Key for each character
# Change key for each character
# Decipher text from 'z' and 'sigma' for each characters
def decode(encryption):
    global bob_key
    global MINIMUM
    global key_save

    Bytes = []
    for i in encryption:
        Bytes.append(decipher(i))
        bob_key = bob_key >> 1
        if bob_key < MINIMUM:
            bob_key = key_save
    d = bytearray(Bytes)
    image = Image.open(io.BytesIO(d))
    image.save(r'C:\Programming\Python\test.PNG')
    return


# Decipher one character
def decipher(cipher):
    global bob_key

    i = (bob_key & 0xFFF) | 3
    cipher = cipher ^ i
    return cipher - i


#path = r"C:\Programming\Python\encryption\pic.jpg"
# with open(path, "rb") as image:
#   f = image.read()
#   b = bytearray(f)
#   t = time()
#e = encrypt(path)
#   t1 = time()
#d = decode(e)
#   t2 = time()
#
# image = Image.open(io.BytesIO(d))
# image.save(r'C:\Programming\Python\test.PNG')
#
# print('\nTotal number of characters: {:,}\n'.format(len(b)))
# print(f'Encryption Speed: \t{round( len(b)/(t1 - t)/1000, 3 )}\tK\t\tBytes/s')
# print(f'\t\t\t\t\t{round( (t1 - t)/len(b)*1e6, 2 )}\t\t\tμs/Byte')
# print(f'\t\t\t\t\t{round( (t1 - t), 4 )}\t\t\ts')
# print()
# print(f'Decryption Speed: \t{round( len(b)/(t2 - t1)/1000, 3 )}\tK\t\tBytes/s')
# print(f'\t\t\t\t\t{round( (t2 - t1)/len(b)*1e6, 2 )}\t\t\tμs/Byte')
# print(f'\t\t\t\t\t{round( (t2 - t1), 4 )}\t\t\ts')
# print()
# print(f'Total: \t\t\t\t{round( (t2 - t), 4 )}\t\t\ts')




