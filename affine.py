import string
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("'a' must be coprime with 26 for a valid affine cipher.")
    
    alphabet = string.ascii_uppercase
    ciphertext = ""
    
    for char in plaintext.upper():
        if char in alphabet:
            p = alphabet.index(char)
            c = (a * p + b) % 26
            ciphertext += alphabet[c]
        else:
            ciphertext += char  # Preserve spaces and non-alphabet characters
    
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("'a' must be coprime with 26 for a valid affine cipher.")
    
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("No modular inverse found for 'a'.")
    
    alphabet = string.ascii_uppercase
    plaintext = ""
    
    for char in ciphertext.upper():
        if char in alphabet:
            c = alphabet.index(char)
            p = (a_inv * (c - b)) % 26
            plaintext += alphabet[p]
        else:
            plaintext += char  # Preserve spaces and non-alphabet characters
    
    return plaintext

def main():
    try:
        a = int(input("Enter key 'a' (must be coprime with 26): "))
        b = int(input("Enter key 'b': "))
        
        if gcd(a, 26) != 1:
            print("Invalid 'a'. It must be coprime with 26.")
            return
        
        valid_inputs = ["encrypt", "decrypt"]

        while True:
            user_input = input("Enter 'encrypt' or 'decrypt': ").strip().lower()
            
            if user_input in valid_inputs:
                break  # Exit loop if input is valid
            else:
                print("Invalid input. Please try again.")

        if user_input == "encrypt":
            plaintext = input("Enter the message to encrypt: ")
            encrypted_message = affine_encrypt(plaintext, a, b)
            print("Encrypted message:", encrypted_message)
        else:
            ciphertext = input("Enter the message to decrypt: ")
            decrypted_message = affine_decrypt(ciphertext, a, b)
            print("Decrypted message:", decrypted_message)
    except ValueError:
        print("Invalid input. Please enter integers for 'a' and 'b'.")

if __name__ == "__main__":
    main()
