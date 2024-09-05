import DiegoLand.Person.Person as Person

def Fight(person1 : Person.Person, person2 : Person.Person):
    print(person1.GetName(), " and ", person2.GetName(), " are fighting!")
    print(person1.GetName(), " says: 'I hate you ",person2.GetName(),"!'")
    print(person2.GetName(), " says: 'I hate you too!'")
    print("The fight is over! ", person1.GetName(), " won!\n")
    return 0