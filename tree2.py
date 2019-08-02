import math
from tkinter import *

m = Tk()
m.geometry("1000x640")
m.resizable(0, 0)
c = Canvas(m, width=1000, height=640)
c.configure(bg='#313628')
c.pack()

class branch:
    def __init__(self,pos,angle,length):
        self.x = pos[0]
        self.y = pos[1]
        self.angle = angle
        self.length = length
    
    def getEnd(self):
        angle = math.radians(self.angle)
        x1,y1 = math.cos(angle) * self.length, math.sin(angle) * self.length
        return [self.x + x1,self.y + y1]
    
class tree:
    def __init__(self,x,y,delta_angle,start_len):
        self.x = x
        self.y = y
        self.age = 1
        self.delta_angle = delta_angle
        self.map = [[branch([x,y],-90,start_len)]]
    
    def grow(self):
        row = []
        for b in self.map[self.age-1]:
            row.append(branch(b.getEnd(),b.angle + self.delta_angle,b.length/1.5))
            row.append(branch(b.getEnd(),b.angle - self.delta_angle,b.length/1.5))
    
    def draw(self):
        for r in self.map:
            for b in r:
                print('as')
                end = b.getEnd()
                c.create_line(b.x,b.y,end[0],end[1],fill='white')


def drawLine(x,y,angle,len):
    angle = math.radians(angle)
    x2,y2 = math.cos(angle) * len, math.sin(angle) * len
    c.create_line(x,y,x + x2,y + y2,fill='white')

t = tree(500,600,30,100)
t.grow()
t.draw()

m.mainloop()
