lines = []

def sort_pair(a, b):
    if b > a:
        return [a, b]
    return [b, a]

class Block:
    def __init__(self, line):
        left, right = line.split('~')
        left = [int(x) for x in left.split(',')]
        right = [int(x) for x in right.split(',')]
        self.xs = sort_pair(left[0], right[0])
        self.ys = sort_pair(left[1], right[1])
        self.zs = sort_pair(left[2], right[2])
        self.height = self.zs[1] - self.zs[0] + 1
        self.supporters = set()
        self.supportees = set()

    def can_be_removed(self):
        for b in self.supportees:
            if len(b.supporters) < 2:
                return False
        return True

    def other_bricks_would_fall(self, falling):
        count = 0
        need_to_count = []
        for b in self.supportees:
            if b not in falling and b.supporters.issubset(falling):
                falling.add(b)
                need_to_count.append(b)
                count += 1

        for b in need_to_count:
            count += b.other_bricks_would_fall(falling) 

        return count

    def __repr__(self):
        return f'{self.xs} {self.ys} {self.zs}'

with open('inputs/day22', 'r') as file:
    lines = file.read().splitlines()

blocks = [Block(x) for x in lines]
blocks.sort(key = lambda b: b.zs[0])

n = 10

heights = [[0 for y in range(n)] for x in range(n)]
top_blocks = [[None for y in range(n)] for x in range(n)]

for i, b in enumerate(blocks):
    highest = 0
    for x in range(b.xs[0], b.xs[1] + 1):
        for y in range(b.ys[0], b.ys[1] + 1):
            highest = max(heights[x][y], highest)

    supports = 0
    for x in range(b.xs[0], b.xs[1] + 1):
        for y in range(b.ys[0], b.ys[1] + 1):
            if heights[x][y] == highest and highest > 0:
                top_blocks[x][y].supportees.add(b)
                b.supporters.add(top_blocks[x][y])
            heights[x][y] = highest + b.height
            top_blocks[x][y] = b

removable = 0
other_bricks = 0
for b in blocks:
    if b.can_be_removed():
        removable += 1
    other_bricks += b.other_bricks_would_fall(set([b]))


print('part 1', removable)
print('part 2', other_bricks)
