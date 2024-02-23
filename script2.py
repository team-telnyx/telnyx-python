import os
import re

# Directory containing the .py files
# Ensure to replace this with the directory path you are working with
directory_path = "telnyx/api_resources"

# Regular expressions to match class lines
class_line_regex = re.compile(r"^class (\w+)\(")

# List to collect all class names
class_names = []

for filename in os.listdir(directory_path):
    if filename.endswith(".py"):
        with open(os.path.join(directory_path, filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                class_search = class_line_regex.search(line)
                if class_search:
                    # Extract the class name
                    class_name = class_search.group(1)
                    # Add the class name to the list
                    class_names.append(class_name)
                    # Assuming one class of interest per file, but you can remove break for multiple
                    break

# Sort the list of class names
class_names.sort()

# Print the sorted class names in the desired format
for class_name in class_names:
    print(f'"{class_name}",')
