import shutil # Importing shutil library to copy the CSV file
from pathlib import Path # Using the pathlib library to check whether a csv file exists
def export_data():
    tracking_folder = Path("tracking")
    tracked_data = any(tracking_folder.glob("*.csv"))
    if not tracked_data:
        print("You have not added any project to track!")
        print("No tracking data to export")
        print("Exiting now!")
        return
    else:
        source = Path("tracking/*.csv")
        destination_folder = Path("backup/")
        # Creating folder
        destination_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, destination_folder)
        print("Export was successful!")
        print("Find your exported progress in CSV format in: \n" \
        f"{destination_folder.resolve()}")
        return