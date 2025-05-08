cuss_words = ["lavdya","zavadya","bullya","kelya","bhenchod","madarchod"]

for word in cuss_words:
    with open("uncencored.txt", "r") as f:
        text = f.read()
        new = text.replace(word,"#"*len(word))
    with open("uncencored.txt", "w") as f:
        f.write(new)
