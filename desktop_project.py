# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib

desktop = pathlib.Path() / "Desktop"

for file in desktop.iterdir():
    print(file)
