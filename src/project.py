import csv
from pathlib import Path
from typing import List

TRACKING = Path("tracking")
HEADER = ["Day", "Date", "Progress", "Productivity Level", "Feedback"]


def _project_file(name: str) -> Path:
    TRACKING.mkdir(parents=True, exist_ok=True)
    return TRACKING / f"{name}.csv"


def list_projects() -> List[str]:
    if not TRACKING.exists():
        print("No projects found.")
        return []
    projects = [p.stem for p in TRACKING.glob("*.csv")]
    if not projects:
        print("No projects found.")
        return []
    print("Projects:")
    for p in projects:
        print(f" - {p}")
    return projects


def create_project(name: str) -> Path:
    path = _project_file(name)
    if path.exists():
        print(f"Project '{name}' already exists at {path}")
        return path
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
    print(f"Project '{name}' created at {path}")
    return path


def add_entry(name: str, day: str = "", date: str = "", progress: str = "", productivity: str = "", feedback: str = ""):
    path = _project_file(name)
    if not path.exists():
        print(f"Project '{name}' does not exist. Creating it now.")
        create_project(name)
    row = [day, date, progress, productivity, feedback]
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print(f"Added entry to project '{name}'.")


def get_feedback(name: str, last: int = 5):
    path = _project_file(name)
    if not path.exists():
        print(f"Project '{name}' not found.")
        return
    with path.open("r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
    feedbacks = [r.get("Feedback", "") for r in reader if r.get("Feedback")]
    if not feedbacks:
        print("No feedback entries found.")
        return
    print(f"Last {last} feedback entries for '{name}':")
    for fb in feedbacks[-last:]:
        print(f" - {fb}")


def show_project(name: str, last: int = 10):
    path = _project_file(name)
    if not path.exists():
        print(f"Project '{name}' not found.")
        return
    with path.open("r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
    if not reader:
        print("No entries yet.")
        return
    rows = reader[-last:]
    print(f"Showing last {len(rows)} entries for '{name}':")
    for r in rows:
        print(f"Day: {r.get('Day','')}, Date: {r.get('Date','')}, Progress: {r.get('Progress','')}, Productivity: {r.get('Productivity Level','')}, Feedback: {r.get('Feedback','')}")


def delete_project(name: str):
    path = _project_file(name)
    if not path.exists():
        print(f"Project '{name}' not found.")
        return
    path.unlink()
    print(f"Project '{name}' deleted.")
