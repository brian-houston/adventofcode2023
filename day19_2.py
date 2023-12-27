import copy

def parse_workflow(line):
    bracket = line.find(chr(123))
    label = line[:bracket]
    conditions = line[bracket+1:-1].split(',')
    for i in range(len(conditions)):
        if ':' in conditions[i]:
            conditions[i] = conditions[i].split(':')
            conditions[i][0] = [conditions[i][0][0], conditions[i][0][1], int(conditions[i][0][2:])]
        else:
            conditions[i] = [conditions[i]]
    return label, conditions

def split_interval(interval, condition):
    var = condition[0]
    sign = condition[1]
    num = condition[2]
    pass_interval = copy.deepcopy(interval)
    reject_interval = copy.deepcopy(interval)

    if sign == '<':
        if interval[var][0] >= num:
            return None, interval
        if interval[var][1] < num:
            return interval, None
        pass_interval[var][1] = num - 1
        reject_interval[var][0] = num
    else:
        if interval[var][0] > num:
            return interval, None
        if interval[var][1] <= num:
            return None, interval
        pass_interval[var][0] = num + 1
        reject_interval[var][1] = num

    return pass_interval, reject_interval

def calc_combinations(interval):
    ret = 1
    del interval['workflow']
    for min, max in interval.values():
        ret *= max - min + 1
    return ret


workflows = []
with open('inputs/day19', 'r') as file:
    workflows, _ = file.read().split('\n\n')
    workflows = workflows.splitlines()

workflows_dict = {}
for w in workflows:
    label, conditions = parse_workflow(w)
    workflows_dict[label] = conditions

init_interval = {
        'workflow': 'in',
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000],
        }
intervals = [init_interval]

result = 0
while intervals:
    p = intervals.pop()
    if p['workflow'] in 'RA':
        if p['workflow'] == 'A':
            result += calc_combinations(p)
        continue

    for condition in workflows_dict[p['workflow']]:
        if not p:
            break
        if len(condition) == 1:
            p['workflow'] = condition[0]
            intervals.append(p)
            break

        pass_interval, p = split_interval(p, condition[0])
        if pass_interval:
            pass_interval['workflow'] = condition[1]
            intervals.append(pass_interval)

print(result)
