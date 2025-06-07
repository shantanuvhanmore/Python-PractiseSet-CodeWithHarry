class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        real  = self.real * other.real - self.imaginary * other.imaginary
        img = self.real * other.imaginary + self.imaginary * other.imaginary
        return complex(real, img)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
c1 = complex(4,5)
c2 = complex(8,6)
c3 = complex(5,6)


print(c1 * c2)
print(c1 + c2)