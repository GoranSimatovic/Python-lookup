def fibonacci(n):
    a=0
    b=1
    i=0
    while i < n:
        print(a)
        print(b)
        a = a+b
        b = a+b
        i=i+1
