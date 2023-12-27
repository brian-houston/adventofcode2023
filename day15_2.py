from collections import OrderedDict
def hash(string):
    curr = 0
    for c in string:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr
        
inputs = open('inputs/day15', 'r').read().strip().split(',') 
boxes = [OrderedDict() for _ in range(256)]
hashed = [hash(x) for x in inputs] 

for string in inputs:
    if '=' in string:
        label, lense = string.split('=')
        boxes[hash(label)][label] = int(lense)
    if '-' in string:
        label = string[:-1]
        box = boxes[hash(label)]
        if label in box:
            box.pop(label)

sum = 0 
for i, box in enumerate(boxes, 1):
    for j, focus in enumerate(box.values(), 1):
        sum += i * j * focus
print(sum)

