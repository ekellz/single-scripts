# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib
import json
from collections import Counter
from datetime import datetime

db_path = pathlib.Path('Users/ericajansen/Docume')
# Desktop path
desktop = pathlib.Path() / "Desktop"

for file in desktop.iterdir():
    print(file)
