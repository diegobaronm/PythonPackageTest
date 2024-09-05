import DiegoLand.World.World as World
import DiegoLand.Person.Person as Person
import DiegoLand.Actions.ForPeople.Bad as BadActions
import DiegoLand.Actions.ForPeople.Good as GoodActions
import DiegoLand.Actions.ForWorld.Weather as WeatherActions
import DiegoLand.Actions.ForWorld.Time as TimeActions

def main():
    diego = Person.Person("Diego",31,"M")
    giz = Person.Person("Giz", 31, "F")

    diego.Display()
    giz.Display()

    diego.SayHi()
    giz.Birthday()

    World.WORLD.Display()

    print("It's ", World.WORLD.GetTime(), " o'clock")
    print("The weather is ", World.WORLD.GetWeather())

    giz.Display()

    GoodActions.Meet(diego, giz)
    GoodActions.Kiss(diego, giz)

    BadActions.Fight(diego, giz)
    

    World.WORLD.Display()
    TimeActions.Sunrise(World.WORLD)
    WeatherActions.Rain(World.WORLD)

    World.WORLD.Display()
    TimeActions.AdvaceHours(World.WORLD, 5)
    World.WORLD.Display()

    WeatherActions.Snow(World.WORLD)
    TimeActions.Sunset(World.WORLD)
    World.WORLD.Display()


    return 0


if __name__ == "__main__":
    main()