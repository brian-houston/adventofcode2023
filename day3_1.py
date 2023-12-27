grid = open('inputs/day3', 'r').read().split('\n') 
grid = [x for x in grid if x]

width = len(grid[0]) 
height = len(grid)

def clamp(v, small, big):
    return max(small, min(v, big))

def parse_part_num(left, right, y):
    part_num = int(grid[y][left:right])
    left_bound = clamp(left - 1, 0, width - 1)
    right_bound = clamp(right, 0, width - 1)
    top_bound = clamp(y - 1, 0, height - 1)
    bottom_bound = clamp(y + 1, 0, height - 1)
    for y in range(top_bound, bottom_bound+1):
        for x in range(left_bound, right_bound+1):
            v = grid[y][x]
            if v != '.' and not v.isdigit():
                return part_num 
    return 0

sum = 0
start = -1 
for y in range(height):
    for x in range(width):
        v = grid[y][x]
        if start < 0 and v.isdigit():
            start = x

        if start >= 0 and not v.isdigit():
            sum += parse_part_num(start, x, y)
            start = -1
    if start >= 0:
        sum += parse_part_num(start, width, y)
        start = -1

print(sum)
