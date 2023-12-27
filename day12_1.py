def gen_number_dots(min_dots, max_dots, i, arr, out):
    if i == len(arr) - 1:
        arr[i] = max_dots
        out.append(arr[:])
        return

    for n in range(min_dots, max_dots + 1):
        arr[i] = n 
        gen_number_dots(1, max_dots - n, i+1, arr, out)

def check_subset_symbols(symbols, i, n, symbol):
    for j in range(i, i+n):
        s = symbols[j]
        if s != symbol and s != '?':
            return False
    return True

def check_symbols(symbols, hashes, dots):
    i = 0
    res = None
    for j in range(len(hashes) + len(dots)):
        k = j // 2
        if j % 2 == 0:
            res = check_subset_symbols(symbols, i, dots[k], '.') 
            i += dots[k]
        else:
            res = check_subset_symbols(symbols, i, hashes[k], '#') 
            i += hashes[k]
        if not res:
            return False
    return True


lines = open('inputs/day12', 'r').read().split('\n') 
lines = [x.split() for x in lines if x]
symbols = [x[0] for x in lines]
nums = [[int(y) for y in x[1].split(',')] for x in lines]
n = len(symbols)

count = 0
for i in range(n):
    nsymbols = len(symbols[i])
    nhashes = sum(nums[i])
    ndots = nsymbols - nhashes
    ngaps = len(nums[i]) + 1
    arr = [0 for _ in range(ngaps)]
    out = []
    gen_number_dots(0, ndots, 0, arr, out)
    for dots in out:
        if check_symbols(symbols[i], nums[i], dots):
            count += 1

print(count)
