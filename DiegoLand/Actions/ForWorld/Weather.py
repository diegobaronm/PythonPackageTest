import DiegoLand.World.World as World

def Rain(world : World.World):
    world.SetWeather("Rain")
    print("It's raining!\n")

def Snow(world : World.World):
    world.SetWeather("Snow")
    print("It's snowing!\n")