x = int(input("please enter an integer:"))
if x < 0:
    x = 0
    print('Negative to zero')
elif x == 1:
    print('One')
elif x == 0:
    print('Zero')
else:
    print('more:', x)
