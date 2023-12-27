import re

network = {}
def add_node(line):
    match_obj = re.match(r'(?P<node>\w+) \= \((?P<left>\w+), (?P<right>\w+)\)', line)
    details = match_obj.groupdict()
    network[(details['node'], 'L')] = details['left']
    network[(details['node'], 'R')] = details['right']

lines = open('inputs/day8', 'r').read().split('\n\n') 
directions = lines[0]
nodes = lines[1].split('\n')
nodes = [x for x in nodes if x]

for n in nodes:
    add_node(n)

curr = 'AAA'
step = 0
while(curr != 'ZZZ'):
    d = directions[step % len(directions)]
    curr = network[(curr, d)]
    step += 1
print(step)
