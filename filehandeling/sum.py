sum = 0
a = open("test.txt", "w")

data = """this is test file 123
          another line 456"""
a.write(data)
a.close()

b = open("test.txt", "r+")
contents = b.readlines()

for line in contents:
    for char in line:
        if char.isdigit() == True:
            sum += int(char)
message = (f"\nthe sum is {sum}")
b.write(message)
b.close()
