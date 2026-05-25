"""Setting up user account for the first time"""
from dataclasses import dataclass
import os
import json # Importing to maintain persistent storage for user
def set_user(json): # Creating a function to help user log in
    print("User Account not set")
    # Ask user if he wishes to make a user account
    ans = input("Do you want to set a user?(y/n)")
    if ans == "n":
        return
    if ans != "y":
        print("please enter a valid input")
        set_user(json)
        return
    # If user affirms to create an account
    # Creating a dataclass to easily access user name and password
    @dataclass
    class User:
        user_name: str
        password: str
    # Creating a reusable block of code for the signup part
    def signup():
        user_name = input("Username: ")
        password = input("Password: ")

        return User(user_name, password)
    # Initialising the function
    user = signup()
    # Validating user name
    # Checking the length of the user name
    if len(user.user_name) < 4:
        print("The length of user name should be atleast 4 characters!")
        signup()
    # Validating password
    # Checking the length of the password
    if len(user.password) < 8:
        print("The password should atleast be 8 characters or more!")
        signup()
    # getting a boolean value for whether the password contains any digit
    hasdigit = any(char.isdigit() for char in user.password)
    # Validating presence of digits in the password
    if not hasdigit:
        print("Password must contain digits!")
        signup()
    # getting a boolean value for whether the password contains any special characters
    special_char = "!@#$%^&*()"
    present = any(c in special_char for c in user.password)
    # Validating presence of special character in password
    if not present:
        print("Password must contain special characters")
        signup()
    # Getting a boolean value for whether the password contains alphabets
    hasalpha = any(c.isalpha() for c in user.password)
    if not hasalpha:
        print("Password must contain alphabets")
        signup()
    # getting a boolean value for whether the password contains any lowercase letters
    haslower = any(c.islower() for c in user.password)
    # Validating the presence of lowercase characters
    if not haslower:
        print("Password must contain lower characters")
        signup()
    hasupper = any(c.isupper() for c in user.password)
    if not hasupper:
        print("Password must contain upper characters")
        signup()
    return
with open("user_info.json", "r") as f:
    data_check = json.load(f)
    if data_check["user_exists"] == False:
        set_user(data_check)
    print("User has been set successfully!")
    print("Log in to start your improvement journey!")
    exit
    if data_check["user_exists"] == True:
        print("A user already exists")
        print(f"You have been logged in as {data_check["user_name"]}")     