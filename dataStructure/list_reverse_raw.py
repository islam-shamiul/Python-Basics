a = [1, 2, 3, 4, 5]
b = []

for n in range(len(a)-1, -1, -1):
    b.append(a[n])

a = b
print(a)
