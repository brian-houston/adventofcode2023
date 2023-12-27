symbol_lookup = {
        '.': {
            'right': ['right'],
            'left': ['left'],
            'up': ['up'],
            'down': ['down'],
            },
        '\\': {
            'right': ['down'],
            'left': ['up'],
            'up': ['left'],
            'down': ['right'],
            },
        '/': {
            'right': ['up'],
            'left': ['down'],
            'up': ['right'],
            'down': ['left'],
            },
        '|': {
            'right': ['up', 'down'],
            'left': ['up', 'down'],
            'up': ['up'],
            'down': ['down']
            },
        '-': {
            'right': ['right'],
            'left': ['left'],
            'up': ['left', 'right'],
            'down': ['left', 'right']
            }
        }

direction_lookup = {
        'left': (-1, 0),
        'right': (1, 0),
        'up': (0, -1),
        'down': (0, 1),
        }

class Beam:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def update(self, grid):
        symbol = grid[self.y][self.x]
        new_directions = symbol_lookup[symbol][self.direction]
        self.direction = new_directions[0]
        self.update_position()

        if len(new_directions) > 1:
            new_beam = Beam(self.x, self.y, new_directions[1])
            new_beam.update_position()
            return new_beam

        return None
    
    def within(self, width, height):
        return self.x >= 0 and self.x < width and self.y >= 0 and self.y < height

    def update_position(self):
        change = direction_lookup[self.direction]
        self.x += change[0]
        self.y += change[1]

    def __repr__(self):
        return f'{self.x} {self.y} {self.direction}'

direction_to_i = {
        'left': 0,
        'right': 1,
        'up': 2,
        'down': 3
        }
# returns True if first time visiting in that direction
def set_visited(beam, visited):
    i = direction_to_i[beam.direction]
    v = 1 << i;
    if visited[beam.y][beam.x] & v != 0:
        return False
    visited[beam.y][beam.x] |= v
    return True


grid = []
with open('inputs/day16', 'r') as file:
    grid = file.read().splitlines()
width = len(grid[0])
height = len(grid)
visited = [[0 for x in range(width)] for y in range(height)]

beams = [Beam(0, 0, 'right')]

while beams:
    if not beams[-1].within(width, height) or not set_visited(beams[-1], visited):
        beams.pop()
        continue
    new_beam = beams[-1].update(grid)
    if new_beam:
        beams.append(new_beam)

count = 0
for row in visited:
    for v in row:
        count += int(v != 0)
print(count)
