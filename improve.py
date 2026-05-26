"""Improve"""
"""By Harshit Malik"""
"""Github: harshit-malik25813"""
# Parsing Arguements
import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()
# Importing defined libraries for the program
import src.helpers
import src.setup
from src.help import commands, help
import src.add_project
# Importing JSON library to load and process user info
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
# Setting up subparser for the setup function
subparsers = parser.add_subparsers(dest="command")
setup_parser = subparsers.add_parser("setup")
setup_subparser = setup_parser.add_subparsers(dest="setup_cmd")
# Adding login, logout, and update_user
setup_subparser.add_parser("logout")
setup_subparser.add_parser("login")
update_usr = setup_subparser.add_parser("update_user")
update_usr_subparser = update_usr.add_subparsers(dest="update_field")
update_usr_subparser.add_parser("--username")
update_usr_subparser.add_parser("--password")
if args.command == "setup":
	if args.setup_cmd == "login":
		src.setup.login()
	if args.setup_cmd == "logout":
		src.setup.logout()
	if args.setup_cmd == "update_user":
		src.setup.update_user(args.update_field)
	else:
		help()
# Adding the help functionality
help_parser = subparsers.add_parser("-h")
help_subparser = help_parser.add_subparsers(dest="help_cmd")
help_subparser.add_parser("--commands")
if args.command == "help":
	if args.help_cmd == "--commands":
		commands()
	else:
		help()
# Adding project 
project = subparsers.add_parser("add-project")
project_subparser = project.add_subparsers(dest="project")
if args.command == "project":
	src.add_project.include(args.project)
