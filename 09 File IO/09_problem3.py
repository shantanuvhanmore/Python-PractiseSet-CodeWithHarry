import os

folder_path = r'C:\Users\shant\OneDrive\Desktop\codes\python\chapter 9 - ps\13 - years old'
for i in range(2,21):
    file_path = os.path.join(folder_path,f"table_of_{i}.txt")
    with open(file_path, 'w') as f:
        f.write(f"Table of {i}\n")
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")
