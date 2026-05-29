"""User setup utilities for Improve CLI"""
from dataclasses import dataclass # to create dataclass for user 
import json # to access user data in JSON file
from pathlib import Path # To manipulate the folder and files
import shutil # To make directories
from .export import export_data # Export data
from .help import show_help # Printing help

USER_FILE = Path("tracking") / "user_info.json" # The path of user file 
# Declaring essential functions

def _load_user_info():
    # Do not create the file by default. Return defaults if file missing.
    if not USER_FILE.exists():
        return {"user_exists": False, "user_name": "", "password": ""}
    with USER_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

# To write user_info
def _write_user_info(data: dict):
    # To write user info in a JSON file for the first time
    USER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with USER_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# To validate password
def _validate_password(pw: str) -> tuple[bool, str]:
    if len(pw) < 8:
        return False, "Password must be at least 8 characters"
    if not any(c.isdigit() for c in pw):
        return False, "Password must contain a digit"
    special_char = "!@#$%^&*()"
    if not any(c in special_char for c in pw):
        return False, "Password must contain a special character"
    if not any(c.isalpha() for c in pw):
        return False, "Password must contain alphabetic characters"
    if not any(c.islower() for c in pw):
        return False, "Password must contain a lowercase character"
    if not any(c.isupper() for c in pw):
        return False, "Password must contain an uppercase character"
    return True, ""

# Logging user in
def login():
    data = _load_user_info()
    # If user exists, no need to do anything
    if data.get("user_exists"):
        print(f"A user already exists. You are logged in as {data.get('user_name')}")
        return

    print("User Account not set")
    # Get user confirmation
    ans = input("Do you want to set a user? (y/n): ").strip().lower()
    if ans != "y" or "n":
        print("Invalid Input!")
        login()
        return
    if ans == "n":
        print("Aborting user setup")
        return
    # Setting up a dataclass to help with easily accessing username and password
    @dataclass
    class User:
        user_name: str
        password: str
    # Setting up the user
    # Only let user leave if he enters the username and password correctly
    while True:
        # Validating username and password
        user_name = input("Username: ").strip()
        if len(user_name) < 4:

            print("The length of user name should be at least 4 characters!")
            continue

        password = input("Password: ")
        valid, msg = _validate_password(password)
        if not valid:
            print(msg)
            continue
        user = User(user_name, password)
        break

    new_data = {"user_exists": True, "user_name": user.user_name, "password": user.password}
    _write_user_info(new_data)
    print("User has been set successfully!")
    print("Log in to start your improvement journey!")

# Logging user out
def logout():
    data = _load_user_info()
    # If user tries to log out but user doesn't exist
    if not data.get("user_exists"):
        print("No user is currently logged in.")
        return
    print("Logout")
    # Asking user for confirmation
    confirmation = input("Are you sure you want to logout? Your data will be deleted unless exported (y/n): ").strip().lower()
    if confirmation not in ("y", "n"):
        print("Please respond with y or n")
        return
    if confirmation == "n":
        return
    # Ask user if he wishes to export his data
    ans = input("Do you wish to export your progress report to CSV before logout? (y/n): ").strip().lower()
    if ans == "y":
        export_data()
        # After successful export, offer to delete the tracking directory
        try:
            tracking_dir = USER_FILE.parent
            if tracking_dir.exists():
                delete_confirm = input("Export complete. Do you want to delete the tracking directory? (y/n): ").strip().lower()
                if delete_confirm == "y":
                    shutil.rmtree(tracking_dir)
                    print("Tracking directory deleted.")
        except Exception as e:
            print(f"Warning: failed to delete tracking directory: {e}")
    # Update JSON file
    no_user = {"user_exists": False, "user_name": "", "password": ""}
    _write_user_info(no_user)
    print("Logged out and user data cleared.")

# To update user data
def update_user(update_field: str):
    if update_field not in ("--username", "--password"):
        print("Invalid input!")
        show_help()
        return
    data = _load_user_info()
    if not data.get("user_exists"):
        print("No user set. Run 'setup login' to create an account.")
        return

    if update_field == "--username":
        new_username = input("Enter new username: ").strip()
        if len(new_username) < 4:
            print("Username must be at least 4 characters long")
            return
        data["user_name"] = new_username
        _write_user_info(data)
        print("Username updated.")
        return

    if update_field == "--password":
        new_password = input("Enter new password: ")
        valid, msg = _validate_password(new_password)
        if not valid:
            print(msg)
            return
        data["password"] = new_password
        _write_user_info(data)
        print("Password updated.")
        return