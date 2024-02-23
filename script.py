import os
import re

# Directory containing the .py files
# Ensure to replace this with the directory path you are working with
directory_path = "telnyx/api_resources"

# Regular expressions to match class lines
class_line_regex = re.compile(r"^class (\w+)\(")

for filename in os.listdir(directory_path):
    if filename.endswith(".py"):
        with open(os.path.join(directory_path, filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                class_search = class_line_regex.search(line)
                if class_search:
                    # Extract the class name
                    class_name = class_search.group(1)
                    # Construct the template statement
                    template_statement = (
                        f"from telnyx.api_resources.{filename[:-3]} import {class_name}"
                    )
                    print(template_statement)
                    # Assuming only one class per file as per the given context
                    break
