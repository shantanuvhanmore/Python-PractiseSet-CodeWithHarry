# Write a program to find the greatest of four numbers entered by the user.
a1 =int(input("Enter number :"))
a2 =int(input("Enter number :"))
a3 =int(input("Enter number :"))
a4 =int(input("Enter number :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("THe greatest amongst four:",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("THe greatest amongst four:",a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("THe greatest amongst four:",a3)
else:
    print("THe greatest amongst four:",a4)
