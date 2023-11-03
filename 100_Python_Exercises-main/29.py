import math

radius = 10
h = 2
volume = ((4 * math.pi * pow(radius, 3)) / 3) - (
    (math.pi * pow(h, 2) * (3 * radius - h)) / 3
)

print(volume)
