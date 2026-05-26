"""Improve CLI"""
import argparse
import json
from pathlib import Path
from src import helpers, add_project, setup as setup_mod, project as project_mod
from src.help import show_help, commands


USER_FILE = Path("tracking") / "user_info.json"


def _load_user():
	if USER_FILE.exists():
		with USER_FILE.open("r", encoding="utf-8") as f:
			return json.load(f)
	return {"user_exists": False, "user_name": "", "password": ""}


def main():
	parser = argparse.ArgumentParser(prog="improve", description="Improve CLI")
	subparsers = parser.add_subparsers(dest="command")

	# setup
	setup_parser = subparsers.add_parser("setup")
	setup_sub = setup_parser.add_subparsers(dest="setup_cmd")
	setup_sub.add_parser("login")
	setup_sub.add_parser("logout")
	update_parser = setup_sub.add_parser("update_user")
	update_parser.add_argument("update_field", choices=["--username", "--password"]) 

	# help
	help_parser = subparsers.add_parser("help")
	help_parser.add_argument("--commands", action="store_true")

	# add-project (legacy) - kept for backward compatibility
	addp = subparsers.add_parser("add-project")
	addp.add_argument("project_name")

	# project management group
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

	user_info = _load_user()
	if not user_info.get("user_exists"):
		helpers.first_time()
	else:
		print(f"Welcome back!, {user_info.get('user_name')}")

	if args.command == "setup":
		if args.setup_cmd == "login":
			setup_mod.login()
		elif args.setup_cmd == "logout":
			setup_mod.logout()
		elif args.setup_cmd == "update_user":
			setup_mod.update_user(args.update_field)
		else:
			show_help()
		return

	if args.command == "help":
		if args.commands:
			commands()
		else:
			show_help()
		return

	if args.command == "add-project":
		# legacy behavior: create project CSV
		project_mod.create_project(args.project_name)
		return

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

	if args.command == "export":
		from src.export import export_data
		export_data()
		return

	parser.print_help()


if __name__ == "__main__":
	main()
