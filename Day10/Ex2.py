def ranges(nums):
    nums = sorted(set(nums))
    edges = iter(nums[:1] + sum([[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e], []) + nums[-1:])
    return [(s, e) for s, e in zip(edges, edges)]

numbers = [int(item.strip()) for item in open('Input.txt', 'r').readlines()]
numbers.extend([0, max(numbers) + 3])

dubious_ranges = ranges(numbers)
total = 1
for dubious in dubious_ranges:
    if dubious[1] == dubious[0]:
        continue
    potential_possibilites = 2 ** (dubious[1] - dubious[0] - 1)
    if potential_possibilites == 8:
        potential_possibilites = 7
    total *= potential_possibilites
print(total)