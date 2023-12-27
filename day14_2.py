import numpy

def count_load(grid):
    load = 0
    n = len(grid)
    for x in range(n):
        for y in range(n):
            symbol = grid[y][x]
            if symbol == 'O':
                load += n - y
    return load

def tilt(grid):
    n = len(grid)
    for x in range(n):
        next = 0
        for y in range(n):
            symbol = grid[y][x]
            if symbol == '#':
                next = y + 1   
            elif symbol == 'O':
                grid[y][x] = '.'
                grid[next][x] = 'O'
                next += 1

grid = open('inputs/day14', 'r').read().splitlines() 
grid = [list(x) for x in grid]
loads = [0]
for i in range(200):
    tilt(grid)
    grid = numpy.rot90(grid, k=-1)
    tilt(grid)
    grid = numpy.rot90(grid, k=-1)
    tilt(grid)
    grid = numpy.rot90(grid, k=-1)
    tilt(grid)
    grid = numpy.rot90(grid, k=-1)
    loads.append(count_load(grid))

window = 5 
lookup = {}
for i in range(len(loads) - window):
    key = tuple(loads[i:i+window])
    if key in lookup:
        cycle = i - lookup[key] 
        offset = (1_000_000_000 - i) % cycle
        print(loads[i + offset])
        break
    lookup[key] = i
