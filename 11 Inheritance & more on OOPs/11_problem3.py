class Employee:
    salary = 1000000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100


e = Employee()
e.salaryAfterIncrement = 1200000
print(e.increment)
print(e.salaryAfterIncrement)