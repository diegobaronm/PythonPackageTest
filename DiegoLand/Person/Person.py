import DiegoLand.World.World as World

class Person:
    def __init__(self, name, age, sex):
        self.m_name = name
        self.m_age = age
        self.m_sex = sex
        World.WORLD.AddPerson(self)

    def Display(self):
        print("Name: ", self.m_name)
        print("Age: ", self.m_age)
        print("Sex: ", self.m_sex)

    # Setters
    def SetName(self, name):
        self.m_name = name
    def SetAge(self, age):
        self.m_age = age
    def SetSex(self, sex):
        self.m_sex = sex

    # Getters
    def GetName(self):
        return self.m_name
    def GetAge(self):
        return self.m_age
    def GetSex(self):
        return self.m_sex
    
    # Personal Actions
    def Birthday(self):
        self.m_age += 1

    def ChangeName(self ,name : str):
        self.SetName(name)

    def SayHi(self):
        print("Hi! My name is ", self.m_name, "\n")


if __name__ == "__main__":
    print("This is the Person module, this code should not be executed directly.")