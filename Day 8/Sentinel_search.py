def sentinel_search(arr,x):
    n = len(arr)
    arr.append(x)
    i=0
    while True:
        if arr[i] == x:
            loc = i
            break
        i += 1
    if loc > n-1:
        return -1
    return loc
    
arr = [1,6,2,9,5,3]

print(setinel_search(arr,5))
