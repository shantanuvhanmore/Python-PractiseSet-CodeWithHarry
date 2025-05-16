import math
class calculator:
    def __init__(self,n):
        self.n = n

    def square(self,n):
        return self.n * self.n
    
    def cube(self, n):
        return self.n * self.n * self.n
    
    def squareroot(self,n):
        return math.sqrt(self.n)
    
    def show(self):
        print(f"Square: {self.square(self.n)}\nCube: {self.cube(self.n)}\nSquare Root: {self.squareroot(self.n)}")

    @staticmethod 
    def greet ():
        print("Hello, I am a Calculator!")


num1 = calculator(9)
num1.greet()

num1.show()
