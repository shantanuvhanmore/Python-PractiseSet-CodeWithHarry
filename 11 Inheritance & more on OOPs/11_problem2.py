class animals:
    pass

class pets(animals):
    pass
class dogs(pets):
    @staticmethod
    def bark():
        print("woof woof!")
d = dogs()
d.bark()
    