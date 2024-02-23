import os
import re

# Directory containing the .py files
# Ensure to replace this with the directory path you are working with
directory_path = "telnyx/api_resources"

# Regular expressions to match class lines
class_line_regex = re.compile(r"^class (\w+)\(")

# Initializing a list to collect all template statements
template_statements = []

for filename in os.listdir(directory_path):
    if filename.endswith(".py"):
        with open(os.path.join(directory_path, filename), "r") as file:
            lines = file.readlines()
            for line in lines:
                class_search = class_line_regex.search(line)
                if class_search:
                    # Extract the class name
                    class_name = class_search.group(1)
                    # Construct the new template statement
                    template_statement = f"api_resources.{class_name}.OBJECT_NAME: api_resources.{class_name},"
                    # Instead of printing, append the statement to the list
                    template_statements.append(template_statement)
                    # Assuming only one class per file based on the given context
                    break

# Sort the list of template statements alphabetically
template_statements.sort()

# Print the sorted statements
for statement in template_statements:
    print(statement)
