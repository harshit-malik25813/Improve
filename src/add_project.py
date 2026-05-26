import csv
from pathlib import Path


def include(project: str):
    print("Adding a new project!")
    print("Did you know that most successful persons were experts at a lot of things!")
    tracking = Path("tracking")
    tracking.mkdir(parents=True, exist_ok=True)
    file_path = tracking / f"{project}.csv"
    with file_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Day", "Date", "Progress", "Productivity Level", "Feedback"])
    print("Track your progress every day and improve your consistency with Improve.")
    print(f"Project '{project}' has been created at {file_path}")
