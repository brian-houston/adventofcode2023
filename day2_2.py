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

def power(game):
    maxs = {
            'red': 0,
            'green': 0,
            'blue': 0,
            }

    for draw in game:
        for pair in draw:
            color = pair[1]
            maxs[color] = max(maxs[color], int(pair[0]))

    return maxs['red'] * maxs['green'] * maxs['blue']

lines = [power(game) for game in lines]
print(sum(lines))

