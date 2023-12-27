chunks = open('inputs/day5', 'r').read().split('\n\n') 

class Range:
    def __init__(self, line):
        line = line.split(' ')
        self.dst_start = int(line[0])
        self.src_start = int(line[1])
        self.length = int(line[2])

    def __repr__(self):
        return f'{self.dst_start} {self.src_start} {self.length}'

    def map(self, x):
        return x - self.src_start + self.dst_start

    def is_inside(self, x):
        return x >= self.src_start and x <= self.src_start + self.length

def map_all(x, ranges):
    for r in ranges:
        if r.is_inside(x):
            return r.map(x)
    return x

def cut_before_colon(chunk):
    colon_index = chunk.find(':')
    return chunk[colon_index+1:].strip()

chunks = [cut_before_colon(chunk) for chunk in chunks]
seeds = [int(x) for x in chunks[0].split()]
chunks = chunks[1:]
chunks = [[Range(y) for y in x.split('\n')] for x in chunks]
for ranges in chunks:
    seeds = [map_all(x, ranges) for x in seeds]

print(min(seeds))
