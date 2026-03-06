from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def password_manger():
    key  = input("Enter your key: ").encode('utf-8')
    while True:
        user_choice = input("Do you want to read , write the password or want to exit the program (r , w , e) : ").lower()

        if user_choice == 'w':
            app = input("Enter the App name: ")
            app_password = input("Enter the passowrd: ")
            encryptd_password = encrpyt_password(app_password,key)
            with open ("Passwords.txt" , "a") as file:
                file.write("\n" + f"App : {app} " + "\n" + f"Password : {encryptd_password} " + "\n")

        elif user_choice == "r":
            app_name = input("Enter the app name you want to access the password of or a for all: ").lower()
            with open("Passwords.txt" ,"r") as file:
                app = file.readlines()
                lines = [row.replace("\n" , "") for row in app if row != "\n"]
                passwords = {}
                try:
                    counter = -1
                    for text in lines:
                            counter += 1
                            if "App : " in text:
                                passwords[text.replace("App : " ,"").strip()] = decrpyt_password(lines[counter+1].replace("Password : ",""), key).decode()
                    if app_name == 'a':
                        print(passwords)
                    else:
                        for k,v in passwords.items():
                            if k.lower() == app_name.lower():
                                print(f"The password of the app {k} is {v}")
                except :
                    print("The key was wrong")
                    break

        elif user_choice == "e":
            break
        else:
            print("Enter the valid choice !")

def encrpyt_password(password , key):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt = b'1234567890123456',
        iterations=1_200_000,
    )

    key1 = base64.urlsafe_b64encode(kdf.derive(key))
    f = Fernet(key1)

    return f.encrypt(password.encode('utf-8')).decode()

def decrpyt_password (password , key):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt = b'1234567890123456',
        iterations=1_200_000,
    )

    key1 = base64.urlsafe_b64encode(kdf.derive(key))
    f = Fernet(key1)

    return f.decrypt(password.encode('utf-8'))

password_manger()