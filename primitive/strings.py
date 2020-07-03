course = "Python Programming"

print(len(course))
print(course[2])
print(course[0:3])
print(course[0])
print(course[-1])
print(course[0:])
print(course[:3])

# escape sequence
test = "python \"programming again"
print(test)

test2 = "python \'programming again"
print(test2)

test3 = "python \nprogramming again"
print(test3)

# formatting string
first = "lol"
last = "man"
print(first + " " + last)
full = first+" "+last
print("as variable:", full)

# using formatter

frmt = f"{first} {last}"
print("using formatter:", frmt)
