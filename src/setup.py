from dataclasses import dataclass
import os
import json # Importing to maintain persistent storage for user
def set_user(json): # Creating a function to help user log in
    print("User Account not set")
    ans = input("Do you want to set a user?(y/n)")
    if ans == "n":
        return
    if ans != "y":
        print("please enter a valid input")
        set_user(json)
        return
    # If user affirms to create an account

    @dataclass
    class User:
        user_name: str
        password: str
    # Creating a reusable block of code for the signup part
    def signup():
        user_name = input("Username: ")
        password = input("Password: ")

        return User(user_name, password)
    user = signup()
    # Validating user name
    if len(user.user_name) < 4:
        print("The length of user name should be atleast 4 characters!")
        signup()
    # Validating password
    if len(user.password) < 8:
        print("The password should atleast be 8 characters or more!")
        signup()
    hasdigit = any(char.isdigit() for char in user.password)
    if not hasdigit:
        print("Password must contain digits!")
        signup()
    special_char = "!@#$%^&*()"
    present = any(c in special_char for c in user.password)
    if not present:
        print("Password must contain special characters")
        signup()
    haslower = any(c.islower() for c in user.password)
    if not haslower:
        print("Password must contain lower characters")
        signup()
    hasalpha = any(c.isalpha() for c in user.password)
    if not hasalpha:
        print("Password must contain alphabets")
        signup()
    hasupper = any(c.isupper() for c in user.password)
    if not hasupper:
        print("Password must contain upper characters")
        signup()
with open("user_info.json", "r") as f:
    data_check = json.load(f)
    if data_check["user_exists"] == False:
        set_user(data_check)    