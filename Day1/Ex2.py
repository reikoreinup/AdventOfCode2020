numbers = []

for textInput in open('Input.txt', 'r').readlines():
    numbers.append(int(textInput))

for first in numbers:
    for second in numbers:
        for third in numbers:
            if first + second + third == 2020:
                print(first * second * third)
