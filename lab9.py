# Program Name: Lab9.py
# Course: IT1114
# Student Name: laydix roblero
# Assignment Number: Lab 9
# Due Date: 11/8/25
# Purpose: Verify that a user entered password meets specified requirements
# Resources: powerpoints and youtube

SPECIALS = {'#', '!','$','_'} # it gives it a task .

def is_valid_password(password: str)->bool: #loops ?
    if len(password) <9:
        return False
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch in SPECIALS for ch in password)
    has_special= any(ch in SPECIALS for ch in password)

    return has_upper and has_lower and has_digit and has_special

def main()-> None:
    password = input("Password:")

    if is_valid_password(password):
        print("Valid Password: ")
    else:
        print("Invalid Password")

if __name__ == "__main__":
    main()

