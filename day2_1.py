lines = open('inputs/day2', 'r').read().split('\n') 
lines = [x.split(':')[1] for x in lines if x]
lines = [[[z.strip().split(' ') for z in y.split(',')] 
        for y in x.split(';')] 
        for x in lines]

lookup = {
        'red': 12,
        'green': 13,
        'blue': 14,
        }

def is_possible(game):
    for draw in game:
        for pair in draw:
            if int(pair[0]) > lookup[pair[1]]:
                return False
    return True

sum = 0
for i, game in enumerate(lines, 1):
    if is_possible(game):
        sum += i
print(sum)

