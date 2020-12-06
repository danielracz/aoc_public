from functools import reduce

INPUT_FILE = "6.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().split("\n\n")

# part1
print(sum(len(set("".join(group.strip().split("\n")))) for group in inp))

# part2
print(sum(all(c in line for line in group.splitlines())
          for group in inp
          for c in set(group)))

# part2 using reduce (reddit)
print(sum(len(reduce(set.intersection, (set(line)
                                        for line in group.splitlines())))
          for group in inp))
