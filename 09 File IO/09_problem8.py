with open("copy.txt" , "r") as f:
    content = f.read()

with open("re_copy.txt" , "w") as f:
    f.write(content)
