from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt = b'1234567890123456',
    iterations=1_200_000,
)

key1 = input("Enter your key: ").encode('utf-8')
key = base64.urlsafe_b64encode(kdf.derive(key1))
f = Fernet(key)

while True:
    user_choice = input("Do you want to read , write the password or want to exit the program (r , w , e) : ").lower()

    if user_choice == 'w':
        app = input("Enter the App name: ")
        real_password = input("Enter the passowrd: ")
        password = f.encrypt(real_password.encode('utf-8')).decode()
        with open ("Passwords.txt" , "a") as file:
            file.write("\n" + f"App : {app} " + "\n" + f"Password : {password} " + "\n")

    elif user_choice == "r":
        with open("Passwords.txt" ,"r") as file:
            app = file.readlines()
            new_app = [row.replace("\n" , "") for row in app if row != "\n"]
            # try:
            counter = -1
            for text in new_app:
                    counter += 1
                    if "Password : " in text:
                        password2 = text.replace("Password : ","")
                        real_password2 = f.decrypt(password2.encode('utf-8'))
                        new_app[counter] = real_password2.decode()
            print(new_app)
            # except :
            #     print("The key was wrong")
            #     break
    elif user_choice == "e":
        break
    else:
        print("Enter the valid choice !")