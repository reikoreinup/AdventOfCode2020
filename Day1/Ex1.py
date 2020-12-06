numbers = []

for textInput in open('Input.txt', 'r').readlines():
    numbers.append(int(textInput))

for first in numbers:
    for second in numbers:
        if first + second == 2020:
            print(first * second)



