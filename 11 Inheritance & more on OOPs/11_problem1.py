class twoDvector:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: {self.x}x {self.y}y")
        

class threeDvector(twoDvector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def show(self):
        print(f"Coordinates: {self.x}x {self.y}y {self.z}z")



twoD = twoDvector(2,3)
twoD.show()
threeD = threeDvector(2,3,5)
threeD.show()
