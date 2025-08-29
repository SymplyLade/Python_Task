# This is how it works
# Using os.getcwd()

import os

# Get the current working directory

print("Current working directory:", os.getcwd())

# Ensure to check the output

# Absolute path example
absolute_path = r"C:\Users\user133\Desktop"

# Relative path example
relative_path = "my_path.py"

print("Absolute Path:", absolute_path)
print("Relative Path:", relative_path)

# Joining paths(The Right way)
import os 

folder = r"C:\Users\user133\Desktop"
filename = "my_path.py"

path = os.path.join(folder, filename)
print("Full path:", path)


# 4. Checking if a file or folder exists

import os 
path = "my_path.py"
if os.path.exists(path):
    print("Yes, the file exists!")
else:
    print("File not found.")

# 5. Using pathlib (Modern Way)
from pathlib import Path
# Current working directory
print("Current directory:", Path.cwd())
# Create a Path object
file = Path("myfile.txt")
# Check if it exists
print("File exists:", file.exists())
# Combine paths
folder = Path("C:/Users/user133/Desktop")
full_path = folder / "myfile.txt"
print("Full path:", full_path)

# 6. Navigating Folder with pathlib
from pathlib import Path
# Get parent folder of current file
print("Parent folder:", Path.cwd().parent)
# List all files in a directory 
for file in ath.cwd().iterdir():
    print(file) 