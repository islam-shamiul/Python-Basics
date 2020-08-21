x = "this is a sentense"

y = ""

for z in range(len(x)-1, -1, -1):
    y += x[z]
print(y)
