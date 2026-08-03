import os
# Select the path of the directory you want to list the contents of. You can change the path in the `directory_path` variable.
directory_path = r'C:\Users\Amanat Ali\Downloads\July-December 2026\Python'      # or any directory path
# Use the OS module to list the contents of the specified directory.
contents = os.listdir(directory_path)

for item in contents:
    print(item)