sequence = input()

stack = []

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
}

success = True
for el in sequence:
    if el in pairs.keys():
        stack.append(el)

    elif el in pairs.values():
        if not stack:
            success = False
            break
        opening = stack.pop()
        if not pairs[opening] == el:
            success = False
            break

if success:
    print('YES')
else:
    print('NO')