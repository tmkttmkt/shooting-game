
from Teki import *
class Cstart:
      def __init__(self):
            self.mode=0
            self.teki=[Hairetu(),Kouzoubun()]
      def update(self,player):
            num=self.teki[self.mode].update(player)
            if self.teki[self.mode].mode==3:
                  del self.teki[self.mode]
                  num=2
                  if len(self.teki)==0:
                        self.mode=3
            return num
      def draw(self):
            self.teki[self.mode].draw()
class CPointa:
      def __init__(self):
            self.mode=0
            self.teki=[Hairetu(),Hairetu()]
      def update(self):
            self.teki[self.mode].update()
      def draw(self):
            self.teki[self.mode].draw()
class CStruct:
      def __init__(self):
            self.mode=0
            self.teki=[Hairetu(),Hairetu()]
      def update(self):
            self.teki[self.mode].update()
      def draw(self):
            self.teki[self.mode].draw()
            
            
      
