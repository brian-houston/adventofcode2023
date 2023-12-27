from functools import cache

@cache
def count_arrangements(symbols, nums):
    if not symbols:
        return 1 if not nums else 0
    if not nums:
        return 0 if '#' in symbols else 1
    
    ret = 0
    if symbols[0] in '.?':
        ret += count_arrangements(symbols[1:], nums)
    if symbols[0] in '#?':
        if (nums[0] <= len(symbols) and 
            '.' not in symbols[:nums[0]] and
            (nums[0] == len(symbols) or symbols[nums[0]] != '#')):
            ret += count_arrangements(symbols[nums[0]+1:], nums[1:]) 
    return ret

lines = open('inputs/day12', 'r').read().splitlines() 

sum = 0
for line in lines:
    symbols, nums = line.split()
    nums = eval(nums)
    symbols = '?'.join([symbols] * 5)
    nums = nums * 5
    sum += count_arrangements(symbols, nums)
print(sum)
