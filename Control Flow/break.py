for x in range(2,10):
    for n in range(2,x):
        if x%n==0:
            print(x,'is not a prime number')
            break #here the nested loop exits
    else:
        print(x,'is a prime number')
