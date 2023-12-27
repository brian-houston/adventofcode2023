lines = open('inputs/day1', 'r').read().split('\n') 

keywords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def first_digit(line, reversed = False):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            return line[i] 
        for j, kw in enumerate(keywords, 1):
            if reversed:
                kw = kw[::-1]
            if line[i:].startswith(kw):
                return str(j)
        i += 1
    return '0' 

lines = [first_digit(line) + first_digit(line[::-1], reversed=True) for line in lines]
lines = [int(line) for line in lines]
print(sum(lines))
