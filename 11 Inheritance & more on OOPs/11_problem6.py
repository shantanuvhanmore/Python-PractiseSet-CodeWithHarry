class vector:
    def __init__(self,l):
        self.l = l


    def __len__(self):
        return len(self.l)
    
c1 = vector([4,5,5])
c2 = vector([8,6,6])

print(len(c1))