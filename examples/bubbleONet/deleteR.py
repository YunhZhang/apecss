import os
import shutil

# Set the path to the 'results' folder
results_folder = "path/to/results"

# Iterate over all subfolders in the 'results' folder
for folder_name in os.listdir(results_folder):
    # Check if 'R0_1e-5' is in the folder name
    if "R0_1e-5" in folder_name:
        # Create the full path of the folder to be removed
        folder_path = os.path.join(results_folder, folder_name)
        # Remove the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Removed folder: {folder_path}")
