all_directions = ['N', 'E', 'S', 'W']
current_direction = 'E'
current_pos = (0, 0)

def move(command, amount, current_pos):
    if command == 'N':
        current_pos = (current_pos[0] + amount, current_pos[1])
    elif command == 'E':
        current_pos = (current_pos[0], current_pos[1] + amount)
    elif command == 'S':
        current_pos = (current_pos[0] - amount, current_pos[1])
    elif command == 'W':
        current_pos = (current_pos[0], current_pos[1] - amount)
    return current_pos

for textInput in open('Input.txt', 'r').readlines():
    command = textInput[0]
    amount = int(textInput[1:])
    if command == 'R':
        new_dir_idx = all_directions.index(current_direction) + amount // 90
        if new_dir_idx >= len(all_directions):
            new_dir_idx -= 4
        current_direction = all_directions[new_dir_idx]
    elif command == 'L':
        current_direction = all_directions[all_directions.index(current_direction) - amount // 90]
    elif command == 'F':
        current_pos = move(current_direction, amount, current_pos)
    else:
        current_pos = move(command, amount, current_pos)
print(f'Manhattan value for position {current_pos}: {abs(current_pos[0]) + abs(current_pos[1])}')
