from pgzero.actor import Actor
import math
class Tamas(Actor):
      def __init__(self,name,kakud,pos,speed):
            super().__init__(name,pos)
            self.xp=math.cos(math.radians(kakud))*4*speed
            self.yp=math.sin(math.radians(kakud))*4*speed
            self.kakud=math.radians(kakud)
            self.angle+=2
      def update(self):
            self.x += self.xp
            self.y += self.yp

class TypeA(Tamas):
      def __init__(self,kakud,pos,speed):
            super().__init__('typea',kakud,pos,speed)

class TypeB(Tamas):
      def __init__(self,kakud,pos,speed):
            super().__init__('typea',kakud,pos,speed)
            self.time=0
      def update(self):
            self.time+=1
            self.x += self.xp
            self.y += self.yp
            bure=math.cos(math.radians(self.time*5))*5
            self.y-=math.cos(self.kakud)*bure
            self.x+=math.sin(self.kakud)*bure
class TypeC(TypeB):
      def __init__(self,kakud,pos,speed):
            super().__init__(kakud,pos,speed)
      def update(self):
            self.time+=1
            self.x += self.xp
            self.y += self.yp
            bure=math.cos(math.radians(self.time*5))*5
            self.y+=math.cos(self.kakud)*bure
            self.x-=math.sin(self.kakud)*bure
class TypeD(Tamas):
      def __init__(self,kakud,pos,speed):
            super().__init__('typea',kakud,pos,speed)
            self.time=0
      def update(self):
            self.time+=1
            self.x += self.xp
            self.y += self.yp
            bure=self.time*self.time*0.01
            self.y+=math.cos(self.kakud)*bure
            self.x-=math.sin(self.kakud)*bure
class TypeE(Tamas):
      def __init__(self,kakud,pos,speed):
            super().__init__('typea',kakud,pos,speed)
            self.time=0
      def update(self):
            self.time+=1
            self.x += self.xp
            self.y += self.yp
            bure=self.time*self.time*0.01
            self.y-=math.cos(self.kakud)*bure
            self.x+=math.sin(self.kakud)*bure
class TypeF(Tamas):
      def __init__(self,kakud,pos,speed):
            super().__init__('typeb',kakud,pos,speed)
            self.time=0
      def update(self):
            self.time+=1
            self.x += self.xp
            self.y += self.yp
            bure=self.time*0.1
            self.y+=math.cos(self.kakud)*bure
            self.x-=math.sin(self.kakud)*bure
class TypeG(Tamas):
      def __init__(self,kakud,pos,speed):
            super().__init__('typeb',kakud,pos,speed)
            self.time=0
      def update(self):
            self.time+=1
            self.x += self.xp
            self.y += self.yp
            bure=self.time*0.1
            self.y-=math.cos(self.kakud)*bure
            self.x+=math.sin(self.kakud)*bure



            
