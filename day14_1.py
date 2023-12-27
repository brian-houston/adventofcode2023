def count_load(x, grid):
    load = 0
    start = 0 
    n = len(grid)
    for y in range(n):
        symbol = grid[y][x]
        if symbol == '#':
            start = y + 1
        elif symbol == 'O':
            load += n - start
            start += 1
    return load

grid = open('inputs/day14', 'r').read().splitlines() 
load = 0
for x in range(len(grid[0])):
    load += count_load(x, grid)
print(load)
