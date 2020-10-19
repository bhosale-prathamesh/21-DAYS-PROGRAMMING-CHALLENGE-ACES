def fibbonacci_search(arr,x):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1+ fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset=0
    while fib>1:
        i = min(offset+fib2,n)
        if a[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif a[i]>x:
            fib = fib2
            fib1 = fib1-fib2
            fib2 = fib - fib1
        else:
            return i
    return -1
