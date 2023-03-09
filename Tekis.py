import random
import math
from pgzero.actor import Actor
DO_HEIGHT=600
SAB_HEIGHT=200
DO_WIDTH  = 700
SAB_WIDTH  = 200
WIDTH=DO_WIDTH+SAB_WIDTH
HEIGHT = DO_HEIGHT+SAB_HEIGHT
class Tekis(Actor):
    def __init__(self,name,damage,score,x,y):
        super().__init__(name,center=(x,y))
        self.damage=damage
        self.score=score

class Char(Tekis):
    def __init__(self,x,y):
        super().__init__('char',8,2,x,y)
    def update(self):
        self.y+=2
    
class Int(Tekis):
    def __init__(self,x,y):
        super().__init__('int',8*4,1,x,y)
    def update(self):
        self.y+=random.randrange(6)
            
class Float(Tekis):
    def __init__(self,x,y):
        super().__init__('float',8*4,2,x,y)
    def update(self):
        self.x+=random.randrange(20)-10       
        self.y+=6
class Double(Tekis):
    def __init__(self,x,y):
        super().__init__('double',8*8,3,x,y)
    def update(self):
        self.x+=math.cos(math.radians(self.y*1.5)) *5  
        self.y+=5
class If(Tekis):
    def __init__(self,x,y):
        super().__init__('if',8*2,2,x,y)
    def update(self):
        self.y+=2
class Else(Tekis):
    def __init__(self,x,y):
        super().__init__('else',8*2,2,x,y)
    def update(self):
        self.y+=2
class Switch_bun(Tekis):
    def __init__(self):
        x=random.randint(1,2)
        if x==1:
            x=50
            self.pura=1
        else:
            x=DO_WIDTH-50
            self.pura=-1
        y=0
        self.error=0
        super().__init__('switch',8*6,5,x,y)
    def update(self):
        if self.pura==1:
            self.x+=2
        else:
            self.x-=2
        try:
            self.y=math.sqrt(300**2-(self.x-DO_WIDTH/2)**2)*2
        except:
            if self.error==0:
                print("math domain error")
            self.error+=1
            del self
class For(Tekis):
    def __init__(self,x,y):
        super().__init__('for',8*4,4,x,y)
        self.xp=3
    def update(self):
        self.y+=3
        if(self.y%150==0):
            self.xp*=-1
        self.x+=self.xp
class While(Tekis):
    def __init__(self,x,y):
        super().__init__('while',8*2,8,x,y)
        self.xp=5
    def update(self):
        self.y+=1
        self.x+=self.xp
        if self.x > DO_WIDTH or self.x < 0:
            self.xp*=-1
            self.x+=2*self.xp

