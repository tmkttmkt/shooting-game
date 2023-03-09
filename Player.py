from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.music import pause
DO_HEIGHT=600
SAB_HEIGHT=200
DO_WIDTH  = 700
SAB_WIDTH  = 200
WIDTH=DO_WIDTH+SAB_WIDTH
HEIGHT = DO_HEIGHT+SAB_HEIGHT
error=Actor('error')
class Player(Actor):
      def __init__(self,yaruki):
            super().__init__('player',center=(HEIGHT/2,WIDTH/2))
            self.mode=2
            self.max_yaruki=yaruki
            self.yaruki=self.max_yaruki
            self.haba=35
            self.lift_time=self.time=0
            self.a=0
            self.score=0
            self.tairyoku=99
      def draw(self):
            super().draw()
            if self.mode==0:
                  error.draw()
      def update(self):
            if self.yaruki<self.max_yaruki:
                  self.yaruki+=0.3
            self.time+=1
            if keyboard.w:
                  if(self.y>self.haba):
                        self.y -= 5
            if keyboard.s:
                  if(self.y<DO_HEIGHT-self.haba):
                        self.y += 5
            if keyboard.a:
                  if(self.x>self.haba):
                        self.x -= 5
            if keyboard.d:
                  if(self.x<DO_WIDTH-self.haba):
                        self.x += 5
            if self.mode==0:
                  if self.time==self.lift_time:
                        self.mode=1
                        self.a+=1
                  error.y=self.y
                  error.x=self.x
      def mouse_down(self,updown):
            if self.mode>0:
                  self.mode+=updown
                  if self.mode>=4:
                        self.mode-=3
                  if self.mode<=0:
                        self.mode+=3

                  
      def taiatari(self,damage):
            self.yaruki-=damage
            if(self.yaruki<0):
                  self.yaruki=0
            self.mode=0
            self.tairyoku-=damage/10
            if self.tairyoku<0:
                  self.mode=-1
                  pause()
            else:
                  self.lift_time=self.time+60
            
      
            
                  
      
