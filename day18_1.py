lines = []
with open('inputs/day18', 'r') as file:
    lines = file.read().splitlines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.x} {self.y}'
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

class Edge:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    def __repr__(self):
        return f'{self.x} {self.y} {self.direction}'

direction_lookup = {
        'R': Point(1, 0),
        'L': Point(-1, 0),
        'U': Point(0, 1),
        'D': Point(0, -1),
        }

class Instruction:
    def __init__(self, line):
        line = line.split()
        self.direction = line[0]
        self.length = int(line[1])
        self.color = line[2][2:-1] 
    def to_point(self):
        d = direction_lookup[self.direction]
        return Point(d.x * self.length, d.y * self.length)

instructions = [Instruction(line) for line in lines]
curr = Point(0, 0)
area = 0
edge_area = 0
prev = None
for instr in instructions:
    prev = curr
    diff = instr.to_point()
    curr = curr.add(diff)
    area += (prev.y + curr.y) * (prev.x - curr.x) 
    edge_area += abs(diff.x + diff.y)

print(int(1 + 0.5 * (abs(area) + edge_area)))
