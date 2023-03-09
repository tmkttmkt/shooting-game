#from pgzero.actor import Actor
from Men import *
class Stage:
      def __init__(self):
            self.mode=0
      def update(self,player):
            num=self.mens[self.mode].update(player)
            if self.mens[self.mode].mode==3:
                  self.mode=3
            return num
      def draw(self):
            self.mens[self.mode].draw()
            
class Ctenou(Stage):
      def __init__(self):
            super().__init__()
            self.mens=[Cstart()]

            

