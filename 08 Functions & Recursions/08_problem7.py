def rem(l,word):
    f = []
    for item in l:
        if item != word:
            f.append(item.strip(word))
    return f

L = ["shrau","abhay","bunty","asur","s"]
word = "s"
print(rem(L,word))

