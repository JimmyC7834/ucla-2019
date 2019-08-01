import math
from tkinter import *

m = Tk()
m.geometry("640x640")
m.resizable(0, 0)
c = Canvas(m, width=640, height=640)
c.configure(bg='#313628')
c.pack()

def drawLine(x,y,angle,len):
    angle = math.radians(angle)
    x2,y2 = math.cos(angle) * len, math.sin(angle) * len
    print(x2,',',y2)
    c.create_line(x,y,x + x2,y + y2,fill='white')
    return x + x2,y + y2

start_len = 100
x,y = 320,640
delta_angle = -30
start_angle = -90
x,y = drawLine(x,y,-90,start_len)
for i in range(1,100):
    print(x,y)
    x,y = drawLine(x,y,start_angle + delta_angle * i,start_len/(1.2**i))

m.mainloop()
