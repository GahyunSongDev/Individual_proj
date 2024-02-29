from cryptography.fernet import Fernet

# gernerate and save the key
# def writeKey():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# writeKey()

def loadKey():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Please run a key generation script first.")
        quit()

key = loadKey()
cipher = Fernet(key) # byte type (b' ...)

def encrypt_info(info):
    cipher_info = cipher.encrypt(info.encode()) # change the string(info) to byte type for encryption
    return cipher_info.decode() # chagne byte type to string type


def decrypt_info(cipher_info):
    try:
        decrypted_info = cipher.decrypt(cipher_info.encode()).decode()
        return decrypted_info
    except Exception as e:
        print(f"Decryption error: {e}")
        return None
    
# debugging for testing encryption/decryption   
# encrypted_data = encrypt_info("song")
# print(f"Encrypted Data: {encrypted_data}")

# # decrypt_info 함수를 사용하여 복호화
# decrypted_data = decrypt_info(encrypted_data)
# print(f"Decrypted Data: {decrypted_data}")

def signUp():
    username = input("\nWhat is your name? ").lower()
    pwd = input("\nEnter your password: ").lower()
    dob = input("\nEnter your Date of birth (MMDDYYYY): ")

    encrypted_pwd = encrypt_info(pwd)

    with open('members.txt', 'a') as f:
        f.write(f"{username}/{encrypted_pwd}/{dob}\n")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nYou're successfully signed up")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def signIn():
    uName = input("\nWhat is your name? ").lower()
    pwd = input("\nEnter your password: ").lower()

    with open('members.txt', 'r') as f:
        for line in f:
            parts = line.strip().split("/")
            decrypted_pwd = decrypt_info(parts[1])
            if uName == parts[0] and decrypted_pwd is not None and pwd == decrypted_pwd:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\nThank you! ", uName, "\nYou successfully signed in.")
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
        print("\nInvalid username or password. Please try again.")

def forgetName(a):
    with open('members.txt', 'r') as f:
        for line in f.readlines():
            parts = line.split("/")
            stored_dob = parts[2].strip()   # Extract and remove leading/trailing whitespaces
            if a == stored_dob :
                uName, encryptPwd, dob = parts
                print("\n---------------------------------")
                print(f"\nFound username: {uName}\n")
                print("\n---------------------------------")
                return
        print("\nWe can't find your name.")

def forgetPwd(b):
    username, dob = b.split(",")    # split the user inpue with comma initialize them again
    with open('members.txt', 'r') as f:
        for line in f.readlines():
            parts = line.split("/")
            stored_uname = parts[0].strip().lower()
            stored_pwd = parts[1].strip()
            stored_dob = parts[2].strip()
            if username == stored_uname and dob == stored_dob:
                uName, encryptPwd, dob = parts
                decrypted_data = decrypt_info(stored_pwd)
                if decrypted_data is not None:
                    print("\n---------------------------------")
                    print(f"\nYour username : {uName}")
                    print(f"\nFound password: {decrypted_data}\n")
                    print("\n---------------------------------")
                    return
                else:
                    print("\nDecryption failed. Cannot display password.")
                    return
        print("\nWe can't find your password.")

print("\nWelcome!")

while True:
    mode = input("\nWould you like to sign up or sign in? (sign in/sign up/quit) \nIf you forget your name/password, type 'forget'  ").lower()

    if mode == "quit":
        print("\nBye ;->\n")
        quit()

    if mode == "sign in":
        signIn()
        break

    elif mode == "sign up":
        signUp()

    elif mode == "forget":
        option = input("\nDo you want to find 'username' or 'password'? (Username/Password) ").lower()

        if option == "username":
            nameToFind = input("\nEnter your date of birth (MMDDYYYY): ")
            forgetName(nameToFind)
        elif option == "password":
            pwdToFind = input("\nEnter your username and date of birth (comma and no white space in between): ").lower()
            forgetPwd(pwdToFind)
        else:
            print("\nError !!!!")
            break

    else:
        print("\nError! Please try again")
