# IBN (AMDG) 3/4/2022

def build_vehicle(wheels, axels, doors, color):
    return "The car has {0} wheels, {1} axels, {2} doors and is the color {3}.".format(wheels, axels, doors, color)


wheels = input("How many wheels does the car have? ")
axels = input("How many axels does the car have? ")
doors = input("How many doors does the car have? ")
color = input("What color is the car? ")
print(build_vehicle(wheels, axels, doors, color))
