direction_lookup = {
        'north': (0,-1),
        'east': (1,0),
        'south': (0,1),
        'west': (-1,0),
        }


symbol_lookup = {
        'S': {'east': 'north'},
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

class Edge:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.winding = 1 if direction == 'north' else -1

    def __repr__(self):
        return f'{self.x} {self.y} {self.winding}'

def is_vertical(d):
    return d == 'north' or d == 'south'

grid = open('inputs/day10', 'r').read().split('\n') 
grid = [x for x in grid if x]

start_pos = None
for y, row in enumerate(grid):
    x = row.find('S')
    if x >= 0:
        start_pos = (x, y)
        break

curr = start_pos
dir = 'north' 
vdir = 'north'
edges = []
while True:
    curr = add_points(curr, direction_lookup[dir])
    x = curr[0]
    y = curr[1]
    symbol = grid[y][x] 
    dir = symbol_lookup[symbol][dir]
    if is_vertical(dir):
        vdir = dir
    edges.append(Edge(x, y, vdir))
    if curr == start_pos:
        break

# winding draw
sum = 0
for y in range(len(grid)):
    active_edges = [e for e in edges if e.y == y]
    active_edges.sort(key = lambda e: e.x)
    n = len(active_edges)
    winding = 0
    i = 0
    while i < n:
        e = active_edges[i]
        x = e.x

        # treat consecutive active edges as single block
        while i + 1 < n and x + 1 == active_edges[i+1].x:
            i += 1
            x += 1
        if e.winding == active_edges[i].winding:
            winding += e.winding

        # inside path when winding is nonzero
        if i + 1 < n and winding != 0:
            sum += active_edges[i+1].x - active_edges[i].x - 1
        i += 1
    
print(sum)
