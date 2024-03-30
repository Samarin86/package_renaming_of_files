import os
import re

path = "files"  # The directory to rename
list_names = []
counter = 0

for file_name in os.listdir(path):
    if file_name != 'Renaming_audio.py':
        # list_names.append(os.path.join(file_name[5:]))
        list_names.append(re.findall(r'\w', file_name))

print(list_names)

# for item in os.listdir(path):
#     if item != 'Renaming_audio.py':
#         os.rename(os.path.join(path, item),
#                   os.path.join(path, list_names[counter]))
#         counter += 1

print('Переименование завершено!')
