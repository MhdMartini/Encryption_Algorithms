This code is an implementation of the LSA Encryption Algorithm. The challenge in this project was to create a nencryption algorithm which acheives the best balance between security and speed. 

A mathematician friend of mine invented the LSA encryption algorithm and asked me to implement it with python, and maybe develop a phone app down the road. 

The LSA depends on Gauss's Generalization of Wilson's Theorem; the encryption algorithm and the coding algorithm are explained in detail in a separate file. 

***THE LSA ALGORYTHM IS PATENTED, PLEASE DO NOT USE IT FOR COMMERCIAL PURPOSES***

Procedure:
- To establish a secure connection, a master key (K) must be shared between the communicating parties; this key could be generated with     the RSA, Diffie-Hellman, or privately shared. 

- After the master key is shared between the parties, the master key will be used to generate a number (N) for each encrypted character.

- Encryption relied on Gauss's Generalization of Wilson's Theorem and Group Theory. For any number N, let the coprimes of N be the "group"    of N, or ( G(N) ). Also, let the product of all group elements be "Φ". The Theorem states that if N is prime or if N is in the form of "p^t" or        "2p^t" (where p is a prime number, and t is any positive intiger,) then Φ % N = -1. Otherwise, if N is not in the mantioned form, then    Φ % N = 1.

- Simple Example: Encrypting the letter "B":
  - the master key generates a number (let it be 10 for simplicity). Thus:
    G(N) = {1, 3, 7, 9}. 
  - let the character "B" have an order of 2 (A, B, C). Alice then sends (1*3 % N) to Bob. let the cipher text be denoted "c" 
  - To decrypt the message, Bob multiplies "c" by the group elements backwards, and perform the modulus operation for each step. When       Bob finds congruency to -1 or 1 (depending on N,) Bob knows the character order, and hence the character. 
  - Thus, Bob does the following upon receiving  (1*3 % N = 3):
    - 3 * 9 % 10 ?= -1:       No
    - 3 * 9 * 7 % 10 ?= -1:   Yes! Therefore, cipher text means "B"
  - Note, some details differ in the actual implementation in order to maximize the speed of the algorithm without compromising its         security.
