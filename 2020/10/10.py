import numpy as np

INPUT_FILE = "10.in"

with open(INPUT_FILE, 'r') as f:
    inp = list(map(int, f.read().splitlines()))
    M = max(inp) + 3
    inp.extend([M, 0])

# part1 (kudos to Balu for np.diff)
diffs = list(np.diff(sorted(inp)))
print(diffs.count(3) * diffs.count(1))

def memoize(f):
    memo = {}
    def cache(last):
        if last not in memo:
            memo[last] = f(last)
        return memo[last]
    return cache

@memoize
def get_sum(last):
    if last == 0:
        return 1
    return sum(get_sum(i) for i in inp if last > i >= last - 3)

# part2
print(get_sum(M))
