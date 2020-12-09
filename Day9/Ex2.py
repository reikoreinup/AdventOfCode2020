def sublists(l, n):
    for i in range(len(l) + 1):
        for j in range(i + 1, len(l) + 1):
            sli = l[i:j]
            if sum(sli) == bad_number:
                print(min(sli) + max(sli))

bad_number = 177777905
numbers = [int(item.strip()) for item in open('Input.txt', 'r').readlines()]
sublists(list(filter(lambda n: n < bad_number, numbers)), bad_number)
