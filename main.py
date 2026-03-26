from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random
import string


def password_manger(user_password = "", code = 0 ):
    key  = input("Enter your key: ").encode('utf-8')
    while True:
        if code == 0 :
            user_choice = input("Do you want to read , write the password or want to exit the program (r , w , e) : ").lower()
        else:
            user_choice = 'w'
        if user_choice == 'w':
            app = input("Enter the App name: ")
            if code == 0:
                app_password = input("Enter the passowrd: ")
            else:
                app_password = user_password
            encryptd_password = encrpyt_password(app_password,key)
            with open ("Passwords.txt" , "a") as file:
                file.write("\n" + f"App : {app} " + "\n" + f"Password : {encryptd_password} " + "\n")
            
            if code != 0:
                break

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

def generate_password(min_len , want_digits = True , want_special = True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    password = ""
    for i in range(min_len):
        if want_digits and want_special:
            password += random.choice(letters + digits + punctuation)
        elif want_digits and not want_special:
            password += random.choice(letters + digits)
        elif not want_digits and want_special:
            password += random.choice(letters + punctuation)
        else:
            password += random.choice(letters)

    return password

def get_password_info():
    while True:
        try:
            min_len = int(input("Enter the minimum length of password that you need: "))
            break
        except ValueError:
            print("Please enter the number")
    want_digits = True if input("Want digits (Y / N): ").lower() == "y" else False
    want_special = True if input("Want special chracters (Y / N): ").lower() == "y" else False
    password = generate_password(min_len , want_digits , want_special)

    return password

def  main():
    while True:
        choice = int(input("Do you want to generate Password or access manage (1 / 2): "))
        if choice in [1 ,2]:
            break
    
    if choice == 2:
        password_manger()
    else:
        password = get_password_info()
        print(f"Password: {password}")
        code = int(input("Do you want to save password or not (1 / 2): "))
        if code == 1:
            password_manger(password,code)

if __name__ == "__main__":
    main()