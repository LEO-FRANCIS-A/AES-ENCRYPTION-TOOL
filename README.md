# AES-ENCRYPTION-TOOL

 *COMPANY*: CODTECH IT SOLUTIONS

 *NAME*: LEO FRANCIS A

 *INTERN ID*: CT04DM1437 

 *DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

 *DURATION*: 4 WEEKS

 *MENTOR*: NEELA SANTOSH


AES ENCRYPTION TOOL

This is a Python command-line tool that lets users securely encrypt and decrypt files using the AES encryption algorithm with 256-bit keys in CBC mode. The purpose of this tool is to protect sensitive information by converting it into an unreadable format that can only be reversed with the correct password.

Features

    AES 256 encryption for strong file protection

    Password-based key generation using SHA 256

    PKCS7 padding to handle any file size

    Password input is hidden for security

    Works with any type of file, including text, images, and binary files

    Encrypted files are saved with a dot enc extension

    Decrypted files are saved with a dot dec extension

Tools and Libraries Used

    Python3 was used to write the script

    Ubuntu command line was used to run and test the tool

    Sublime Text was used as the code editor

    The cryptography library was used for AES cipher operations and padding

    The hashlib module was used to create a secure key from the password

    The os module was used to generate a random 16 byte initialization vector

    The getpass module was used to securely enter the password without showing it on the screen

    The xxd tool was used to view the encrypted binary file in a readable format without corrupting the terminal

How It Works

Encryption Process
   
    The user selects a file and provides a password.

    The password is converted into a 256 bit key using SHA 256 hashing.

    A random 16 byte initialization vector is generated.
   
    The file is read and padded using PKCS7 to match the AES block size.

    The data is encrypted using AES in CBC mode.

    The output file includes the IV followed by the encrypted content and is saved with a dot enc extension.

Decryption Process
 
    The user provides the encrypted file and the same password used during encryption.

    The initialization vector is extracted from the first 16 bytes of the file.

    The remaining encrypted data is decrypted using the AES key.

    Padding is removed to restore the original content.

    The decrypted data is saved in a new file with a dot dec extension.

Usage Example

    $ python3 encrypt.py
    AES File Encryption Tool
    1. Encrypt a file
    2. Decrypt a file
    Enter your choice (1 or 2): 1
    Enter the path to the file: secret.txt
    Enter the password:
    Encryption completed. File saved as: secret.txt.enc

The tool will perform the action and save the result as either a dot enc or dot dec file.
To view the encrypted content safely, use the xxd command instead of cat.


Platform Used

    This tool was developed using Ubuntu command line for execution and Sublime Text for coding and editing.
    It is compatible with any platform that supports Python3.

Output Screenshots:

Encryption

![Image](https://github.com/user-attachments/assets/907091b3-cb42-4dc2-984b-122a569780b7)

Encrypted Data

![Image](https://github.com/user-attachments/assets/531df4ec-80a2-4756-89f0-b72fbc5bfe07)

Decryption

![Image](https://github.com/user-attachments/assets/9a5795d7-717b-4fbc-aa89-39e8e40fc5fc)

Decrypted Data

![Image](https://github.com/user-attachments/assets/d6876149-dc0d-414d-a946-c3b25a725f6f)
