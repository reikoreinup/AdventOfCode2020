import itertools

def is_valid(list, number):
    for value in itertools.combinations(list, 2):
        if (sum(value)) == number:
            return True
    return False

numbers = [int(item.strip()) for item in open('Input.txt', 'r').readlines()]
for i in range(25, len(numbers)):
    if not is_valid(numbers[i - 25:i], numbers[i]):
        print(numbers[i])
