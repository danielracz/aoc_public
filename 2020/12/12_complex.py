INPUT_FILE = "12.in"

with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

# ship position
p1 = 0 + 0j
p2 = 0 + 0j

# waypoint position
wpp1 = 1 + 0j
wpp2 = 10 + 1j

move = {}
move['N'] = complex(0, 1)
move['S'] = complex(0, -1)
move['E'] = complex(1, 0)
move['W'] = complex(-1, 0)

rotate = {}
rotate['R'] = -1j
rotate['L'] = 1j

for line in inp:
    action, value = line[:1], int(line[1:])
    if action == "F":
        p1 += value * wpp1
        p2 += value * wpp2
    elif action in ['R', 'L']:
        for _ in range(value // 90):
            wpp1 *= rotate[action]
            wpp2 *= rotate[action]
    else:
        p1 += value * move[action]
        wpp2 += value * move[action]

print(abs(p1.real) + abs(p1.imag))
print(abs(p2.real) + abs(p2.imag))
