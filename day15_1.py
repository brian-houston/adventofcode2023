def hash(string):
    curr = 0
    for c in string:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr
        
inputs = open('inputs/day15', 'r').read().strip().split(',') 
hashed = [hash(x) for x in inputs] 
print(sum(hashed))
