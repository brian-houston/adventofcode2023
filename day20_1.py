class Module:
    def __init__(self, line):
        label, outputs = line.split(' -> ')
        self.outputs = outputs.split(', ')
        self.inputs = []
        self.state = 0
        if label[0] in '&%':
            self.type = label[0] 
            self.label = label[1:]
        else:
            self.type = 'broadcast'
            self.label = label 

    def init_state(self):
        if self.type == '%':
            self.state = 0
        elif self.type == '&':
            self.state = [0 for _ in self.inputs]

    def connect(self, modules):
        for dst in self.outputs:
            if dst in modules:
                modules[dst].inputs.append(self.label)

    def process_pulse(self, p):
        pulse_src, _, pulse_strength = p
        src = self.label
        strength = -1 
        if self.type == '%' and pulse_strength == 0:
            self.state = 1 - self.state 
            strength = 1 if self.state == 1 else 0
        elif self.type == '&':
            self.state[self.inputs.index(pulse_src)] = pulse_strength 
            strength = 0 if sum(self.state) == len(self.inputs) else 1
        if strength >= 0:
            return [(src, dst, strength) for dst in self.outputs]
        else:
            return []

    def __repr__(self):
        return f'{self.type} {self.label} {self.outputs}'

lines = []
with open('inputs/day20', 'r') as file:
    lines = file.read().splitlines()
    
modules = {}
for line in lines:
    mod = Module(line)
    modules[mod.label] = mod

for mod in modules.values():
    mod.connect(modules)

for mod in modules.values():
    mod.init_state()

count = [0, 0]
init_pulses = [('broadcaster', m, 0) for m in modules['broadcaster'].outputs]
for i in range(1000):
    pulses = init_pulses
    count[0] += 1
    while pulses:
        next_pulses = []
        for p in pulses:
            count[p[2]] += 1
            if p[1] not in modules:
                continue
            nps = modules[p[1]].process_pulse(p)
            if nps:
                next_pulses += nps
        pulses = next_pulses

print(count[0] * count[1])    
