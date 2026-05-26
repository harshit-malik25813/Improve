import shutil
from pathlib import Path


def export_data():
    tracking_folder = Path("tracking")
    if not tracking_folder.exists():
        print("No tracking folder found.")
        return

    csv_files = list(tracking_folder.glob("*.csv"))
    if not csv_files:
        print("You have not added any project to track!")
        print("No tracking data to export")
        print("Exiting now!")
        return

    destination_folder = Path("backup")
    destination_folder.mkdir(parents=True, exist_ok=True)

    for csv_file in csv_files:
        shutil.copy2(csv_file, destination_folder / csv_file.name)

    print("Export was successful!")
    print("Find your exported progress in CSV format in:\n" \
          f"{destination_folder.resolve()}")
    return