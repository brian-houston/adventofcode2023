lines = open('inputs/day4', 'r').read().split('\n') 
lines = [x for x in lines if x]

sum = 0
for line in lines:
    colonIndex = line.find(':')
    barIndex = line.find('|')
    winningNumsString = line[colonIndex+1:barIndex].strip()
    myNumsString = line[barIndex+1:].strip()
    winningNums = set([int(x) for x in winningNumsString.split()])
    myNums = [int(x) for x in myNumsString.split()]
    match = -1 
    for n in myNums:
        if n in winningNums:
            match += 1
    if match >= 0:
        sum += 2 ** match

print(sum)
