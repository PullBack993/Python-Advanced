import re
letters = r"[a-z]"
punctuation = r"['\?,\!\.-]"
counter_letters = 0
counter_punctuation = 0
output = []

with open('2text.txt', 'r') as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        line_letter = (len(re.findall(letters, line, re.IGNORECASE)))
        line_punct = (len(re.findall(punctuation, line)))
        output.append(f"Line: {counter} {line[:-1]} ({line_letter}) ({line_punct})")
        counter += 1

with open('2.output.txt', 'w') as file:
    file.writelines("\n".join(output))