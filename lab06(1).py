x = 9**8 + 3**5 - 9
a = []
while x > 0:
    a = [x % 3] + a
    x = x//3
print(a.count(2))