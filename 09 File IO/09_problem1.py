


f = open("poem.txt", "r")
text = f.read()
if "twinkle" in text:
    print("FILE 'poem.txt' CONTAIN 'twinkle'")
else:
    print("FILE 'poem.txt' DOES NOT CONTAIN 'twinkle'")

f.close()
