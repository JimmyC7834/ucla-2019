def getMax(arr):
    m = 0
    index = 0
    for i,v in enumerate(arr):
        if v > m:
            m = v
            index = i
    return arr[index]

print(getMax([1,5,3,8,4,1,3,4,8,9,24]))