import numpy as np
from scipy.signal import convolve

INPUT_FILE = '17.in'
with open(INPUT_FILE, "r") as f:
    grid = np.array([[c == "#" for c in line] for line in f.read().splitlines()])

def solve(dim, grid):
    assert dim >= 2
    grid = np.pad(grid[(None,) * (dim - 2)], [(6,)] * dim)
    kernel = np.ones(shape = (3,) * dim, dtype = np.int8)
    kernel[(1,) * dim] = 0

    for i in range(6):
        ns = convolve(grid, kernel, mode = 'same')
        grid = (grid & np.isin(ns, [2, 3])) | (~grid & (ns == 3))

    return np.sum(grid)

print(solve(3, grid))
print(solve(4, grid))
