with open("copy.txt" , "r") as f:
    content2 = f.read()

with open("re_copy.txt" , "r") as f:
    content1 = f.read()

if content1 == content2:
    print("The contents of both files are identical.")
else:
    print("The contents of both files are not identical.")