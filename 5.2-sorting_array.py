def getMax(arr):
    m,index = 0,0
    for i,v in enumerate(arr):
        m,index = v if v > m else m , i if v > m else index
    return arr[index]

print(getMax([1,5,3,8,4,199,1,3,4,8,9,24]))