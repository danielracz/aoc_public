import re
from functools import reduce
import math

INPUT_FILE = "18.in"
with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

def evalltr_p1(expr):
    nums, signs = re.split("\*|\+", expr), re.split("[0-9]+", expr)[1:-1]
    l = [nums[0]] + [signs[i] + nums[i + 1] for i in range(0, len(signs))]
    return reduce(lambda x, y: eval(str(x) + y), l)

def evalltr_p2(expr):
    return math.prod(eval(x) for x in expr.split("*"))

def eval_line(line, evalltr):
    stack = []
    expr = ""
    for c in line.replace(" ", ""):
        if c.isnumeric() or c in ["*", "+"]:
            expr += c
        elif c == "(":
            stack.append(expr)
            expr = ""
        elif c == ")":
            val = evalltr(expr)
            expr = stack.pop() + str(val)
    return evalltr(expr)

# part1
print(sum(eval_line(line, evalltr_p1) for line in inp))
# part2
print(sum(eval_line(line, evalltr_p2) for line in inp))
