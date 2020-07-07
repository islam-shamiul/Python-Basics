try:
    age = int(input("age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("invalid input")

else:
    print("input was okey")
