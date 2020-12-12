ship_pos, wp_pos = (0, 0), (1, 10)

def move(command, amount, current_pos):
    if command == 'N':
        return current_pos[0] + amount, current_pos[1]
    elif command == 'E':
        return current_pos[0], current_pos[1] + amount
    elif command == 'S':
        return current_pos[0] - amount, current_pos[1]
    elif command == 'W':
        return current_pos[0], current_pos[1] - amount

for textInput in open('Input.txt', 'r').readlines():
    command = textInput[0]
    amount = int(textInput[1:])
    if command == 'L' or command == 'R':
        turns = amount // 90
        if command == 'L' and turns == 1 or command == 'R' and turns == 3:
            wp_pos = wp_pos[1], -wp_pos[0]
        elif command == 'L' and turns == 3 or command == 'R' and turns == 1:
            wp_pos = -wp_pos[1], wp_pos[0]
        elif turns == 2:
            wp_pos = -wp_pos[0], -wp_pos[1]
    elif command == 'F':
        ship_pos = move("E" if wp_pos[1] >= 0 else "W", abs(wp_pos[1] * amount), ship_pos)
        ship_pos = move("N" if wp_pos[0] >= 0 else "S", abs(wp_pos[0] * amount), ship_pos)
    else:
        wp_pos = move(command, amount, wp_pos)
print(f'Manhattan value for position {ship_pos}: {abs(ship_pos[0]) + abs(ship_pos[1])}')
