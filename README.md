# ENCYDERCY

This Python project provides a command-line interface to encrypt and decrypt text files using AES encryption. It utilizes the `cryptography` library for encryption and decryption operations.

## Features

- Encrypt text files securely using AES encryption.
- Decrypt previously encrypted text files with the correct key.
- Passwords are securely hashed using PBKDF2 with SHA-256 for key derivation.
- Encryption utilizes AES in Cipher Feedback (CFB) mode for added security.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd ENCYDERCY
    ```

3. Install the required dependencies:


## Usage

To use the file encryption and decryption tool, follow these steps:

1. navigate to the tool folder and find the file encrypt.py :
    ```bash
    cd <folderlocation>
    ```
2. Run the script:

    ```bash
    python encrypt.py
    ```

3. Select the operation:
    - **Encryption:** Encrypt a text file.
    - **Decryption:** Decrypt an encrypted text file.
    - **Quit:** Exit the program.

4. Enter the required information:
    - For encryption: provide the path of the file to encrypt, the location to save the encrypted file, and the encryption key.
    - For decryption: provide the path of the encrypted file, the location to save the decrypted file, and the decryption key.

5. Follow the prompts to complete the encryption or decryption process.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
