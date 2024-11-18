import os
import pyfiglet
import getpass 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
text = pyfiglet.figlet_format("ZWN _ CRAWL")
print(text)

def encrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        data = f.read()

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)

    padder = padding.PKCS7(128).padder()
    data = padder.update(data) + padder.finalize()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(iv)
        f.write(encrypted_data)

def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_data) + unpadder.finalize()

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

def main():
    while True:
        print("Select operation:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Quit")

        choice = input("Enter choice: ")

        if choice == '1':
            input_file = input("Enter the location of the file to encrypt: ")
            output_file = input("Enter the location where you want to save the encrypted file: ")
            password = getpass.getpass("Enter the encryption key: ")
            encrypt_file(input_file, output_file, password.encode())
            print('File encrypted successfully.')
        elif choice == '2':
            input_file = input("Enter the location of the encrypted file: ")
            output_file = input("Enter the location where you want to save the decrypted file: ")
            password = getpass.getpass("Enter the decryption key: ")
            decrypt_file(input_file, output_file, password.encode())
            print('File decrypted successfully.')
        elif choice.lower() == '3':
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
