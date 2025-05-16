from random import randint
class train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
        
    def book(self,fro,to):
        print(f"you ticket reservation for {self.trainNo} has sucessfully booked from {fro} to {to}")

    def status(self):
        print(f"your train number is {self.trainNo} ")

    def fare(self):
        print(f"train {self.trainNo} running under Indian Railways.")

koyna = train(randint(444444,999999))

koyna.status()

koyna.book("pune","miraj")

koyna.fare()