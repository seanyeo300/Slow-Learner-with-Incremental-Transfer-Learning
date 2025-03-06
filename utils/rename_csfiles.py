import os
import csv

# Define the root directory containing the WAV files in various subfolders
root_directory = r"F:\CochlScene\Test"

# Define the output CSV file
output_csv = r'cochl_test.csv'

# Create the CSV file and write the header
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    csvwriter.writerow(["filename", "scene_label", "identifier", "source_label"])

    # Walk through all subdirectories and files
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.wav'):
                # Extract the scene label, identifier, and source label from the filename
                parts = file.replace('.wav', '').split('_')
                
                # Construct the relative filename to start with 'audio/'
                relative_filename = os.path.join('audio', file).replace("\\", "/")
                
                # Extract scene_label, identifier, and source_label
                scene_label = parts[0]
                identifier = f"{parts[1]}_{parts[2]}"
                source_label = f"{parts[3]}"
                
                # Write the row to the CSV file
                csvwriter.writerow([relative_filename, scene_label, identifier, source_label])