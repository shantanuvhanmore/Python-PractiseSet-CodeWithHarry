# Write a program to print the following star pattern.
#   *     i = 1
#  ***    i = 2   n = 3
# *****   i = 3
n = int(input("Enter number:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
