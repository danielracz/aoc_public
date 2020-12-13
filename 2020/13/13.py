from sympy.ntheory.modular import crt

INPUT_FILE = "13.in"
with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

ts = int(inp[0])
buses = [(-i, int(x)) for i, x in enumerate(inp[1].split(",")) if x != "x"]

# part 1
leaves = min([(x[1], (ts // x[1] + 1) * x[1]) for x in buses], key = lambda x: x[1] - ts)
print(leaves[0] * (leaves[1] - ts))

# part2
a, n = list(zip(*buses))
print(crt(n, a)[0])
