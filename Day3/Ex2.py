totalCount = 1
for i in [1, 3, 5, 7]:
    f = open('Input.txt')
    f.readline()
    line = f.readline()
    count, idx = 0, i
    while line:
        line = line.strip() * 1000  # xD
        while idx >= len(line):
            idx = idx - len(line) - 1
        if line[idx] == "#":
            count += 1
        idx += i
        line = f.readline()
    totalCount *= count

f = open('Input.txt')
f.readline()
f.readline()
line = f.readline()
count, idx = 0, 1
while line:
    line = line.strip() * 1000  # xD
    while idx >= len(line):
        idx = idx - len(line) - 1
    if line[idx] == "#":
        count += 1
    idx += 1
    f.readline()
    line = f.readline()
totalCount *= count
# paha on olla
print(totalCount)
