print(sum([len(item) for item in ["".join(set(datum.replace("\n", ""))) for datum in open('Input.txt', 'r').read().split('\n\n')]]))
