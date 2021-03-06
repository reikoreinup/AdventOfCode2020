ids = []
for textInput in open('Input.txt', 'r').readlines():
    rows, columns = [i for i in range(128)], [i for i in range(8)]

    for letter in textInput:
        if letter == 'F':
            for i in range(len(rows) // 2):
                del rows[-1]
        if letter == 'B':
            for i in range(len(rows) // 2):
                del rows[0]
        if letter == 'L':
            for i in range(len(columns) // 2):
                del columns[-1]
        if letter == 'R':
            for i in range(len(columns) // 2):
                del columns[0]
    ids.append(rows[0] * 8 + columns[0])

print([item for item in range(min(ids), max(ids) + 1) if item not in ids])

