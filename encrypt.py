import os
import hashlib
from getpass import getpass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def derive_key(password):
    return hashlib.sha256(password.encode()).digest()

def encryption(text, password):
    try:
        key = derive_key(password)
        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(text, 'rb') as f:
            data = f.read()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        encrypted = encryptor.update(padded_data) + encryptor.finalize()

        with open(text + ".enc", 'wb') as f:
            f.write(iv + encrypted)

        print(f"File encrypted successfully!\n--> Saved as: {text}.enc")

    except FileNotFoundError:
        print("--> Error: File not found.")

def decryption(text, password):
    try:
        key = derive_key(password)

        with open(text, 'rb') as f:
            iv = f.read(16)
            encrypted_data = f.read()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

        output_file = text.replace(".enc", ".dec")

        with open(output_file, 'wb') as f:
            f.write(decrypted)

        print(f"File decrypted successfully!\n--> Saved as: {output_file}")

    except FileNotFoundError:
        print("--> Error: File not found.")
    except ValueError:
        print("--> Decryption failed. Wrong password or corrupted file.")

print("\nAES ENCRYPTION TOOL ")
print("1. Encryption")
print("2. Decryption")

choice = input("Select a method(1 or 2): ").strip()
text = input("Enter the file path: ").strip()
password = getpass("Enter your password: ")

if choice == '1':
    encryption(text, password)
elif choice == '2':
    decryption(text, password)
else:
    print("Invalid Choice. Please select 1 or 2")
