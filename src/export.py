import shutil
from pathlib import Path

# To export user tracking data to a CSV file
def export_data():
    tracking_folder = Path("tracking") 
    if not tracking_folder.exists(): # If user exports data but the folder doesnt contain any
        print("No tracking data found.") 
        return

    csv_files = list(tracking_folder.glob("*.csv")) # Creating a list of files in the folder

    destination_folder = Path("backup") # Creating a folder called backup to copy the tracked CSV files
    destination_folder.mkdir(parents=True, exist_ok=True)

    for csv_file in csv_files:
        shutil.copy2(csv_file, destination_folder / csv_file.name)

    print("Export was successful!")
    print("Find your exported progress in CSV format in:\n" \
          f"{destination_folder.resolve()}")
    print("You can still continue with your progress as it hasnt been deleted")
    return
