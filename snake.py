import tkinter
import random

class grid():
    def __init__(self,size,tzise = 64):
        self.size = size
        self.tzise = tzise
        self.food_pos = [random.randint(0,size-1),random.randint(0,size-1)]
        self.COLOR = ['#595358','#A4AC96','#CADF9E']
        self.map = []
        for _ in range(size):
            row = [1 for _ in range(size)]
            self.map.append(row)
        self.update()
    
    def draw(self):
        size = self.size
        ts = self.tzise
        for r in range(size):
            for t in range(size):
                #c.create_rectangle(t,r,50,50)
                color = self.COLOR[self.map[r][t] -1]
                c.create_rectangle(ts*r+2,ts*t+2,ts*(r+1)-2,ts*(t+1)-2,fill = color, outline = color)
    
    def update(self,snake = ''):
        m = []
        for _ in range(self.size):
            row = [1 for _ in range(self.size)]
            m.append(row)
        self.map = m
        fp = self.food_pos
        self.map[fp[0]][fp[1]] = 3
        if snake != '':
            for b in snake.bodys:
                self.map[b[0]][b[1]] = 2 
            if snake.bodys[0] == self.food_pos:
                snake.score()
                self.spawn_food()

    def spawn_food(self):
        while True:
            x,y = random.randint(0,self.size-1),random.randint(0,self.size-1)
            if self.map[y][x] == 1:
                self.map[y][x] = 3
                self.food_pos = [x,y]
                break

class snake():
    def __init__(self, len, start_pos = [0,0], dir=[1,0]):
        self.bodys = []
        self._dir = dir
        for _ in range(len):
            self.bodys.append(start_pos)
    
    def update(self,grid):
        if not self.is_dead(grid):
            self.move()
        else:
            print('game over')

    def score(self):
        self.bodys.append(self.bodys[len(self.bodys)-2])

    def move(self):
        for i in range(len(self.bodys)-1,0,-1):
            self.bodys[i] = self.bodys[i-1]
        pos = self.bodys[0]
        d = self._dir
        self.bodys[0] = [pos[0] + d[0],pos[1] + d[1]]

    def is_dead(self,grid):
        b = self.bodys[0]
        d = self._dir
        if b[0] + d[0] > grid.size-1 or b[1] + d[1] > grid.size-1:
            return True
        if b[0] + d[0] < 0 or b[1] + d[1] < 0:
            return True
        return False

def up(event):
    s._dir = [0,-1] if s._dir != [0,1] else s._dir
def down(event):
    s._dir = [0,1] if s._dir != [0,-1] else s._dir
def right(event):
    s._dir = [1,0] if s._dir != [-1,0] else s._dir

def left(event):
    s._dir = [-1,0] if s._dir != [1,0] else s._dir

m = tkinter.Tk()
m.geometry("640x640")
m.resizable(0, 0)
c = tkinter.Canvas(m, width=640, height=640)
c.configure(bg='#313628')
c.pack()
m.bind('w',up)
m.bind('a',left)
m.bind('s',down)
m.bind('d',right)
g = grid(10,64)
s = snake(3)
g.spawn_food()
def task():
    s.update(g)
    g.update(s)

    g.draw()
    m.after(100,task)

m.after(100,task)
m.mainloop()