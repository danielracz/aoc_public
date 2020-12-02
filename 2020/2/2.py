from collections import Counter

INPUT_FILE = "2.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

def valid(line):
    nums, letter, s = line.strip().split()
    m, M = map(int, nums.split("-"))
    letter = letter[0]
    # part 1
    #c = Counter(s)
    #return m <= c[letter] <= M

    return (s[m - 1] == letter) ^ (s[M - 1] == letter)

print(sum(1 for line in inp if valid(line)))
