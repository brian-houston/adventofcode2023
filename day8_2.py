import re
import math

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

curr_nodes = [x[0] for x in network.keys() if x[0][2] == 'A' and x[1] == 'L']
n_nodes = len(curr_nodes)
n_directions = len(directions)
cycles = [0 for _ in range(n_nodes)]
for i in range(n_nodes):
    step = 0
    while curr_nodes[i][2] != 'Z':
        d = directions[step % n_directions]
        curr_nodes[i] = network[(curr_nodes[i], d)]
        step += 1
    cycles[i] = step
    
print(math.lcm(*cycles))
