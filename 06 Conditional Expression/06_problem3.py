# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams
str = input("Enter the message: ")

if((str.count("Make a lot of money") > 0) or (str.count("buy now") > 0) or (str.count("subscribe now") > 0) or (str.count("click this") > 0)):
    print("spam1 has detected")
else:
    print("not found !!")



print(str.find("buy now"))
print(str.count("buy now"))