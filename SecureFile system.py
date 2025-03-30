#!/usr/bin/env python
# coding: utf-8
# # Assignment - 4

# Assignment - Create a simple, secure file system using Python, focusing on basic file operations, encryption, and hashing.
# 

# # 1.File Operations:
# create_file(filename): Creates an empty file with the specified filename,
# read_file(filename): Reads and prints the content of an existing file,
# update_file(filename, new_content): Appends new content to an existing file,
# delete_file(filename): Deletes a file from the filesystem.

# # 2.Encryption:
# generate_random_key(): Generates a random key for encryption using the Fernet class from the cryptography module,
# encrypt_file(filename, key): Encrypts a file using the provided key and saves the ciphertext to a new file,
# decrypt_file(encrypted_filename, key): Decrypts an encrypted file using the provided key and saves the plaintext to a new file.

# # 3.Hashing:
# compute_hashes(filename): Computes MD5 and SHA-1 hashes for a given file. It reads the file in chunks to avoid memory issues.
# 

# # 4.Password Management:
# hash_password(password): Hashes a password using the argon2 algorithm with a random salt. The hashed password is returned,
# verify_password(stored_hash, input_password): Verifies an input password against a stored hash. Returns True if the verification succeeds, otherwise False.
# 

# # 5.Main Program:
# The if __name__ == "__main__": block runs the main program,
# It displays a menu for user interaction, allowing them to choose various options (e.g., create, read, encrypt, hash passwords),
# The program continues until the user selects the “Exit” option.





import os
import hashlib
import base64
from cryptography.fernet import Fernet
import argon2

# File Operations
def create_file(filename):          
    with open(filename, 'w') as f:
        pass
    print(f"File '{filename}' created successfully.")

def read_file(filename):              
    if not os.path.exists(filename):
        print("Error: File not found.")
        return
    with open(filename, 'r') as f:
        content = f.read()
        print(f"File Content:\n{content}")

def update_file(filename, new_content):  
    if not os.path.exists(filename):
        print("Error: File not found.")
        return
    with open(filename, 'a') as f:
        f.write(new_content + "\n")
    print(f"Content added to '{filename}'.")

def delete_file(filename):          
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print("Error: File not found.")

# Encryption
def generate_random_key(): 
    return Fernet.generate_key()

def encrypt_file(filename, key):
    if not os.path.exists(filename):
        print("Error: File not found.")
        return
    try:
        fernet = Fernet(key)
        with open(filename, 'rb') as f:
            plaintext = f.read()
        ciphertext = fernet.encrypt(plaintext)
        with open(f"{filename}.encrypted", 'wb') as encrypted_file:
            encrypted_file.write(ciphertext)
        print(f"File '{filename}' encrypted and saved as '{filename}.encrypted'")
    except Exception as e:
        print("Encryption Error:", str(e))

def decrypt_file(encrypted_filename, key):
    if not os.path.exists(encrypted_filename):
        print("Error: Encrypted file not found.")
        return
    try:
        fernet = Fernet(key)
        with open(encrypted_filename, 'rb') as encrypted_file:
            ciphertext = encrypted_file.read()
        plaintext = fernet.decrypt(ciphertext)
        print("Decrypted content:", plaintext.decode())
    except Exception as e:
        print("Error during decryption:", str(e))

# Hashing
def compute_hashes(filename):
    if not os.path.exists(filename):
        print("Error: File not found.")
        return
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while chunk := f.read(BUF_SIZE):
            md5.update(chunk)
            sha1.update(chunk)

    print(f"MD5: {md5.hexdigest()}")
    print(f"SHA1: {sha1.hexdigest()}")

# Password Management
def hash_password(password):
    argon2_hasher = argon2.PasswordHasher()
    return argon2_hasher.hash(password)

def verify_password(stored_hash, input_password):
    argon2_hasher = argon2.PasswordHasher()
    try:
        return argon2_hasher.verify(stored_hash, input_password)
    except argon2.exceptions.VerifyMismatchError:
        return False

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. Encrypt a file")
        print("6. Decrypt a file")
        print("7. Compute hashes (MD5 and SHA-1) for a file")
        print("8. Hash a password")
        print("9. Verify a password")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)
        elif choice == "2":
            filename = input("Enter the filename to read: ")
            read_file(filename)
        elif choice == "3":
            filename = input("Enter the filename to update: ")
            new_content = input("Write the content: ")
            update_file(filename, new_content)
        elif choice == "4":
            filename = input("Enter the filename to delete: ")
            delete_file(filename)
        elif choice == "5":
            filename = input("Enter the filename: ")
            key_input = input("Enter the encryption key (leave empty to generate a new one): ")
            if key_input:
                try:
                    key = base64.urlsafe_b64encode(key_input.encode().ljust(32)[:32])
                except:
                    print("Invalid key format. Using a random key instead.")
                    key = generate_random_key()
            else:
                key = generate_random_key()
                print(f"Generated encryption key: {key.decode()} (Save this key!)")
            encrypt_file(filename, key)
        elif choice == "6":
            encrypted_filename = input("Enter the filename: ")
            key_input = input("Enter the decryption key: ")
            try:
                key = base64.urlsafe_b64encode(key_input.encode().ljust(32)[:32])
            except:
                print("Invalid key format.")
                continue
            decrypt_file(encrypted_filename, key)
        elif choice == "7":
            filename = input("Enter the filename: ")
            compute_hashes(filename)
        elif choice == "8":
            password = input("Enter the password: ")
            hashed = hash_password(password)
            print(f"Hashed Password: {hashed}")
        elif choice == "9":
            stored_hash = input("Enter the stored hash: ")
            input_password = input("Enter the password to verify: ")
            if verify_password(stored_hash, input_password):
                print("Password verification successful!")
            else:
                print("Password verification failed.")
        elif choice == "10":
            print("Exiting the program. Goodbye!")
            break
