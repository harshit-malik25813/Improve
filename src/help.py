def show_help():
    print("Improve")
    print("You might have entered a wrong command to get here")
    print("To see the list of commands, run: improve help --commands")


def commands():
    print("Available commands:")
    print("  setup login")
    print("  setup logout")
    print("  setup update --username | --password")
    print("  project list")
    print("  project create <name>")
    print("  project add-entry <name> [--day] [--date] [--progress] [--productivity] [--feedback]")
    print("  project show <name> [--last N]")
    print("  project feedback <name> [--last N]")
    print("  project delete <name>")
    print("  add-project <name>   (legacy; prefer project create)")
    print("  export")
