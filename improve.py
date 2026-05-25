"""Open-source project"""
"""By Harshit Malik"""
"""Github: harshit-malik25813"""
import src.helpers
import json
with open("user_info.json", "r") as f:
	user_info = json.load(f)
from src.setup import user_exists
if user_exists == False:
	src.helpers.first_time()
if user_exists == True:
	print(f"Welcome back!, {user_info["user_name"]}")
# Adding actual functionality for the program
# Using argparse for usage of extra arguements

