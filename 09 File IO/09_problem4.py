with open("uncencored.txt", "r") as f:
    text = f.read()
    update_text = text.replace("Donkey", "#####")
    print(update_text)

with open("uncencored.txt", "w") as f:
    f.write(update_text)
    print(update_text)
