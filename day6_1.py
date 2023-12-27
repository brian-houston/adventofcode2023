def calc_distance(hold_time, max_time):
    return hold_time * (max_time - hold_time)

lines = open('inputs/day6', 'r').read().split('\n') 
times = lines[0].split()[1:]
distances = lines[1].split()[1:]
times = [int(x) for x in times]
distances = [int(x) for x in distances]

answer = 1
for i in range(len(times)):
    count = 0
    for j in range(times[i]):
        if calc_distance(j, times[i]) > distances[i]:
            count += 1
    answer *= count

print(answer)
