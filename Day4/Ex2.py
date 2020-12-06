import re

attributes = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def are_fields_valid(text_input):
    birth_valid = 1920 <= int(re.search(r"byr:(\d{4})", text_input).group(1)) <= 2002
    issue_valid = 2010 <= int(re.search(r"iyr:(\d{4})", text_input).group(1)) <= 2020
    expiration_valid = 2020 <= int(re.search(r"eyr:(\d{4})", text_input).group(1)) <= 2030
    hair_valid = re.search(r"hcl:#[a-f0-9]{6}", text_input)
    eye_valid = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", text_input)
    pid_valid = re.search(r"pid:[0-9]{9}(?!\d)", text_input)
    if re.search(r"hgt:(\d+)cm", text_input) or re.search(r"hgt:(\d+)in", text_input):
        height_valid = 150 <= int(re.search(r"hgt:(\d+)cm", text_input).group(1)) <= 193 if re.search(r"hgt:(\d+)cm", text_input) else 59 <= int(re.search(r"hgt:(\d+)in", text_input).group(1)) <= 76
    else:
        height_valid = False
    all_valid = birth_valid and issue_valid and expiration_valid and height_valid and hair_valid and eye_valid and pid_valid
    return all_valid

def is_ok(text_input):
    for attribute in attributes:
        if attribute not in text_input:
            return False
    return are_fields_valid(textInput)

count = 0
for textInput in "".join(open('Input.txt', 'r').readlines()).split("\n\n"):
    textInput = textInput.replace("\n", " ")
    if is_ok(textInput):
        count += 1
print(count)
