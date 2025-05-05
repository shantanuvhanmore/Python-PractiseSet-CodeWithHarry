# sum of n nutural numbers
@staticmethod
def SumNnatural(n):
    sum = 0
    i = n
    while(i>0):
        sum = sum + i
        i = i - 1
    print(f"The sum of first {n} natural numbers is {sum}")
n = int(input("Enter the \'n\': "))
SumNnatural(n)