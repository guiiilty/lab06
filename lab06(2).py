count = 0

for letter1 in ['X', 'Y', 'Z']:
    for letter2 in ['A', 'B', 'C', 'D']:
        for letter3 in ['A', 'B', 'C', 'D']:
            for letter4 in ['A', 'B', 'C', 'D']:
                word = letter1 + letter2 + letter3 + letter4
                count += 1

print(count)