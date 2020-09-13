"""
Use Python to implement an encryption/decryption program for RSA using letter
by letter encryption (using ASCII code of each letter to represent it). This will be similar (in
parts) to the Elgamal implementation you have seen before.
"""

#! /usr/bin/python3

import sympy
import random

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def extendedGCD(a, b):
    x = b
    y, z = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        y, z = z - q * y, y
    if z < 0: x1 += x
    return z

def keyGen(q):
    key = random.randint(1000, q)
    while gcd(q, key) != 1:
        key = random.randint(1000, q)
    return key

def modExp(b, e, m):
    x = 1
    while e > 0:
        b, e, x = (b * b % m, e // 2, b * x % m if e % 2 else x)
    return x

def encrypt(plaintext, e, n):
    ciphertext = pow(plaintext, e) % n
    return ciphertext

def decrypt(ciphertext, d, n):
    plaintext = pow(ciphertext, d) % n
    return plaintext

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

if __name__ == '__main__':
    primeRange = sympy.primerange(200, 500)
    primeList = list(primeRange)
    rangeUpper = len(primeList) - 1
    p = primeList[random.randint(1, rangeUpper)]
    q = primeList[random.randint(1, rangeUpper)]

    # ensure that the primes are not the same
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    value = True
    if value:
        n = p * q
        print("N:", n)
        phi = (p - 1) * (q - 1)
        print("Phi:", phi)

        value1 = True
        while value1:
            e = keyGen(phi)
            if gcd(e, phi) == 1 and e < phi:
                value1 = False

        print("E:", e)

        value2 = True
        while value2:
            d = extendedGCD(e, phi)
            if d < phi:
                value2 = False

        print("D:", d)
        plaintext = "mathematics is the music of reason"
        print("Plaintext:", plaintext)
        encrypted_message = []
        for i in range(0, len(plaintext)):
            encrypted_message.append(plaintext[i])
        for i in range(0, len(encrypted_message)):
            encrypted_message[i] = encrypt(ord(encrypted_message[i]), e, n)
        print("Encrypted message:", encrypted_message)

        decrypted_message = []
        for i in range(0, len(encrypted_message)):
            decrypted_message.append(chr(int(decrypt(encrypted_message[i], d, n))))

        print("Decrypted message is:", end=" ")
        for i in range(len(decrypted_message)):
            print(decrypted_message[i], end="")

