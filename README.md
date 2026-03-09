# Passsword Manager
A simple CLI based password manager that takes the multiple passwords and encrpyt them and then store them in the file to be decrypted and used later
## Features
- Secure password encryption using Fernet symmetric encryption
- Uses PBKDF2 key derivation with SHA256 for strong security
- Allows storing passwords for multiple applications
- Retrieve password for a specific app
- Option to display all stored passwords
- Passwords are stored encrypted, not in plain text
- Simple command-line interface
- Protection against wrong keys (decryption fails safely)

## How the App Works
1. Run the program.
2. Enter a secret key (this key is used to encrypt and decrypt passwords).
3. Choose one of the options:
    - w → Write a new password
    - r → Read saved passwords
    - e → Exit the program
4. When writing a password:
    - Enter the application name
    - Enter the password
    - The password will be encrypted and saved to Passwords.txt.
5.  When reading passwords:
    - Enter the app name to get its password
    - Enter a to display all stored passwords
    - If something goes wrong (wrong spelling, no connection, etc.), an error message appears.

## How to Run the Program
1. Make sure **Python** is installed.
2. Install all required modules using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
3. Run the program
    ```bash
    python Main.py
    ```
    
## File Structure
```bash
project/
│── Main.py
│── README.md
│── requirements.txt
│── Passwords.txt (it will be generated upon running the programs and saving atleast one password)
```

## Technologies Used
- Python
- cryptograph
- PBKDF2 Key Derivation
- SHA256 hashing
- Base64 encoding 

## Notes
- Passwords are encrypted using Fernet symmetric encryption.
- The user key is strengthened using PBKDF2HMAC with 1,200,000 iterations.
- Encrypted passwords are stored in Passwords.txt.
- Without the correct key, stored passwords cannot be decrypted.

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!
