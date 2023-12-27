import numpy as np

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def between(v, a, b):
    return v >= a and v <= b

min_coord = 200000000000000
max_coord = 400000000000000
def does_intersect(h1, h2):
    denom = cross(h1.velocity_xy, h2.velocity_xy)
    if denom == 0:
        return False
    u = cross(h2.position_xy - h1.position_xy, h2.velocity_xy) / denom
    v = cross(h2.position_xy - h1.position_xy, h1.velocity_xy) / denom
    if u < 0 or v < 0:
        return False

    inter = h1.position_xy + h1.velocity_xy * u 
    if between(inter[0], min_coord, max_coord) and between(inter[1], min_coord, max_coord):
        return True
    return False
    

class Hail:
    def __init__(self, line):
        position, velocity = line.split('@')
        self.position = np.array([int(x) for x in position.split(',')])
        self.velocity = np.array([int(x) for x in velocity.split(',')])
        self.position_xy = self.position[0:2]
        self.velocity_xy = self.velocity[0:2]

lines = []
with open('inputs/day24', 'r') as file:
    lines = file.read().splitlines()

hailstones = [Hail(x) for x in lines]

count = 0
n = len(hailstones)
for i in range(n):
    for j in range(i + 1, n):
        if does_intersect(hailstones[i], hailstones[j]):
            count += 1
print(count)
