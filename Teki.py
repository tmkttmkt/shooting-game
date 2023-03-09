from pgzero.actor import Actor
from Tekis import *
from Player import Player
import math
DO_HEIGHT=600
SAB_HEIGHT=200
DO_WIDTH  = 700
SAB_WIDTH  = 200
WIDTH=DO_WIDTH+SAB_WIDTH
HEIGHT = DO_HEIGHT+SAB_HEIGHT
class Teki:
    def __init__(self):
        self.lists   = []
        self.time=0
        self.count=0
        self.mode=0
    def update(self,player):
        self.time+=1
        for self.list in self.lists:
            self.list.update()
            if(self.list.x>DO_WIDTH or self.list.x<0 or self.list.y>DO_HEIGHT):
                self.lists.remove(self.list)
                del self.list
                continue
            if player.colliderect(self.list):
                self.lists.remove(self.list)
                player.taiatari(self.list.damage)
                del self.list
    def draw(self):
        for self.list in self.lists:
            self.list.draw()
        if self.mode==1:
            self.bosu.draw()

class Hairetu(Teki):
    def __init__(self):
        super().__init__()
    def update(self,player):
        super().update(player)
        sun=0
        if self.count>50:
            if self.mode==0:  
                self.mode=1
                sun=70
                self.bosu=Actor("haireru",center=(DO_HEIGHT/2,50))
                self.hp=70
            if self.hp<0:
                self.mode=3
            if self.time%400==0:
                for x in range(-75, 75+30, 30):
                    for y in range(-25, 25+20, 20):
                        self.lists.append(Char(self.bosu.x+x,self.bosu.y+y))
            if self.time%400==200:
                for x in range(0,DO_WIDTH, 30):
                        self.lists.append(Int(x,0))
            self.bosu.x+=math.sin(math.radians(self.time*0.73))*1.8
            
        if self.time%30==0:
            self.lists.append(Char(random.randrange(DO_WIDTH),0))
        if self.time%40==0:
            self.lists.append(Int(random.randrange(DO_WIDTH),0))
        if self.time%60==0:
            self.lists.append(Float(random.randrange(DO_WIDTH),0))
        if self.time%60==0:
            self.lists.append(Double(random.randrange(DO_WIDTH),0))
        return sun

class Kouzoubun(Teki):
    def __init__(self):
        super().__init__()
    def update(self,player):
        super().update(player)
        sun=0
        if self.time%120==0:
            self.lists.append(Char(random.randrange(DO_WIDTH),0))
        if self.time%40==0:
            self.lists.append(Int(random.randrange(DO_WIDTH),0))
        if self.count>50:
            if self.time%60==0:
                x=random.randrange(DO_WIDTH)
                self.lists.append(If(x,0))
                self.lists.append(Else(x+50,0))
            if self.mode==0:  
                self.mode=1
                self.bosu=Actor("kouzoubun",center=(DO_HEIGHT/2,50))
                sun=64
                self.hp=64
            if self.hp<0:
                self.mode=3
            if self.time%180<24*2 and self.time%2==0:
                self.lists.append(If((self.time%180/2)*30,0))
            if self.time%400<35*5 and self.time%5==0:
                self.lists.append(For(DO_WIDTH-(self.time%400/5)*50,0))
                self.lists.append(For(DO_WIDTH-(self.time%400/5+1)*50,0))
                self.lists.append(For(DO_WIDTH-(self.time%400/5+2)*50,0))
            if self.time%180==0:
                self.lists.append(While(random.randrange(DO_WIDTH),0))
            if self.time%10==0:
                num=random.randint(1,4)
                if num==1:
                    self.bosu.x+=20
                if num==2:
                    self.bosu.x-=20
                if num==3:
                    self.bosu.x+=4
                if num==4:
                    self.bosu.x-=4
        else:
            if self.time%60==0:
                self.lists.append(If(random.randrange(DO_WIDTH),0))
            if self.time%123==0:
                self.lists.append(Switch_bun())
            if self.time%90==0:
                self.lists.append(While(random.randrange(DO_WIDTH),0))
            if self.time%30==20:
                self.lists.append(For(random.randrange(DO_WIDTH),0))
        return sun

            

            

class Kansu(Teki):
    def __init__(self):
        super().__init__()
    def update(self):
        super().update()
class Pointa(Teki):
    def __init__(self):
        super().__init__()
    def update(self):
        super().update()
class Struct(Teki):
    def __init__(self):
        super().__init__()
    def update(self):
        super().update()
