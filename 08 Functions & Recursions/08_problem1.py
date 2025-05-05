@staticmethod
def greatestOfThree(a,b,c):
    if((a>b) and (a>c)):
        print(f"{a} is Greatest among three")
    elif((b>a)and (b>c)):
        print(f"{b} is Greatest among three")
    else:
        print(f"{c} is Greatest among three")


a = int(input("Enter number one:"))
b = int(input("Enter number two:"))
c = int(input("Enter number third:"))

greatestOfThree(a,b,c)
