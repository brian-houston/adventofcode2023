grid = []
with open('inputs/day21', 'r') as file:
    grid = file.read().splitlines()
    grid = [list(row) for row in grid]

directions = [(1,0), (-1,0), (0, 1), (0,-1)]
size = len(grid)
goal = 26501365 
prev = set()
for y in range(size):
    for x in range(size):
        if grid[y][x] == 'S':
            prev.add((x, y))

counts = []
for i in range(0, 328):
    curr = set()
    for x, y in prev:
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if grid[ny % size][nx % size] != '#':
                curr.add((nx, ny))
    if i % size == goal % size:
        counts.append(len(prev))
    prev = curr

def calc_plots(n):
    return counts[0] + n * (counts[1] - counts[0]) + (counts[2] - 2 * counts[1] + counts[0]) * n * (n-1) / 2

print(calc_plots(goal//size))
