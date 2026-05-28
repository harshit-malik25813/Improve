**Improve — CLI Project Tracker**

Improve is a small, single-file CLI application (with supporting modules under `src/`) to help you track progress on projects using CSV-backed project logs. It provides simple user setup, per-project CSV tracking, quick reporting and export functionality.

**Features**
- **User setup:** create, update, and logout a local user account (`setup` commands).
- **Project management:** create, list, delete projects and add daily entries (`project` commands).
- **Entry tracking:** each project is stored as a CSV under `tracking/` with columns Day, Date, Progress, Productivity Level, Feedback.
- **Feedback & view:** fetch recent feedback entries or show recent rows for a project.
- **Export:** copy all tracking CSV files to a `backup/` folder.

**Quick Links**
- Main CLI entry: [improve.py](improve.py)
- Core project logic: [src/project.py](src/project.py)
- User/setup utilities: [src/setup.py](src/setup.py)
- Export helper: [src/export.py](src/export.py)
- First-run helper text: [src/helpers.py](src/helpers.py)
- Legacy project helper: [src/add_project.py](src/add_project.py)

**Requirements & Setup**
- Python 3.9+ recommended (uses standard library features such as `dataclasses` and `pathlib`).
- No third-party packages are required—the provided `requirements.txt` lists standard-library modules and can be ignored for pip installs.
- Create and activate a virtual environment (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Running the CLI**
- Basic help:

```bash
python improve.py --help
```

- Setup a user account (interactive):

```bash
python improve.py setup login
```

- Create a project:

```bash
python improve.py project create MyProject
```

- Add an entry to a project:

```bash
python improve.py project add-entry MyProject --day "Day 1" --date "2026-05-28" --progress "Started" --productivity "7" --feedback "Good start"
```

- List projects:

```bash
python improve.py project list
```

- Show recent entries for a project:

```bash
python improve.py project show MyProject --last 10
```

- Get recent feedback entries:

```bash
python improve.py project feedback MyProject --last 5
```

- Export all tracking CSVs to `backup/`:

```bash
python improve.py export
```

**Storage & File Layout**
- Tracking CSVs and user info are stored in the `tracking/` directory. Example files:
	- `tracking/MyProject.csv` — per-project CSV with header `Day,Date,Progress,Productivity Level,Feedback`
	- `tracking/user_info.json` — stores a small JSON object with `user_exists`, `user_name`, and `password`.

**Notes & Behavior**
- The CLI is implemented in `improve.py` and delegates commands to modules in `src/`.
- Password validation enforces a minimum length and requires digits, alphabetic, uppercase, lowercase and a special character (see `src/setup.py`).
- The `add-project` command is retained for backward compatibility but `project create` is preferred.

**Development & Contribution**
- Run the CLI directly with `python improve.py` to test features.
- The codebase is small and intended as a learning/demo project. Contributions or issues can be opened against the original upstream repository referenced in the code comments.

**License**
- This repository does not include a license file. Check the original upstream project before reusing code in production.

