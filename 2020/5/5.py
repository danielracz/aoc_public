import numpy as np
import networkx as nx
import copy
import itertools
import math

from collections import defaultdict, deque, Counter
from scipy.signal import convolve

INPUT_FILE = "5.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

def get_rc(s):
    a = s[:7].replace("F", "0").replace("B", "1")
    b = s[7:].replace("R", "1").replace("L", "0")
    return int(a, 2), int(b, 2)

ids = [8 * x[0] + x[1] for l in inp if (x := get_rc(l))]
m, M = min(ids), max(ids)

# part 1
print(M)

# part 2
print(set(range(m, M)) - set(ids))
