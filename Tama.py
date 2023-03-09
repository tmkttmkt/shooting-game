#from pgzero.actor import Actor
#from pgzero.keys import keys
from pgzero.keyboard import keyboard
from pgzero.clock import clock
from Player import Player
from Tamas import *
DO_HEIGHT=600
SAB_HEIGHT=200
DO_WIDTH  = 700
SAB_WIDTH  = 200
WIDTH=DO_WIDTH+SAB_WIDTH
HEIGHT = DO_HEIGHT+SAB_HEIGHT
class Tama:
    def __init__(self):
        self.lists   = []
        self.time=0
        self.next_time=0
        self.kakud=0

    def draw(self):
        for self.list in self.lists:
            self.list.draw()
    def update(self,teki):
            self.time+=1
            score=0
            num=0
            if self.time==self.next_time:
                self.oto_simple(self.yaruki)
            for self.list in self.lists:
                self.list.update()
                if self.list.x > DO_WIDTH+50 or self.list.x <-50 or self.list.y<-50 or self.list.y > DO_HEIGHT+50 :
                      self.lists.remove(self.list)
                      del self.list
                for teki.list in teki.lists:
                      if self.list.colliderect(teki.list):
                            try:
                                teki.lists.remove(teki.list)
                                teki.count+=1
                                self.lists.remove(self.list)
                            except:
                                print("list.remove(x): x not in list")
                            score+=teki.list.score
            if teki.mode==1:
                for self.list in self.lists:
                    if self.list.colliderect(teki.bosu):
                        try:
                            self.lists.remove(self.list)
                        except:
                            print("list.remove(x): x not in list")
                        teki.hp-=2
                        num+=2
            return score,num
    def pos_update(self):
        teihen=self.pos[0]-self.ppos[0]
        tatehen=self.pos[1]-self.ppos[1]
        taihen=math.sqrt((self.pos[0]-self.ppos[0])**2+(self.pos[1]-self.ppos[1])**2)
        self.kakudc=math.degrees(math.acos(teihen/taihen))
        self.kakuds=math.degrees(math.asin(teihen/taihen))            
        if tatehen>=0:
            self.kakud=-90+self.kakuds
        else:
            self.kakud=self.kakudc
        self.kakud*=-1
    def key_down(self,player):
        self.ppos=[player.x,player.y]
        self.pos_update()
        num=0
        if player.mode==1:
            if player.yaruki>5:
                player.yaruki-=5
                self.lists.append(TypeA(self.kakud,self.ppos,0.9))
                self.lists.append(TypeA(self.kakud,self.ppos,1.1))
                self.lists.append(TypeA(self.kakud,self.ppos,1))
                num=1
        elif player.mode==2:
            num=self.simple(player)
            self.next_time=self.time+20
        elif player.mode==3:
            num=self.haba(player)
        return num



    def simple(self,player):
        if player.yaruki>15:
            player.yaruki-=15
            self.lists.append(TypeA(self.kakud,self.ppos,1))
            self.lists.append(TypeB(self.kakud,self.ppos,1))
            self.lists.append(TypeC(self.kakud,self.ppos,1))
            self.kakudd=self.kakud
            self.yaruki=player.yaruki
            return 1
        return 0
    def oto_simple(self,yaruki):
        if yaruki>15: 
            yaruki-=15
            self.lists.append(TypeA(self.kakudd,self.ppos,1))
            self.lists.append(TypeB(self.kakudd,self.ppos,1))
            self.lists.append(TypeC(self.kakudd,self.ppos,1))
    
    def haba(self,player):
        if player.yaruki>20:
            player.yaruki-=20
            self.lists.append(TypeA(self.kakud,self.ppos,1))
            self.lists.append(TypeD(self.kakud,self.ppos,1))
            self.lists.append(TypeE(self.kakud,self.ppos,1))
            self.lists.append(TypeF(self.kakud,self.ppos,1))
            self.lists.append(TypeG(self.kakud,self.ppos,1))                   
            return 1
        return 0
