import csv
from pathlib import Path

# To add a project to track progress of
def include(project: str): # Defining a function
    print("Adding a new project!")
    print("Did you know that most successful persons were experts at a lot of things!")
    tracking = Path("tracking") # checking the tracking file path
    if not tracking.exists():
         tracking.mkdir(parents=True, exist_ok=True) # Making a directory for tracking projects if it doesnt exist
    file_path = tracking / f"{project}.csv" # Path to the CSV file to be used to track the user's progress
    with file_path.open("w", newline="", encoding="utf-8") as f: # Writing headers for the tracking
        writer = csv.writer(f)
        writer.writerow(["Day", "Date", "Progress", "Productivity Level", "Feedback"])
    print("Track your progress every day and improve your consistency with Improve.")
    print(f"Project '{project}' has been created at {file_path}")
