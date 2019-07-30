import random
a = [5,6,7,8,random.randint(0,20)]
b = []
c = 0
for _ in range(10):
    r = random.randint(0,100)
    b.append(r)
    c += r
print(b)
print(c)