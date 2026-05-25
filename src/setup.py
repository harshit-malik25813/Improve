"""Improve"""
"""By Harshit Malik"""
"""Github: harshit-malik25813"""
"""Setting up user account for the first time"""
from dataclasses import dataclass
from .export import export_data
import json # Importing to maintain persistent storage for user info
from .help import help
with open("user_info", "rw") as f:
    data_check = json.load(f)
user_exists = data_check["user_exists"]
def login():
    def set_user(json): # Creating a function to help user log in
        print("User Account not set")
        # Ask user if he wishes to make a user account
        ans = input("Do you want to set a user?(y/n)").lower()
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
        # Getting a boolean value for whether the user has entered some uppercase characters
        hasupper = any(c.isupper() for c in user.password)
        # Validating presence of uppercase characters
        if not hasupper:
            print("Password must contain upper characters")
            signup()
        # If user somehow makes it this far without getting annoyed
        return
    # Actual function
    # If the user comes to login when he already created a user account
    if data_check["user_exists"] == "True":
        print("A user already exists")
        print(f"You have been logged in as {data_check["user_name"]}")

    # Add the user info to the JSON storing the user data
    if data_check["user_exists"] == "False":
        set_user(data_check)
        print("User has been set successfully!")
        print("Log in to start your improvement journey!")
    return
def logout():
    with open("user_info.json", "r") as f:
        user_data = json.load(f)
    print("Logout")
    confirmation = input("Are you sure you want to logout, your data will be deleted unless exported(y/n)?").lower()
    if confirmation != "y" or "n":
        print("Please respond with y/Y for yes or n/N for no")
        logout()
    if confirmation == "y":
        ans = input("Do you wish to export your progress report to CSV(y/n)?").lower()
        if ans != "y" or "n":
            print("Please respond with y/Y for yes or n/N for no")
            logout()
        if ans == "y":
            export_data()
            no_user = {
                "user_exists" : "False",
                "user_name" : "",
                "password" : ""
            }
            json.dump(no_user, data_check)
        if ans == "n":
            no_user = {
                "user_exists" : "False",
                "user_name" : "",
                "password" : ""
            }
            json.dump(no_user, data_check)
    if confirmation == "n":
        return
def update_user(update):
    if update != "username" or "password":
        print("Invalid input!")
        help()
    if update == "username":
        confirmation = input("Are you sure you want to change your username(y/n)?").lower()
        if confirmation != "y" or "n":
            print("Please respond with y/Y or n/N")
            update_user(update)
        if confirmation == "n":
            return
        if confirmation == "y":
            user_info = {
                "user_exists" : "true",
                "user_name" : update,
                "password" : data_check["password"]
            }
            json.dump(user_info, data_check)
            return

    