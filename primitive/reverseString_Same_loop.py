a = "this is a sentense"

x = ""
y = a.split(" ")

for z in y:
    for v in range(len(z)-1, -1, -1):
        x += z[v]
    x += " "
print(x)
