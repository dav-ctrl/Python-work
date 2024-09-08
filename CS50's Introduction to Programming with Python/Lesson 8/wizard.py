class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self,name,house):
        super._init__(name)
        self.house

class Professor(Wizard):
    def __init__(self,name,subject):
        super.__init__(subject)
        self.subject

wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Defense Against the Dark Arts")


