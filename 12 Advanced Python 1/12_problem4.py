def divide(a,b):
    try:
        result = a/b
        print(f"{a}/{b}= {result}")
    except Exception as e:
        print("infinite by handling the ‘ZeroDivisionError’")

A = int(input("Enter the A: "))
B = int(input("Enter the B: "))
divide(A,B)