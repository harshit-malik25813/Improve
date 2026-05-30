"""Improve CLI"""
"""Developed by: harshit-malik25813"""
"""Open Sourced on GitHub"""
"""https://github.com/harshit-malik25813/Improve"""
import argparse # To include the functionality of parsing the arguements
import json # To Read JSON file containing the user data
from pathlib import Path # To locate the path of essential tracking data
# Essential helper functions imported
from src import helpers, setup as setup_mod, project as project_mod 
from src.help import show_help, commands 

# User tracking path
USER_FILE = Path("tracking") / "user_info.json"

# Internal function to load user data and return it
def _load_user():
	if USER_FILE.exists():
		with USER_FILE.open("r", encoding="utf-8") as f:
			return json.load(f)
	return {"user_exists": False, "user_name": "", "password": ""}

# Main program
def main():
	# Adding argument parsers
	parser = argparse.ArgumentParser(prog="improve", description="Improve CLI", add_help=False) # Initiate parsing of arguements
	parser.add_argument("-h", "--help", action="store_true")
	parser.add_argument("--commands", action="store_true")
	# Allow subparsers in the program
	subparsers = parser.add_subparsers(dest="command")

	# setup arguments
	setup_parser = subparsers.add_parser("setup") # Setup parser
	setup_parser.add_argument("--login", action="store_true") # Login argument
	setup_parser.add_argument("--logout", action="store_true") # Logout argument
	setup_sub = setup_parser.add_subparsers(dest="setup_cmd") # Refer to setup subarguments as 'setup_cmd'
	update_parser = setup_sub.add_parser("update_user") # Update user subargument
	update_parser.add_argument("--username", action="store_true")
	update_parser.add_argument("--password", action="store_true")

	# add-project (legacy) - kept for backward compatibility as the feature has been integrated with project command
	addp = subparsers.add_parser("add-project") # add-project argument
	addp.add_argument("project_name") # Project name

	# project management group(improved)
	project_parser = subparsers.add_parser("project")
	project_sub = project_parser.add_subparsers(dest="proj_cmd")
	project_sub.add_parser("list")
	create = project_sub.add_parser("create")
	create.add_argument("project_name")
	add_entry = project_sub.add_parser("add-entry")
	add_entry.add_argument("project_name")
	add_entry.add_argument("--day", default="")
	add_entry.add_argument("--date", default="")
	add_entry.add_argument("--progress", default="")
	add_entry.add_argument("--productivity", default="")
	add_entry.add_argument("--feedback", default="")
	feedback = project_sub.add_parser("feedback")
	feedback.add_argument("project_name")
	feedback.add_argument("--last", type=int, default=5)
	show = project_sub.add_parser("show")
	show.add_argument("project_name")
	show.add_argument("--last", type=int, default=10)
	delete = project_sub.add_parser("delete")
	delete.add_argument("project_name")

	# export
	subparsers.add_parser("export")

	args = parser.parse_args()

	user_info = _load_user() # Load user data
	if not user_info.get("user_exists"): # If the user data doesn't exist
		helpers.first_time() # Initiate the script to invite user for the first time
	else:
		print(f"Welcome back!, {user_info.get('user_name')}")

	if args.command == "setup": # If user enters setup
		if getattr(args, "login", False): # For login
			setup_mod.login()
		elif getattr(args, "logout", False): # For logout
			setup_mod.logout()
		elif args.setup_cmd == "update_user": # For updating user
			if getattr(args, "username", False):
				setup_mod.update_user("--username")
			elif getattr(args, "password", False):
				setup_mod.update_user("--password")
			else:
				show_help()
		else:
			show_help() # If user enters anything unexpected
		return

	if getattr(args, "help", False): # If user enters help
		if getattr(args, "commands", False): # If person specifially asks to list commands
			commands()
		else:# Just show the help page
			show_help()
		return

	if args.command == "add-project": # Legacy function to create the project
		# legacy behavior: create project CSV
		project_mod.create_project(args.project_name) # Use the create project function in place of add_project.py
		return
	# Project functions
	if args.command == "project":
		if args.proj_cmd == "list":
			project_mod.list_projects()
		elif args.proj_cmd == "create":
			project_mod.create_project(args.project_name)
		elif args.proj_cmd == "add-entry":
			project_mod.add_entry(args.project_name, day=args.day, date=args.date, progress=args.progress, productivity=args.productivity, feedback=args.feedback)
		elif args.proj_cmd == "feedback":
			project_mod.get_feedback(args.project_name, last=args.last)
		elif args.proj_cmd == "show":
			project_mod.show_project(args.project_name, last=args.last)
		elif args.proj_cmd == "delete":
			project_mod.delete_project(args.project_name)
		else:
			show_help()
		return
	# Export functions
	if args.command == "export":
		from src.export import export_data
		export_data()
		return
	# if invalid
	parser.print_help()
# Initialise the function
if __name__ == "__main__":
	main()
