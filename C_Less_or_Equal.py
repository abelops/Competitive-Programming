size, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()
if k ==0 :
    val =arr[k] -1
    if val > 0:
        print(val)
    else:
        print(-1)
elif k == size:
    print(arr[k-1])
else:
    value1 =arr[k]
    value2 = arr[k-1]
    if value1 == value2:
        print(-1)
    else:
        print(value2)
    
