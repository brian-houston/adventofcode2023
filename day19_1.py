def parse_part(line):
    line = line[1:-1] #remove brackets
    ret = {}
    for rating in line.split(','):
        key, value = rating.split('=')
        ret[key] = int(value)
    return ret

def parse_workflow(line):
    bracket = line.find(chr(123))
    label = line[:bracket]
    conditions = line[bracket+1:-1].split(',')
    for i in range(len(conditions)):
        if ':' in conditions[i]:
            conditions[i] = conditions[i].split(':')
        else:
            conditions[i] = [conditions[i]]
    return label, conditions

workflows = []
parts = []
with open('inputs/day19', 'r') as file:
    workflows, parts = file.read().split('\n\n')
    workflows = workflows.splitlines()
    parts = parts.splitlines()


workflows_dict = {}
for w in workflows:
    label, conditions = parse_workflow(w)
    workflows_dict[label] = conditions

result = 0
for p in parts:
    p = parse_part(p)
    workflow = 'in'
    x, m, a, s = p['x'], p['m'], p['a'], p['s']
    while workflow not in 'AR':
        for condition in workflows_dict[workflow]:
            if len(condition) == 1:
                workflow = condition[0]
            elif eval(condition[0]):
                workflow = condition[1]
                break
    if workflow == 'A':
        result += sum(p.values())
print(result)
