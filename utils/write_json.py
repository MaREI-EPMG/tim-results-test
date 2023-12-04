import os
import json

# Path to the JSON file
json1_file_path = '../specs/scenarioTitles.json'
json2_file_path = '../specs/scenarios.json'

# Specify the folder path
folder_path = '../data'

# Function to get subfolder names in the given folder
def get_subfolder_names(folder_path):
    subfolder_names = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    return {name: name for name in subfolder_names}

# Function to update the JSON file
def update_json1(json1_file_path, subfolder_names):
    try:
        # Read existing JSON file
        with open(json1_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Add subfolder names to the JSON data
        data.update(subfolder_names)

        # Write the updated JSON back to the file
        with open(json1_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        print(f'Successfully updated {json1_file_path}')

    except Exception as e:
        print(f'Error updating JSON file: {e}')
        
        
def update_json2(json2_file_path, subfolder_names):
    try:
        # Read existing JSON file
        with open(json2_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Update the list of dictionaries
        updated_list = []
        for entry in data:
            if "name" in entry:
                name = entry["name"]
                variants = [{"name": name, "specs": None}]
                updated_list.append({"name": name, "variants": variants})

 
        # Add subfolder names to the list
        for key, value in subfolder_names.items():
            variants = [{"name": key, "specs": None}]
            updated_list.append({"name": key, "variants": variants})

        # Write the updated JSON back to the file
        with open(json2_file_path, 'w') as json_file:
            json.dump(updated_list, json_file, indent=2)

        print(f'Successfully updated {json2_file_path}')

    except Exception as e:
        print(f'Error updating JSON file: {e}')



# Get subfolder names
subfolder_names = get_subfolder_names(folder_path)

# Update the JSON file
update_json1(json1_file_path, subfolder_names)
update_json2(json2_file_path, subfolder_names)




