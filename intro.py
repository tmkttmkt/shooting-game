import pgzrun
from Stage import *
from Teki import *
from Tama import Tama
from Player import Player

class butan:
    def __init__(self):
        self.BOX=(200,0,0)
        self.CLORE=Rect((20, 20), (100, 100))
    def draw(self):
        screen.draw.rect(self.BOX,self.CLORE)
    def mouse_down(self):
        self.collidepoint


DO_HEIGHT=600
SAB_HEIGHT=200
DO_WIDTH  = 700
SAB_WIDTH  = 200
WIDTH=DO_WIDTH+SAB_WIDTH
HEIGHT = DO_HEIGHT+SAB_HEIGHT


stage=Ctenou()
tama=Tama()
player=Player(120)
time=0
TITLE='GENGO'
tmode=0
mmode=0
gmode=0
set_time=0
up_dwon_flg=1
gmcolor=(0,0,0)
class Story:
    def __init__(self,name,bun):
        self.rogo=Actor("rogo/"+name,center=(100,DO_HEIGHT+100))
        self.txt=""
        self.txtu=""
        self.input=bun
        self.i=0
        self.mode=1
    def draw(self):
        self.rogo.draw()
        screen.draw.rect(Rect((150,DO_HEIGHT+50), (DO_WIDTH,150)),(255,255,255))
        screen.draw.text(str(self.txt),(150,DO_HEIGHT+50-10),fontname='genshingothic-bold.ttf',color=(0,0,0),fontsize=50)
        screen.draw.text(str(self.txtu),(150,DO_HEIGHT+100-10),fontname='genshingothic-bold.ttf',color=(0,0,0),fontsize=50)
    def update(self):

        if self.i>13:
            self.mode=2
        if self.mode!=0:
            try:
                if self.input[self.i]==" ":
                    self.txt+=self.input[self.i]
                    self.i+=1
                if self.mode==1:
                    self.txt+=self.input[self.i]
                    sounds.chart.play()
                    self.i+=1
                else:
                    self.txtu+=self.input[self.i]
                    sounds.chart.play()
                    self.i+=1
            except:
                self.mode=0
class Start:
    def __init__(self):
        music.play('first.wav')
    def draw(self):
        screen.draw.text("GENGO",(WIDTH/2-200,HEIGHT/3),fontname='fugazone_regular.ttf',color=(0,0,0),fontsize=100)
        #screen.draw.text("",(WIDTH/2+100,HEIGHT/3),fontname='nicokaku.ttf',color=(0,0,0),fontsize=20)
        screen.draw.filled_rect(Rect((DO_WIDTH/2-120,DO_HEIGHT/2+100), (240,60)), (64,64,64))
        screen.draw.text("START",(DO_WIDTH/2-120,DO_HEIGHT/2+100),color="BLACK",fontsize=40)
        screen.draw.filled_rect(Rect((DO_WIDTH/2-120,DO_HEIGHT/2+170), (240,60)), (64,64,64))
        screen.draw.text("CONTINUATION",(DO_WIDTH/2-120,DO_HEIGHT/2+170),color="BLACK",fontsize=40)
        screen.draw.filled_rect(Rect((DO_WIDTH/2-120,DO_HEIGHT/2+240), (240,60)), (64,64,64))
        screen.draw.text("EXPLANATION",(DO_WIDTH/2-120,DO_HEIGHT/2+240),color="BLACK",fontsize=40)
    def key_down(self,pos):
        global tmode,mmode,story,bun,bun_num
        if(pos[0]>DO_WIDTH/2-120 and pos[0]<DO_WIDTH/2+120):
            if(pos[1]>(DO_HEIGHT/2+100) and pos[1]<(DO_HEIGHT/2+100)+60):
                music.play('main.wav')
                bun_num=1
                story=Story("c",bun[1])
                tmode=3
                mmode=1
            if(pos[1]>(DO_HEIGHT/2+170) and pos[1]<(DO_HEIGHT/2+170)+60):
                tmode=2
            if(pos[1]>(DO_HEIGHT/2+240) and pos[1]<(DO_HEIGHT/2+240)+60):
                tmode=1
class HPbar:
    def __init__(self,maxhp):
        self.hp=maxhp
        self.maxhp=maxhp
    def draw(self):
        if self.maxhp!=0:
            screen.draw.filled_rect(Rect((100,0), (500,15)),"RED")
            screen.draw.filled_rect(Rect((100,0), (500*self.hp/self.maxhp,15)),"GREEN")
    def damege(self,damege):
        self.hp-=damege
        if self.hp<0:
            self.hp=0
            
