correct = 0
x = 11
y = 28
z = 6

p0 = False or True
a0 = True
if not p0 == a0:
    print("Your answer to p0 was incorrect.")
else:
    correct+=1

p1 = x <= 11 and x > -11
a1 = True
if not p1 == a1:
    print("Your answer to p1 was incorrect.")
else:
    correct+=1

p2 = (z%3) == 0
a2 = True
if not p2 == a2:
    print("Your answer to p2 was incorrect.")
else:
    correct+=1

    #True == False
p3 = y-x > 0 == x <= z
a3 = False
if not p3 == a3:
    print("Your answer to p3 was incorrect.")
else:
    correct+=1

p4 = "argon" < "zoo"
a4 = True
if not p4 == a4:
    print("Your answer to p4 was incorrect.")
else:
    correct+=1

p5 = "mass" > "massive"
a5 = False
if not p5 == a5:
    print("Your answer to p5 was incorrect.")
else:
    correct+=1

a = not True #False
b = True and False #False
c = not b or a #True

p6 = not (a and b) #True
a6 = True
if not p6 == a6:
    print("Your answer to p6 was incorrect.")
else:
    correct+=1

p7 = not a or c #True
a7 = True
if not p7 == a7:
    print("Your answer to p7 was incorrect.")
else:
    correct+=1

        #True == True and True
p8 = not a == (a or not b) and (not a or b)
a8 = True
if not p8 == a8:
    print("Your answer to p8 was incorrect.")
else:
    correct+=1


print("You got",correct,"out of 9 correct answers!")