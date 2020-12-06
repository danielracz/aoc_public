# refactored (reddit)
# original is not worth to share

INPUT_FILE = "4.in"
with open(INPUT_FILE, 'r') as f:
    inp = f.read().split("\n\n")

passp =[dict(entry.split(":") for entry in (" ".join(each.splitlines()).split()))
        for each in inp]

validator = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) \
                     or (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: x.startswith("#") and len(x) == 7
                     and all(c in '0123456789abcdef' for c in x[1:]),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric()
}

# part1
print(sum(all(k in p for k in validator.keys())
          for p in passp))

# part2
print(sum(all(k in p for k in validator.keys())
          and all(validator[k](v) for k, v in p.items() if k != 'cid')
          for p in passp))
