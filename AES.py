# I found this script on the internet, and modified it to show time analysis of the AES
import pyaes, pbkdf2, binascii, os, secrets
from time import time

password = "password"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)

iv = secrets.randbits(256)


text = "Hello"*2000  # Total of 10,000 characters
t = time()
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(text)

t1 = time()
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
t2 = time()

# Time analysis
print('\nTotal number of characters: {:,}\n'.format(len(text)))
print(f'\t\t\t\t\t{round( (t2 - t1), 4 )}\t\t\tsTotal Time')
print(f'Encryption Speed: \t{round( len(text)/(t1 - t), 3 )}\tK\t\tcharacters/s')
print(f'\t\t\t\t\t{round( (t1 - t)/len(text)*1e6, 2 )}\t\t\tμs/character')
print(f'\t\t\t\t\t{round( (t1 - t), 4 )}\t\t\ts')
print()
print(f'Decryption Speed: \t{ round(len(text)/(t2 - t1), 3) }\tK\t\tcharacters/s')
print(f'\t\t\t\t\t{round( (t2 - t1)/len(text)*1e6, 2 )}\t\t\tμs/character')
print()
print(f'Total: \t\t\t\t{round( (t2 - t), 4 )}\t\t\ts')







