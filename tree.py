import math
from tkinter import *

m = Tk()
m.geometry("1000x640")
m.resizable(0, 0)
c = Canvas(m, width=1000, height=640)
c.configure(bg='#313628')
c.pack()

def drawLine(x,y,angle,len):
    angle = math.radians(angle)
    x2,y2 = math.cos(angle) * len, math.sin(angle) * len
    c.create_line(x,y,x + x2,y + y2,fill='white')
    return x + x2,y + y2

def make_tree(x,y,start_angle,delta_a,length):
    a1,a2 = start_angle + delta_angle, start_angle - delta_angle
    x1,y1 = drawLine(x,y,a1,length)
    x2,y2 = drawLine(x,y,a2,length)
    return [x1,y1],[x2,y2],a1,a2


start_len = 100
x,y = 500, 640
delta_angle = 20
start_angle = -90
clist = []
alist = [-90]
x,y = drawLine(x,y,-90,start_len)
clist.append([x,y])
for j in range(12):
    tlist = []
    talist = []
    tlen = 0
    for i,coor in enumerate(clist):
        c1,c2,a1,a2 = make_tree(coor[0],coor[1],alist[i],delta_angle,start_len/(1.25**j))
        tlist.append(c1)
        tlist.append(c2)
        talist.append(a1)
        talist.append(a2)
    clist = tlist
    alist = talist



m.mainloop()
