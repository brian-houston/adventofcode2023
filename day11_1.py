grid = open('inputs/day11', 'r').read().split('\n') 
grid = [x for x in grid if x]

width = len(grid[0])
height = len(grid)
empty_rows = [True for _ in range(height)]
empty_cols = [True for _ in range(width)]
galaxies = []
for y in range(height):
    for x in range(width):
        if grid[y][x] == '#':
            empty_cols[x] = False
            empty_rows[y] = False
            galaxies.append((x, y))

empty_rows = [i for i, b in enumerate(empty_rows) if b]
empty_cols = [i for i, b in enumerate(empty_cols) if b]

def between(v, a, b):
    return (v > a and v < b) or (v < a and v > b)

def distance(a, b):
    ret = abs(b[0] - a[0]) + abs(b[1] - a[1])
    for x in empty_cols:
        if between(x, a[0], b[0]):
            ret += 1
    for y in empty_rows:
        if between(y, a[1], b[1]):
            ret += 1
    return ret

total = 0
ngal = len(galaxies)
for i in range(ngal):
    for j in range(i+1, ngal):
        total += distance(galaxies[i], galaxies[j])
print(total)
