"""Improve CLI"""
"""Developed by: harshit-malik25813"""
"""Open Sourced on GitHub"""
"""https://github.com/harshit-malik25813/Improve"""
import argparse # To include the functionality of parsing the arguements
import json # To Read JSON file containing the user data
from functools import lru_cache
from pathlib import Path # To locate the path of essential tracking data
# Essential helper functions imported
from src import helpers, setup as setup_mod, project as project_mod 
from src.help import show_help, commands 

# User tracking path
USER_FILE = Path("tracking") / "user_info.json"
PROJECT_ROOT = Path(__file__).resolve().parent
PYPROJECT_FILE = PROJECT_ROOT / "pyproject.toml"


@lru_cache(maxsize=1)
def _load_version():
	try:
		try:
			import tomllib
		except ModuleNotFoundError:
			tomllib = None
		if tomllib is not None:
			with PYPROJECT_FILE.open("rb") as f:
				data = tomllib.load(f)
			return data["project"]["version"]
		in_project_section = False
		with PYPROJECT_FILE.open("r", encoding="utf-8") as f:
			for raw_line in f:
				line = raw_line.strip()
				if not line or line.startswith("#"):
					continue
				if line.startswith("[") and line.endswith("]"):
					in_project_section = line == "[project]"
					continue
				if in_project_section and line.startswith("version"):
					_, value = line.split("=", 1)
					return value.strip().strip('"').strip("'")
		return "unknown"
	except (FileNotFoundError, KeyError, ValueError, OSError):
		return "unknown"

# Internal function to load user data and return it
def _load_user():
	if USER_FILE.exists():
		with USER_FILE.open("r", encoding="utf-8") as f:
			return json.load(f)
	return {"user_exists": False, "user_name": "", "password": ""}

# Main program
def main():
	# Adding argument parsers
	parser = argparse.ArgumentParser(prog="improve", description="Improve CLI") # Initiate parsing of arguements
	parser.add_argument("--version", action="version", version=f"improve-cli {_load_version()}\nDeveloped by harshit-malik25813")
	# Allow subparsers in the program
	subparsers = parser.add_subparsers(dest="command")

	# setup arguments
	setup_parser = subparsers.add_parser("setup", help="Manage your local user account")
	setup_sub = setup_parser.add_subparsers(dest="setup_cmd", required=True)
	setup_sub.add_parser("login", help="Create or sign in to your local account")
	setup_sub.add_parser("logout", help="Sign out and clear local user data")
	update_parser = setup_sub.add_parser("update", help="Update username or password")
	update_group = update_parser.add_mutually_exclusive_group(required=True)
	update_group.add_argument("--username", action="store_true", help="Change username")
	update_group.add_argument("--password", action="store_true", help="Change password")

	# help (use "help" not "--help"; argparse reserves --help for usage)
	help_parser = subparsers.add_parser("help", help="Show help or list commands")
	help_parser.add_argument("--commands", action="store_true", help="List all commands")

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

	if args.command == "setup":
		if args.setup_cmd == "login":
			setup_mod.login()
		elif args.setup_cmd == "logout":
			setup_mod.logout()
		elif args.setup_cmd == "update":
			if args.username:
				setup_mod.update_user("username")
			else:
				setup_mod.update_user("password")
		return

	if args.command == "help":
		if args.commands:
			commands()
		else:
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
