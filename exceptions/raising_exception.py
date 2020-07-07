def calculate_Age(age):
    if age <= 0:
        raise ValueError("invalid input")
    return 10/age


try:
    calculate_Age(0)
except ValueError as error:
    print(error)
