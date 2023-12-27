from queue import Queue
import random
lines = []
with open('inputs/day25', 'r') as file:
    lines = file.read().splitlines()

vertices = {}

def parse_line(line):
    global vertices
    node, neighbors = line.split(': ')
    neighbors = neighbors.split(' ')
    vertices.setdefault(node, set())
    for n in neighbors:
        vertices.setdefault(n, set())
        vertices[node].add(n)
        vertices[n].add(node)

def count_connected(start):
    visited = set([start])
    q = Queue()
    for n in vertices[start]:
        visited.add(n)
        q.put(n)

    while not q.empty():
        curr = q.get()
        for n in vertices[curr]:
            if n not in visited:
                visited.add(n)
                q.put(n)
    return len(visited)

def bfs(start, goal):
    if start == goal:
        return []

    visited = set([start])
    q = Queue()
    trace = {start: None}

    for n in vertices[start]:
        visited.add(n)
        q.put(n)
        trace[n] = start

    while goal not in visited:
        curr = q.get()
        for n in vertices[curr]:
            if n not in visited:
                visited.add(n)
                q.put(n)
                trace[n] = curr
    
    curr = goal
    path = []
    while curr:
        path.append(curr)
        curr = trace[curr]
    return path
    

for line in lines:
    parse_line(line)

labels = list(vertices.keys())
edge_counts = {}
for _ in range(200):
    path = bfs(random.choice(labels), random.choice(labels))
    for i in range(1, len(path)):
        a = path[i - 1]
        b = path[i]
        key = tuple(sorted([a, b]))
        edge_counts.setdefault(key, 0)
        edge_counts[key] += 1
sorted_edges = sorted(edge_counts.items(), key=lambda x: x[1])
for key, _ in sorted_edges[-3:]:
    a, b = key
    vertices[a].remove(b)
    vertices[b].remove(a)

count1 = count_connected(sorted_edges[-1][0][0])
count2 = count_connected(sorted_edges[-1][0][1])
print(count1 * count2)
