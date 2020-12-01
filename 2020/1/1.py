import itertools

INPUT_FILE = "1.in"

with open(INPUT_FILE, 'r') as f:
    inp = list(map(int, f.read().splitlines()))

# part 1
print(next(each[0] * each[1] for each in itertools.combinations(inp, r = 2)
                             if sum(each) == 2020))

# part 2
print(next(each[0] * each[1] * each[2] for each in itertools.combinations(inp, r = 3)
                                       if sum(each) == 2020))
