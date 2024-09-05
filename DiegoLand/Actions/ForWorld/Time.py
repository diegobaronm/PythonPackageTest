import DiegoLand.World.World as World

def Sunrise(world : World.World):
    world.SetTime(8)
    print("The sun is rising! It's morning!\n")

def Sunset(world : World.World):
    world.SetTime(18)
    print("The sun is setting! It's evening!\n")

def AdvaceHours(world : World.World, hours : int):
    world.SetTime(world.GetTime() + hours)
    print("Time has advanced ", hours, " hours\n")