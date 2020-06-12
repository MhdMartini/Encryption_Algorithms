from one_time_pad_hybrid_bytes import *

alice_key = getrandbits(3072)  # Main Key (Alice's version)
bob_key = alice_key  # Main Key (Bob's version)
key_save = alice_key

MINIMUM = 0x1000


# Generate k from Main Key for each character
# Change key for each character
# Generate cipher text 'z' and 'sigma' for all characters
def encrypt(msg):
    global alice_key
    global MINIMUM
    global key_save

    encryption = []
    for c in msg:
        encryption.append(sender(c))
        alice_key = alice_key >> 3
        if alice_key < MINIMUM:
            alice_key = key_save
    return encryption


# Generate cipher text for a character
def sender(character):
    global alice_key
    i = (alice_key & 0xFFF) # 0 > i > 0xFFF
    cipher = i + ord(character)
    cipher = cipher ^ i
    return cipher


# Generate k from Main Key for each character
# Change key for each character
# Decipher text from 'z' and 'sigma' for each characters
def decode(encryption):
    global bob_key
    global MINIMUM
    global key_save

    text = ''
    for i in encryption:
        text += decipher(i)
        bob_key = bob_key >> 3
        if bob_key < MINIMUM:
            bob_key = key_save
    return text


# Decipher one character
def decipher(cipher):
    global bob_key

    i = (bob_key & 0xFFF)
    cipher = cipher ^ i
    return chr(cipher - i)


# path = r"C:\Programming\Python\encryption\pic.jpg"
# with open(path, "rb") as image:
#   f = image.read()
#   b = bytearray(f)
#   t = time()
#   e = encrypt(b)
#   t1 = time()
#   d = decode(e)
#   t2 = time()

# image = Image.open(io.BytesIO(d))
# image.save(r'C:\Programming\Python\test.PNG')

#text = '\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan\nHello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn\'t save it. The second time, the Neocities editor crashed. Now I\'m writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won\'t get lost somehow. Anyways, let\'s talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There\'s a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It\'s pretty annoying. There\'s also a Teen Titans Go episode about Pig Latin. Don\'t know what Pig Latin is? It\'s a language where you take all the consonan'
text = '1'*10000
t = time()
e = encrypt(text)
t1 = time()
d = decode(e)
t2 = time()

print('\nTotal number of characters: {:,}\n'.format(len(text)))
print(f'Encryption Speed: \t{round(len(text) / (t1 - t) / 1000, 3)} K         characters/s')
print(f'\t\t\t\t\t{round((t1 - t) / len(text) * 1e6, 2)}                μs/character')
print(f'\t\t\t\t\t{round((t1 - t), 4)}              s')
print()
print(f'Decryption Speed: \t{round(len(text) / (t2 - t1) / 1000, 3)} K        characters/s')
print(f'\t\t\t\t\t{round((t2 - t1) / len(text) * 1e6, 2)}               μs/character')
print(f'\t\t\t\t\t{round((t2 - t1), 4)}             s')
print()
print(f'Total:\t\t\t\t{round((t2 - t), 4)}              s')





print(len(set(e)))






