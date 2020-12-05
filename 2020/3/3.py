import math

INPUT_FILE = "3.in"
with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
nums = []

# not the brightest one
for slope in slopes:
    i, j = 0, 0
    c = 0
    while i < len(inp):
        if inp[i][j] == "#": 
            c += 1
        j = (j +slope[0]) % len(inp[0])
        i += slope[1]
    nums.append(c)
print(math.prod(nums))
