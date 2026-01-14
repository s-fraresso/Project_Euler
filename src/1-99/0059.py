from itertools import product
from string import ascii_letters


def decrypt(encrypted_message, key):
    decrypted_message = []
    for i in range(len(encrypted_message)):
        decrypted_message.append(encrypted_message[i] ^ (key[i % 3]))
    return decrypted_message


def encode(message):
    return ''.join(chr(c) for c in message)


with open('input_files\\0059_cipher.txt', 'r') as f:
    encrypted_message = [int(c) for c in f.readline().split(',')]

valid_characters = ascii_letters + ',.?! ;0123456789()\\{\\}/\\+-*=_[]\\"\':'

for key in product(range(ord('a'), ord('z') + 1), repeat=3):
    decrypted_message = decrypt(encrypted_message, key)
    encoded_message = encode(decrypted_message)
    if all(c in valid_characters for c in encoded_message):
        print(encoded_message)
        print(sum(decrypted_message))