from random import randint

def replaceNegatives(a2DList):
    for i,r in enumerate(a2DList):
        for i1,j in enumerate(r):
            a = 'Nope' if j < 0 else j
            a2DList[i][i1] = a
    for l in a2DList:
        print(l)

l = []
for _ in range(10):
    row = []
    for _ in range(10):
        row.append(randint(-10,10))
    l.append(row)
replaceNegatives(l)