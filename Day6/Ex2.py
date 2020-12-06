sets = []
with open('Input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    for group in groups:
        sets.append([set(person) for person in group.split("\n")])
print(sum([len(item[0].intersection(*item)) for item in sets]))
