import os
import re

path = "files"  # The directory to rename
list_names = []
counter = 0

for file_name in os.listdir(path):
    if file_name != 'Renaming_audio.py':
        """ 
        If you need to delete a fixed number of characters:
        """
        # list_names.append(os.path.join(file_name[5:]))
        """
        If you need to completely clear the names of unnecessary characters:
        """
        list_names.append(
            (re.sub(r'[^\w\S]+|[\d]+', r' ', file_name).strip() + '3').replace('_', '', 1))


for item in os.listdir(path):
    if item != 'main.py':
        os.rename(os.path.join(path, item),
                  os.path.join(path, list_names[counter]))
        counter += 1

print('Renaming is complete!')
