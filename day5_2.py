chunks = open('inputs/day5', 'r').read().split('\n\n') 

class MapRange:
    def __init__(self, line):
        line = line.split(' ')
        self.dst_start = int(line[0])
        self.src_start = int(line[1])
        self.length = int(line[2])
        self.src_end = self.src_start + self.length

    def __repr__(self):
        return f'{self.dst_start} {self.src_start} {self.length}'

    def map(self, x):
        return x - self.src_start + self.dst_start

    def is_inside(self, x):
        return x >= self.src_start and x <= self.src_start + self.length

    def intersection(self, x):
        if x.start > self.src_end or x.end < self.src_start:
            return None 
        
        return Range(max(x.start, self.src_start), min(x.end, self.src_end))

    def map_range(self, x, mapped_out, unmapped_out):
        inter = self.intersection(x)
        if not inter:
            unmapped_out.append(x)
            return

        mapped_out.append(Range(self.map(inter.start), self.map(inter.end)))
        if x.start < inter.start:
            unmapped_out.append(Range(x.start, inter.start - 1))
        if x.end > inter.end:
            unmapped_out.append(Range(inter.end + 1, x.end))

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end 

    def __repr__(self):
        return f'{self.start} {self.end}'

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
seeds = [Range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0,len(seeds),2)]
chunks = chunks[1:]
chunks = [[MapRange(y) for y in x.split('\n')] for x in chunks]

for ranges in chunks:
    mapped_seeds = []
    for r in ranges:
        unmapped_seeds = []
        for s in seeds:
            r.map_range(s, mapped_seeds, unmapped_seeds)
        seeds = unmapped_seeds 
    seeds += mapped_seeds

print(min([s.start for s in seeds]))
