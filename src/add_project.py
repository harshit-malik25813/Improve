import csv
def include(project):
    print("Adding a new project!")
    print("Did you know that most successful persons were experts at a lot of things!")
    with open(f"{project}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Day", "Date", "Progress", "Productivity Level", "Feedback"])
    print("Track your progress every day and improve your consistency with Improve.")
    print(f"Project '{project}' has been created!")
