count = 0
for textInput in open('Input.txt', 'r').readlines():
    textInput = textInput.split(":")

    letter = textInput[0][-1]
    word = textInput[1]
    low = int(textInput[0][:-2].split("-")[0])
    high = int(textInput[0][:-2].split("-")[1])
    
    if len(word) > high and (bool(word[low] == letter) ^ bool(word[high] == letter)):
        count += 1

print(count)

