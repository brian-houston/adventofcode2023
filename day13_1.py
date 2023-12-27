def convert_row_to_number(r, grid):
    ret = 0
    n = len(grid[r])
    for i in range(n):
        if grid[r][i] == '#':
            ret |= 2 ** (n - 1 - i)
    return ret

def convert_col_to_number(c, grid):
    ret = 0
    n = len(grid)
    for i in range(n):
        if grid[i][c] == '#':
            ret |= 2 ** (n - 1 - i)
    return ret

def check_mirror(i, arr):
    n = min(i, len(arr) - i)
    for j in range(n):
        if arr[i-1-j] != arr[i+j]:
            return False
    return True

grids = open('inputs/day13', 'r').read().split('\n\n') 
grids = [x.splitlines() for x in grids if x]

count = 0
for grid in grids:
    rows = [convert_row_to_number(i, grid) for i in range(len(grid))]
    cols = [convert_col_to_number(i, grid) for i in range(len(grid[0]))]
    for i in range(1, len(rows)):
        if check_mirror(i, rows):
            count += 100 * i
            break
    for i in range(1, len(cols)):
        if check_mirror(i, cols):
            count += i
            break

print(count)
