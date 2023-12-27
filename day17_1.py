from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

grid = []
with open('inputs/day17', 'r') as file:
    grid = file.read().splitlines()

grid = [[int(y) for y in x] for x in grid]

width = len(grid[0])
height = len(grid)

def within(p):
    return p[0] >= 0 and p[0] < width and p[1] >= 0 and p[1] < height

def add_points(a, b):
    return (a[0] + b[0], a[1] + b[1])

@dataclass(order=True)
class FrontierNode:
    position: Any=field(compare=False)
    direction: Any=field(compare=False)
    heat_loss: int
    steps: Any=field(compare=False)

    def __init__(self, position, direction, heat_loss, steps, prev):
        self.position = position
        self.direction = direction
        self.heat_loss = heat_loss
        self.steps = steps
        self.prev = prev

    def get_next_nodes(self):
        next_directions = []
        next_directions.append((self.direction[1], self.direction[0]))
        next_directions.append((-self.direction[1], -self.direction[0]))
        if self.steps < 2:
            next_directions.append(self.direction)

        next_nodes = []
        for nd in next_directions:
            np = add_points(self.position, nd)
            if not within(np):
                continue
            steps = self.steps + 1 if nd == self.direction else 0
            heat_loss = self.heat_loss + grid[np[1]][np[0]]
            next_nodes.append(FrontierNode(np, nd, heat_loss, steps, self))
        return next_nodes

    def __repr__(self):
        return f'{self.position} {self.direction} {self.heat_loss}'

init_node1 = FrontierNode((1, 0), (1, 0), grid[0][1], 1, None)
init_node2 = FrontierNode((0, 1), (0, 1), grid[1][0], 1, None)

visited = set()
queue = PriorityQueue()
queue.put(init_node1)
queue.put(init_node2)
while not queue.empty():
    node = queue.get()
    if node.position == (width - 1, height - 1):
        print(node.heat_loss)
        break
    if (node.position, node.direction, node.steps) in visited:
        continue
    visited.add((node.position, node.direction, node.steps))

    next_nodes = node.get_next_nodes()
    for n in next_nodes:
        queue.put(n)
