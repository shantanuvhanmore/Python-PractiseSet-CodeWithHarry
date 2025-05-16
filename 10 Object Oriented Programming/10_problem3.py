class attri:
    a = 4
    def __init__(self):
        print(self.a) 
    
    def show(self):
        print(self.a)


object = attri
attri.show(object)
object.a = 0
print(object.a," f") 