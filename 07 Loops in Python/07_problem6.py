# Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter the number "))
l =[]

total = 1
for i in range(n,0,-1):
    l.append(i)
for i in l:
    total = total * i

print(total)