import os

directory_path = r'C:\Users\Amanat Ali\Downloads\July-December 2026\Python'      # or any directory path

contents = os.listdir(directory_path)

for item in contents:
    print(item)