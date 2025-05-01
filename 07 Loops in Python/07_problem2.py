# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.


l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in range(len(l)-1):
    if l[i][0] == "S":
        print("Hello", l[i]) 