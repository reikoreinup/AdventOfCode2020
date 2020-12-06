attributes = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]


def is_ok(text_input):
    for attribute in attributes:
        if attribute not in text_input:
            return False
    return True


count = 0
for textInput in "".join(open('Input.txt', 'r').readlines()).split("\n\n"):
    if is_ok(textInput):
        count += 1
print(count)
