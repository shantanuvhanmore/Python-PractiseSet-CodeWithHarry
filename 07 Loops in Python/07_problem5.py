# Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter the number "))
l = []

for i in range(1,n+1):
    l.append(i)
print(sum(l))
