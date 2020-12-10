INPUT_FILE = "8.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

saccu = 0
for k, line in enumerate(inp):
    newinp = list(inp)
    words = line.split()
    if words[0] == "jmp":
        newinp[k] = "nop 0"
    elif words[0] == "nop":
        newinp[k] = "jmp " + line.split()[1]

    accu = 0
    i = 0
    indices = set([])
    while True:
        if i == len(inp):
            # part2
            print(accu)
        if i in indices or i < 0 or i >= len(inp):
            break
        indices.add(i)
        comm, val = newinp[i].split()
        val = int(val)
        if comm == "acc":
            accu += val
            i += 1
        elif comm == "jmp":
            i += val
        else:
            i += 1

# part1
print(accu)
