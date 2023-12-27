dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
grid = []
junctions = {}

def count_num_paths(x, y):
    count = 0
    for i in range(4):
        if grid[y + dy[i]][x + dx[i]] != '#':
            count += 1
    return count

def distance_to_next_junction(x, y, direction):
    distance = 1
    prev = (x, y)
    curr = (x + 1, y) if direction == '>' else (x, y + 1)
    if grid[curr[1]][curr[0]] == '#':
        return None, -1

    while curr not in junctions:
        distance += 1
        for i in range(4):
            next = (curr[0] + dx[i], curr[1] + dy[i])
            if grid[next[1]][next[0]] != '#' and next != prev:
                prev = curr
                curr = next
                break

    return curr, distance

with open('inputs/day23', 'r') as file:
    grid = file.read().splitlines()

width = len(grid[0])
height = len(grid)

start = (1, 0)
end = (width - 2, height - 1)
junctions[start] = {}
junctions[end] = {}
for y in range(1, height - 1):
    for x in range(1, width - 1):
        if grid[y][x] != '#' and count_num_paths(x, y) != 2:
            junctions[(x, y)] = {}

for j in junctions.keys():
    if j == end:
        continue
    down_j, down_dist = distance_to_next_junction(j[0], j[1], 'v') 
    right_j, right_dist = distance_to_next_junction(j[0], j[1], '>') 
    if down_j:
        junctions[j][down_j] = down_dist
        junctions[down_j][j] = down_dist
    if right_j:
        junctions[j][right_j] = right_dist
        junctions[right_j][j] = right_dist

best = 0
def dfs(curr, visited, dist):
    global best
    if curr == end and dist > best:
        best = dist
    for next, ndist in junctions[curr].items():
        if next not in visited:
            visited.add(curr)
            dfs(next, visited, dist + ndist)
            visited.remove(curr)

dfs(start, set([start]), 0)
print(best)
