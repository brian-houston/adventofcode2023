def pairs(arr):
    if len(arr) < 2:
        return (0, 0)
    
    for i in range(1, len(arr)):
        yield (arr[i-1], arr[i])

def has_nonzero(arr):
    for n in arr:
        if n != 0:
            return True
    return False

lines = open('inputs/day9', 'r').read().split('\n') 
lines = [[int(y) for y in x.split()] for x in lines if x]

ans = 0
for line in lines:
    sum = line[-1]
    while has_nonzero(line):
        line = [x[1] - x[0] for x in pairs(line)]
        sum += line[-1]
    ans += sum
print(ans)
