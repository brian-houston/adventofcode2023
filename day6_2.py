import math

def calc_distance(hold_time, max_time):
    return hold_time * (max_time - hold_time)

lines = open('inputs/day6', 'r').read().split('\n') 
time = int(''.join(lines[0].split()[1:]))
distance = int(''.join(lines[1].split()[1:]))

a = 1
b = -time
c = distance

sol1 = (time - math.sqrt(b**2-4*a*c))/(2*a)
sol2 = (time + math.sqrt(b**2-4*a*c))/(2*a)
print(math.floor(sol2) - math.ceil(sol1) + 1)
