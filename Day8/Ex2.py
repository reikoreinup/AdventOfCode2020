commands_list = [item.strip().split(" ") for item in open('Input.txt', 'r').readlines()]

for i in range(len(commands_list)):
    commands = list(enumerate(commands_list))
    commands[i] = (commands[i][0], [commands[i][1][0].replace("jmp", "nop"), commands[i][1][1]])
    done_commands = []
    accumulator = 0
    i = 0
    while True:
        if i == len(commands):
            print(accumulator)
            break
        if commands[i][0] in done_commands:
            break
        else:
            done_commands.append(commands[i][0])
        command = commands[i][1][0]
        argument = commands[i][1][1]
        if command == 'acc':
            accumulator += int(argument)
            i += 1
        elif command == 'jmp':
            i += int(argument)
        else:
            i += 1
