import DiegoLand.Person.Person as Person

class World():
    def __init__(self, name, weather, time : int) -> None:
        self.m_name = name
        self.m_weather = weather
        self.m_time = time
        self.m_listOfPeople = []

    def Display(self):
        print("Name: ", self.m_name)
        print("Weather: ", self.m_weather)
        print("Time: ", self.m_time)
        print("People in this world: ")
        for person in self.m_listOfPeople:
            print(person.GetName())

    # Setters
    def SetName(self, name):
        self.m_name = name
    def SetWeather(self, weather):
        self.m_weather = weather
    def SetTime(self, time):
        self.m_time = time
    
    # Getters
    def GetName(self):
        return self.m_name
    def GetWeather(self):
        return self.m_weather
    def GetTime(self):
        return self.m_time % 24
    
    # World Actions
    def AddPerson(self, person : Person.Person):
        self.m_listOfPeople.append(person)
    
WORLD = World("Earth", "Sunny", 12)
    
if __name__ == "__main__":
    print("This is the World module, this code should not be executed directly.")