bun=["","","",""]
bun[1]="Cごときを倒せないないならプログラマをやめちまえ"
bun[2]="いまチャーって言ったな！今言ったな！．死んでくれ"
bun[3]="制御文こそプログラム．．．いやアルゴリズムの中核だ！"
rogo=["mu","","",""]
rogo[1]="c"
rogo[2]="haireru"
rogo[3]="pointa"
hpbar=HPbar(0)
start=Start()
bun_num=1
story=Story(rogo[bun_num],bun[bun_num])
EX_BUN="char 一バイトの型、文字を格納する\n"
EX_BUN+="int 四バイトの型、整数を格納する\n"
EX_BUN+="float 四バイトの型、実数を格納する\n"
EX_BUN+="double 八バイトの型、大きな実数を格納する\n\n"
EX_BUN+="charは当たると,あchar(チャー)って感じにな\nるので気を付けよう\n"
EX_BUN+="\n\n   charこそが正義\n"
EX_BUN+="                      stringなんでねえよ\n"
EX_BUN+="                                          by肩幅C言語\n"
def sub_draw():
    screen.draw.filled_rect(Rect((0,DO_HEIGHT), (WIDTH,HEIGHT)), (64,64,64))
    screen.draw.filled_rect(Rect((DO_WIDTH,0), (SAB_WIDTH,DO_HEIGHT)), (128,128,128))
    screen.draw.filled_rect(Rect((DO_WIDTH,50), (35,210)),"RED")
    screen.draw.filled_rect(Rect((DO_WIDTH,50), (35,210*player.yaruki/player.max_yaruki)),"GREEN")
    screen.draw.text("KI\nAI",(DO_WIDTH,0),color="BLACK",fontsize=40)
    screen.draw.filled_rect(Rect((DO_WIDTH+50,50), (35,210)),"RED")
    screen.draw.filled_rect(Rect((DO_WIDTH+50,50), (35,210*player.tairyoku/100)),"GREEN")
    screen.draw.text("TAI\nRYOKU",(DO_WIDTH+50,0),color="BLACK",fontsize=40)
    screen.draw.text("SCORE:"+str(player.score),(DO_WIDTH,260),color="BLACK",fontsize=50)
    if player.mode>0:
        screen.draw.text("MODE:"+str(player.mode),(DO_WIDTH,340),color="BLACK",fontsize=50)
    story.draw()

def draw():
    if tmode==0:
        screen.fill((128, 0, 0))
        start.draw()
    elif tmode==2:
        screen.fill(( 0,128, 0))
        screen.draw.text("未実装です\nNULLです\nマウスクリックして\n戻りください",(0,HEIGHT/3),fontname='genshingothic-bold.ttf',color="BLACK",fontsize=70)
    elif tmode==1:
        screen.fill((255,255,255))
        screen.draw.text(EX_BUN,(0,0),fontname='genshingothic-bold.ttf',color="BLACK",fontsize=43)
    elif tmode==3:
        screen.clear()
        if mmode ==-2:
            screen.fill("RED")
            screen.draw.text("GAMECLEAR",(DO_WIDTH/2-120,DO_HEIGHT/2-100),color=gmcolor,fontsize=140,owidth=2, ocolor="BLACK")
            screen.draw.text("SCORE:"+str(player.score),(DO_WIDTH/2,DO_HEIGHT/2+170),color="BLACK",fontsize=80)
        elif mmode!=0:
            stage.draw()
            player.draw()
            tama.draw()
            sub_draw()
            if gmode==1:
                hpbar.draw()
            if player.mode==-1:
                screen.clear()
                screen.draw.text("GAMEOVER",(DO_WIDTH/2-120,DO_HEIGHT/2-100),gcolor="RED",fontsize=100)
                screen.draw.text("RERTURN\nMENY",(DO_WIDTH/2-120,DO_HEIGHT/2-30),color=(255,255,255),fontsize=60)

            elif mmode<0:
                screen.draw.filled_rect(Rect((DO_WIDTH/2-120,DO_HEIGHT/2-110), (240,220)), (0,0,255))
                screen.draw.filled_rect(Rect((DO_WIDTH/2-100,DO_HEIGHT/2-100), (200,60)), (64,64,64))
                screen.draw.text("MENY",(DO_WIDTH/2-100,DO_HEIGHT/2-100),color="BLACK",fontsize=40)
                screen.draw.filled_rect(Rect((DO_WIDTH/2-100,DO_HEIGHT/2-30), (200,60)), (64,64,64))
                screen.draw.text("MENY",(DO_WIDTH/2-100,DO_HEIGHT/2-30),color="BLACK",fontsize=40)
                screen.draw.filled_rect(Rect((DO_WIDTH/2-100,DO_HEIGHT/2+40), (200,60)), (64,64,64))
                screen.draw.text("RETURN",(DO_WIDTH/2-100,DO_HEIGHT/2+40),color="BLACK",fontsize=40)
            
                

        
        
    
