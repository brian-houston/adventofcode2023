import numpy as np

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def intersect(h1, h2):
    denom = cross(h1.velocity[0:2], h2.velocity[0:2])
    u = cross(h2.position[0:2] - h1.position[0:2], h2.velocity[0:2]) / denom
    v = cross(h2.position[0:2] - h1.position[0:2], h1.velocity[0:2]) / denom

    inter = h1.position + h1.velocity * u
    return inter.astype(int)
    
class Hail:
    def __init__(self, line):
        position, velocity = line.split('@')
        self.position = np.array([int(x) for x in position.split(',')], dtype=np.longdouble)
        self.velocity = np.array([int(x) for x in velocity.split(',')], dtype=np.longdouble)

lines = []
with open('inputs/day24', 'r') as file:
    lines = file.read().splitlines()

hailstones = [Hail(x) for x in lines]

count = 0
n = len(hailstones)

search_size = 1000 

init_vels = set(range(-search_size, search_size))
vel_sets = [init_vels, init_vels.copy(), init_vels.copy()]

for i in range(n):
    for j in range(i + 1, n):
        for k in np.argwhere(hailstones[i].velocity == hailstones[j].velocity):
            diff = hailstones[i].position[k] - hailstones[j].position[k]
            possible = set()
            for l in vel_sets[k[0]]:
                v = hailstones[i].velocity[k] - l
                if v != 0 and diff % v == 0:
                    possible.add(l)
            vel_sets[k[0]] = possible

rock_vel = np.array([list(x)[0] for x in vel_sets])
hailstones[0].velocity -= rock_vel
hailstones[1].velocity -= rock_vel

inter = intersect(hailstones[0], hailstones[1])
print(sum(inter))
