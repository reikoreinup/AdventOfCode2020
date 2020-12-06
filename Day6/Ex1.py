results = []
with open('Input.txt', 'r') as file:
    data = file.read().split('\n\n')
    for datum in data:
        results.append("".join(set(datum.replace("\n", ""))))
print(sum([len(item) for item in results]))
