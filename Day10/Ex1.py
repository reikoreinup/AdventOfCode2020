numbers = [int(item.strip()) for item in open('Input.txt', 'r').readlines()]
numbers.sort()
prev, single, triple = 0, 0, 1
for number in numbers:
    if number - prev == 1:
        single += 1
    elif number - prev == 3:
        triple += 1
    prev = number
print(f'single = {single}, triple = {triple}, multiplied = {single * triple}')