f = open('Input.txt')
f.readline()
line = f.readline()
count, idx = 0, 3
while line:
    line = line.strip() * 1000  # xD
    while idx >= len(line):
        idx = idx - len(line) - 1
    if line[idx] == "#":
        count += 1
    idx += 3
    line = f.readline()

print(count)
