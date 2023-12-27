lines = open('inputs/day1', 'r').read().split('\n') 

def first_digit(line):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            return line[i] 
        i += 1
    return 0

lines = [first_digit(line) + first_digit(line[::-1]) for line in lines]
lines = [int(line) for line in lines]
print(sum(lines))
