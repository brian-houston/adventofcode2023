grid = []
with open('inputs/day21', 'r') as file:
    grid = file.read().splitlines()

directions = [(1,0), (-1,0), (0, 1), (0,-1)]
width = len(grid[0])
height = len(grid)
start = (-1, -1)
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'S':
            start = (x, y)

prev = set()
prev.add(start)
for i in range(64):
    curr = set()
    for coord in prev:
        for d in directions:
            new = (coord[0] + d[0], coord[1] + d[1])
            if new[0] >= 0 and new[0] < width and new[1] >= 0 and new[1] < height and grid[new[1]][new[0]] != '#':
                curr.add(new)
    prev = curr
print(len(prev))