def update():
    global up_dwon_flg,time,set_time,tmode,mmode,gmode,gmcolor,bun,rogo,bun_num,story,hpbar
    time+=1
    if mmode==-2 and time%4==0:
        r=random.randrange(255)
        g=random.randrange(255)
        b=random.randrange(255)
        gmcolor=(r,g,b)
    if mmode>0:
        if player.mode!=-1:
            num=stage.update(player)
            if num==2:
                story=Story(rogo[0],bun[0])
                gmode=0
                hpbar=HPbar(0)
            if num>2:
                bun_num+=1
                story=Story(rogo[bun_num],bun[bun_num])
                hpbar=HPbar(num)
                gmode=1
            player.update()
            try:
                box=tama.update(stage.mens[stage.mode].teki[stage.mens[stage.mode].mode])
                score=box[0]
                if gmode==1:
                    hpbar.damege(box[1])
                player.score+=score
            except:
                print(" list index out of range")
            if time%10==0:
                story.update()
            if stage.mode==3:
                mmode=-2
    if time==set_time:
        up_dwon_flg=1


        
def on_key_down(key):
    global mmode
    if key==keys.SPACE:
        num=tama.key_down(player)
        if num==1:
            sounds.short.play()  
    if key==keys.ESCAPE:
        mmode*=-1
def on_mouse_move(pos):
    global tmode
    if tmode==3:
        tama.pos=pos
    
        
        
def on_mouse_down(pos,button):
    try:
        global up_dwon_flg,time,tmode,mmode,player,tama,stage,set_time,show_score,hpbar
    except:
        global up_dwon_flg,time,mmode
    if button==mouse.LEFT or button==mouse.RIGHT:
        if mmode==0:
            tama=Tama()
            player=Player(60)
            hpbar=HPbar(0)
            stage=Ctenou()
        if player.mode==-1:
            tmode=0
            music.play('first.wav')
            mmode=0
            show_score=player.score
            del player,tama,stage,hpbar
        elif(mmode<0 and pos[0]>DO_WIDTH/2-100 and pos[0]<(DO_WIDTH/2-100)+200):
            if(pos[1]>(DO_HEIGHT/2-100) and pos[1]<(DO_HEIGHT/2-100)+60):
                mmode=0
                music.play('first.wav')
                tmode=0
            if(pos[1]>(DO_HEIGHT/2-30) and pos[1]<(DO_HEIGHT/2-30)+60):
                mmode=0
                music.play('first.wav')
                tmode=0
            if(pos[1]>(DO_HEIGHT/2+40) and pos[1]<(DO_HEIGHT/2+40)+60):
                mmode*=-1
        elif(tmode==0 and pos[0]>DO_WIDTH/2-120 and pos[0]<DO_WIDTH/2+120):
            start.key_down(pos)
        elif tmode==1 or tmode==2:
            tmode=0
        elif mmode==-2:
            tmode=0
            mmode=0

    elif up_dwon_flg==1 and mmode>0:
        if button==mouse.WHEEL_UP:
            up_dwon_flg=0
            set_time=time+20
            player.mouse_down(1)
        if button==mouse.WHEEL_DOWN:
            up_dwon_flg=0
            set_time=time+20
            player.mouse_down(-1)



pgzrun.go()
"""
C:\ProgramData\Anaconda3\Lib\site-packages\pygame
C:\ProgramData\Anaconda3\Lib\site-packages\pgzero

C:/Program Files/Python37/Lib/site-packages/pgzero/__pycache__
C:/Program Files/Python37/Lib/site-packages/pgzero/data

C:/Program Files/Python37/Lib/site-packages/pgzero/__init__.py
C:/Program Files/Python37/Lib/site-packages/pgzero/__main__.py
C:/Program Files/Python37/Lib/site-packages/pgzero/actor.py
C:/Program Files/Python37/Lib/site-packages/pgzero/animation.py
C:/Program Files/Python37/Lib/site-packages/pgzero/builtins.py
C:/Program Files/Python37/Lib/site-packages/pgzero/clock.py
C:/Program Files/Python37/Lib/site-packages/pgzero/constants.py
C:/Program Files/Python37/Lib/site-packages/pgzero/game.py
C:/Program Files/Python37/Lib/site-packages/pgzero/keyboard.py
C:/Program Files/Python37/Lib/site-packages/pgzero/loaders.py
C:/Program Files/Python37/Lib/site-packages/pgzero/music.py
C:/Program Files/Python37/Lib/site-packages/pgzero/ptext.py
C:/Program Files/Python37/Lib/site-packages/pgzero/rect.py
C:/Program Files/Python37/Lib/site-packages/pgzero/runner.py
C:/Program Files/Python37/Lib/site-packages/pgzero/screen.py
C:/Program Files/Python37/Lib/site-packages/pgzero/soundfmt.py
C:/Program Files/Python37/Lib/site-packages/pgzero/spellcheck.py
C:/Program Files/Python37/Lib/site-packages/pgzero/tone.py




"""

