
#SoftUni rocks

word = input()
symbols = {}
for ch in word:
    symbols[ch] = word.count(ch)

sort_symbols = sorted(symbols.items())
[print(f'{ch[0]}: {ch[1]} time/s') for ch in sort_symbols]
