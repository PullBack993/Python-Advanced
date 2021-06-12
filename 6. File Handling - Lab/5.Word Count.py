import re

def get_file(path_file):
    with open(path_file, 'r') as file:
        words = "".join(file.readlines())
        return re.findall(r"[a-z]+", words.lower())

path_words = 'words.txt'
path_text = 'text.txt'

first_words = get_file(path_words)
second_words = get_file(path_text)

counter = {}

for word in first_words:
    if word in second_words:
        counter[word] = second_words.count(word)

sort_words = [f'{el[0]} - {el[1]}'for el in sorted(counter.items(), key=lambda x: -x[1])]

with open('output.txt', 'w') as file:
    file.writelines('\n'.join(sort_words))