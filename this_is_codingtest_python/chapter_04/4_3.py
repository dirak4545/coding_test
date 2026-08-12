pos = input()
tran = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x = tran[pos[0]]
y = int(pos[1])
cnt = 0

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

for dx, dy in steps:
    nx, ny = x + dx, y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)
