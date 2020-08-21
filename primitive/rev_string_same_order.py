a = "this is a sentense"

x = ""
y = a.split(" ")

print(a)
"""print(len(y))
print(y[0])
z1 = y[0][::-1]
z2 = y[1][::-1]
z3 = y[2][::-1]
z4 = y[3][::-1]
print(z1+" "+z2+" "+z3+" "+z4)
"""

for z in y:
    x += z[::-1] + " "
print(x.strip())
