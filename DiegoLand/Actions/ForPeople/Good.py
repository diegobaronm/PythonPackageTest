import DiegoLand.Person.Person as Person 

def Meet(person1 : Person.Person, person2 : Person.Person):
    print(person1.GetName(), " and ", person2.GetName(), " are meeting!")
    person1.SayHi()
    person2.SayHi()

def Kiss(person1 : Person.Person, person2 : Person.Person):
    print(person1.GetName(), " and ", person2.GetName(), " are kissing!")
    print(person1.GetName(), " says: 'I love you ",person2.GetName(),"!'")
    print(person2.GetName(), " says: 'I love you too!'")