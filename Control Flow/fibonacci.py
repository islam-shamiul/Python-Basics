def fib(n):
    a, b= 0, 1
    while a<n:
        print(a,end=' ')
        a, b= b, a+b
    
f100=fib(100)
f100