
for x in range(1, 101):
    if x == 1:
        print("1 is prime number")
    else:
        for y in range(2, x):
            if x % y == 0:
                print(f"{x} is not a prime number")
                break
        else:
            print(f"{x} is prime number")
