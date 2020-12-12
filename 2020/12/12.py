import numpy as np

INPUT_FILE = "12.in"
with open(INPUT_FILE, 'r') as f:
    inp = f.read().splitlines()

# ship positiont
p1 = np.array((0, 0))
p2 = np.array((0, 0))

# waypoint position
wpp1 = np.array((1, 0))
wpp2 = np.array((10, 1))

move = {}
move['N'] = np.array((0, 1))
move['S'] = np.array((0, -1))
move['E'] = np.array((1, 0))
move['W'] = np.array((-1, 0))

rotate = {}
rotate["L"] = np.array([[0, -1], [1, 0]])
rotate["R"] = np.array([[0, 1], [-1, 0]])

for line in inp:
    action, value = line[:1], int(line[1:])
    if action == "F":
        p1 += value * wpp1
        p2 += value * wpp2
    elif action in ['R', 'L']:
        for _ in range(value // 90):
            wpp1 = np.matmul(rotate[action], wpp1)
            wpp2 = np.matmul(rotate[action], wpp2)
    else:
        p1 += value * move[action]
        wpp2 += value * move[action]

print(abs(p1[0]) + abs(p1[1]))
print(abs(p2[0]) + abs(p2[1]))
