from timeit import timeit

code1 = """def calculate_Age(age):
    if age <= 0:
        raise ValueError("invalid input")
    return 10/age


try:
    calculate_Age(0)
except ValueError as error:
    print(error)
"""

code2 = """def calculate_Age(age):
    if age <= 0:
        raise ValueError("invalid input")
    return 10/age


try:
    calculate_Age(0)
except ValueError as error:
    pass
"""

#print("first Code:", timeit(code1, number=10000))
print("2nd code:", timeit(code2, number=10000))
