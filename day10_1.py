direction_lookup = {
        'north': (0,-1),
        'east': (1,0),
        'south': (0,1),
        'west': (-1,0),
        }

symbol_lookup = {
        'S': None,
        '.': None,
        '|': {
            'north': 'north',
            'south': 'south'
            },
        '-': {
            'east': 'east',
            'west': 'west'
            },
        'F': {
            'north': 'east',
            'west': 'south'
            },
        'L': {
            'south': 'east',
            'west': 'north'
            },
        'J': {
            'south': 'west',
            'east': 'north'
            },
        '7': {
            'north': 'west',
            'east': 'south'
            },
        }

def add_points(a, b):
    return (a[0] + b[0], a[1] + b[1])

grid = open('inputs/day10', 'r').read().split('\n') 
grid = [x for x in grid if x]

start_pos = None
for y, row in enumerate(grid):
    x = row.find('S')
    if x >= 0:
        start_pos = (x, y)
        break

curr = [start_pos, start_pos]
dir = ['north', 'west']
step = 0
while True:
    for i in range(len(dir)):
        curr[i] = add_points(curr[i], direction_lookup[dir[i]])
        x = curr[i][0]
        y = curr[i][1]
        dir[i] = symbol_lookup[grid[y][x]][dir[i]]
    step += 1
    if curr[0] == curr[1]:
        break
print(step)
