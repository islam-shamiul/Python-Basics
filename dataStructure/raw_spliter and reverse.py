st = "this is a string with space"
temp = []
rev = ""
last_pos = 0
for i in range(0, len(st), 1):
    if (st[i] == " "):
        temp.append(st[last_pos:i])
        last_pos = i+1
temp.append(st[last_pos:])
print(temp)
print(temp[1])

for j in range(len(temp)-1, -1, -1):
    if j >= 1:
        rev += temp[j]+" "
    else:
        rev += temp[j]
print(rev)
