lines = open('inputs/day4', 'r').read().split('\n') 
lines = [x for x in lines if x]

length = len(lines)
matches = [0 for _ in range(length)]

for i in reversed(range(length)):
    line = lines[i]
    colonIndex = line.find(':')
    barIndex = line.find('|')
    winningNumsString = line[colonIndex+1:barIndex].strip()
    myNumsString = line[barIndex+1:].strip()
    winningNums = set([int(x) for x in winningNumsString.split()])
    myNums = [int(x) for x in myNumsString.split()]
    match = 0 
    for n in myNums:
        if n in winningNums:
            match += 1
    for j in range(i+1, min(i+match+1, length)):
        match += matches[j]
    matches[i] = match

print(sum(matches) + length)
