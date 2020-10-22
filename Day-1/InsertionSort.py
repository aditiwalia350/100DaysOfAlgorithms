arr = [7, 4, 3, 1, 2, 6, 5]
for i in range(1, len(arr)):
    for j in range(i-1, -1, -1):
        if arr[j] > arr[i]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i=j
print(arr)


