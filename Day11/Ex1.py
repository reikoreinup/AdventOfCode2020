def check(y, x, seatmap, value):
    if y < 0 or x < 0:
        return False
    try:
        return seatmap[y][x] == value
    except IndexError:
        return False


def surrounding_value(x, y, seatmap):
    up = down = right = left = up_left = down_right = up_right = down_left = False
    up = check(y - 1, x, seatmap, '#')
    down = check(y + 1, x, seatmap, '#')
    right = check(y, x + 1, seatmap, '#')
    left = check(y, x - 1, seatmap, '#')
    up_left = check(y - 1, x - 1, seatmap, '#')
    down_right = check(y + 1, x + 1, seatmap, '#')
    up_right = check(y - 1, x + 1, seatmap, '#')
    down_left = check(y + 1, x - 1, seatmap, '#')
    values = [up, down, right, left, up_left, down_right, up_right, down_left]
    return sum(values)

with open('Input.txt', 'r') as f:
    seatmap = []
    for element in f:
        seatmap.append(list("".join(element.strip().split('\n'))))
    while True:
        to_occupied_idxs = []
        to_empty_idxs = []
        for y in range(len(seatmap)):
            for x in range(len(seatmap[0])):
                if seatmap[y][x] == 'L' and surrounding_value(x, y, seatmap) == 0:
                    to_occupied_idxs.append((y, x))
                if seatmap[y][x] == '#' and surrounding_value(x, y, seatmap) >= 4:
                    to_empty_idxs.append((y, x))
        for o_idx in to_occupied_idxs:
            seatmap[o_idx[0]][o_idx[1]] = '#'
        for e_idx in to_empty_idxs:
            seatmap[e_idx[0]][e_idx[1]] = 'L'
        if len(to_occupied_idxs) == 0 and len(to_empty_idxs) == 0:
            break
    print(sum(["".join(item).count("#") for item in seatmap]))




