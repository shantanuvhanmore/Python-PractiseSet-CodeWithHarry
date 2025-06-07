class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
        
    def __str__(self):
        return f"{self.x} + {self.y} + {self.z}"
    
c1 = vector(4,5,5)
c2 = vector(8,6,6)
c3 = vector(5,6,5)


print(c1 * c2)
print(c1 + c2)