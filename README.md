# **Improve — CLI Project Tracker**

Improve is a small, single-file CLI application (with supporting modules under `src/`) to help you track progress on projects using CSV-backed project logs. It provides simple user setup, per-project CSV tracking, quick reporting and export functionality.

## **Features**
- **User setup:** create, update, and logout a local user account (`setup` commands).
- **Project management:** create, list, delete projects and add daily entries (`project` commands).
- **Entry tracking:** each project is stored as a CSV under `tracking/` with columns Day, Date, Progress, Productivity Level, Feedback.
- **Feedback & view:** fetch recent feedback entries or show recent rows for a project.
- **Export:** copy all tracking CSV files to a `backup/` folder.

### **Quick Links**
- Main CLI entry: [improve.py](improve.py)
- Core project logic: [src/project.py](src/project.py)
- User/setup utilities: [src/setup.py](src/setup.py)
- Export helper: [src/export.py](src/export.py)
- First-run helper text: [src/helpers.py](src/helpers.py)
- Legacy project helper: [src/add_project.py](src/add_project.py)

## **Requirements**
- Python 3.9+ (`requires-python` in [pyproject.toml](pyproject.toml); uses standard library features such as `dataclasses` and `pathlib`).
- No third-party runtime dependencies. The package is defined in [pyproject.toml](pyproject.toml); [requirements.txt](requirements.txt) only lists standard-library modules for reference and is not used by pip.

## **Install with pip**

From a clone of this repository (recommended: use a virtual environment):

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install .
```

After install, the `improve` console script is on your `PATH` (same commands as `python improve.py` below).

For local development (changes to `improve.py` or `src/` apply without reinstalling):

```bash
pip install -e .
```

Install a built wheel without cloning:

```bash
pip install dist/improve_cli-0.1.0-py3-none-any.whl
```

## **Build from source**

Build sdist and wheel artifacts into `dist/` (requires [build](https://pypi.org/project/build/) once per environment):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install build
python -m build
```

Outputs:
- `dist/improve_cli-0.1.0.tar.gz` — source distribution
- `dist/improve_cli-0.1.0-py3-none-any.whl` — installable wheel

Install the wheel locally:

```bash
pip install dist/improve_cli-0.1.0-py3-none-any.whl
```

## **Run without installing**

Clone the repo, create a venv if you like, and invoke the entry module directly:

```bash
python improve.py --help
```

## **Running the CLI**
- Basic help:

```bash
improve --help
# or: python improve.py --help
```

- Setup a user account (interactive):

```bash
improve setup --login
```

- Create a project:

```bash
improve project create MyProject
```

- Add an entry to a project:

```bash
improve project add-entry MyProject --day "Day 1" --date "2026-05-28" --progress "Started" --productivity "7" --feedback "Good start"
```

- List projects:

```bash
improve project list
```

- Show recent entries for a project:

```bash
improve project show MyProject --last 10
```

- Get recent feedback entries:

```bash
improve project feedback MyProject --last 5
```

- Export all tracking CSVs to `backup/`:

```bash
improve export
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
- Use `pip install -e .` and run `improve`, or run `python improve.py` without installing.
- Rebuild distributables with `python -m build` after packaging changes.
- The codebase is small and intended as a learning/demo project. Contributions or issues can be opened against the original upstream repository referenced in the code comments.


