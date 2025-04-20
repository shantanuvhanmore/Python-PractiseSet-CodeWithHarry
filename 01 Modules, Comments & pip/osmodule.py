import os

# Specify the directory path
directory_path = input("Enter the path of the directory: ")
# hello baborao aaj kau aal nay 
# this following code written with the help of the chatgpt 
# List and print the contents of the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
