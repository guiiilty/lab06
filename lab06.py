import itertools

def count():
    letters = ['A', 'B', 'C', 'D']
    letter1 = ['X', 'Y', 'Z']
    codewords = list(itertools.product(letter1, letters, letters, letters))
    return len(codewords)

num = count()
print(num)