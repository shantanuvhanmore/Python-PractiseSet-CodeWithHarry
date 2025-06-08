


list1 =[]
n = int(input("Enter the for table: "))
list2 = [str(i*n) for i in range(1,11)]

with open("tables.txt","a") as f:
    f.write(f"Table of {n}:\n")
    f.write("\n".join(list2))