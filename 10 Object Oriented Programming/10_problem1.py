class programmers:
    global name,skills,years_of_experience
    def __init__(self, name, skills, years_of_experience):
        self.name = name
        self.skills =  skills
        self.years_of_experience = years_of_experience
    def print_info(self):
        return "name = "+str(self.name)+"\nskills = "+str(self.skills)+"\nyears_of_experienece = "+str(self.years_of_experience)
    
harry = programmers("harry","java",20)

print(harry.print_info())