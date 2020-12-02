from collections import Counter

INPUT_FILE = "2.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

def valid(line):
    l = line.strip().split()
    m = int(l[0].split("-")[0])
    M = int(l[0].split("-")[1])
    letter = l[1][:-1]
    s = l[2]

    # part 1
    #c = Counter(s)
    #return c[letter] >= m and c[letter] <= M

    return (s[m - 1] == letter) ^ (s[M - 1] == letter)

print(sum(1 for line in inp if valid(line)))
