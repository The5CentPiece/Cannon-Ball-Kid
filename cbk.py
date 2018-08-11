import os
os.environ['SDL_VIDEO_WINDOW_POS']='%d, %d' % (0,0)
levelImp=[]
for lv in range(2):
    levelImp.append(__import__(str.format("level{}",lv), globals(), locals(), [], 0))
    lv+=1
import pygame, sys, time, ctypes, math, spriteClasses
from PIL import Image

class Main():
    def __init__(self):
        self.sw=ctypes.windll.user32.GetSystemMetrics(0)
        self.sh=ctypes.windll.user32.GetSystemMetrics(1)
        self.playing=1
        self.speed=1
        self.quick=.015
        self.rolling=0
        self.cooldown=0
        self.facing=1
        self.jumping=0
        self.still=1
        self.rt=0
        self.lt=0
        self.stuck=0
        self.screen=pygame.display.set_mode((self.sw,self.sh),pygame.NOFRAME)
        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert
        self.screen_color=(0,0,0)
        self.plyry=840
        self.cloudx=0
        self.bGColor=[221,253,255]
        self.clock=pygame.time.Clock()
        self.plyr=pygame.image.load("Images/cannonBallKid.png")
        self.clouds=pygame.image.load("Images/clouds.png")
        self.cloudsTwo=pygame.image.load("Images/clouds.png")
        self.ship=pygame.image.load("Images/ship.png")
        self.shipTwo=pygame.image.load("Images/ship.png")
        self.wood=pygame.image.load("Images/wood.png")
        self.metal=pygame.image.load("Images/metal.png")
        self.spike=pygame.image.load("Images/spike.png")
        self.cannon=pygame.image.load("Images/cannon.png")
        self.shipx=0
        self.mapPos=0
        self.levelOn=[]
        while True:
            try:
                i
            except NameError:
                i=0
            if str.format("level{}",i) not in sys.modules:
                break
            else:
                self.levelOn.append(eval(str.format("levelImp[{}].level{}()",i,i)))
                i+=1
        self.level=0
        #objects for sprite classes
        self.kiddo=spriteClasses.kiddo(self.plyry)


        self.obstruction=[0,0,0,0]


    def runGame(self):
        pygame.init()
        self.setLevel(str.format("self.levelOn[{}]",self.level))
        self.move(str.format("self.levelOn[{}]",self.level))
        while True:
            self.clock.tick(60)
            #movement
            events=pygame.event.get()
            key=pygame.key.get_pressed()
            if self.playing==1:
                if key[pygame.K_SPACE] and self.rolling==0 and self.jumping==0 and self.stuck==0:
                    self.jumping=1
                    self.still=0
                    for i in range(24):
                        if self.facing==1:
                            self.plyr=pygame.image.load("Images/cannonBallKidJumpR.png")
                        else:
                            self.plyr=pygame.image.load("Images/cannonBallKidJumpL.png")
                        if i<6:
                            self.plyry=self.plyry-30
                        elif i<9:
                            self.plyry=self.plyry-25
                        elif i<12:
                            self.plyry=self.plyry-15
                        elif i<15:
                            self.plyry=self.plyry+15
                        elif i<18:
                            self.plyry=self.plyry+25
                        else:
                            self.plyry=self.plyry+30
                        self.walking()
                        self.move(str.format("self.levelOn[{}]",self.level))
                        i=i+1
                        time.sleep(self.quick)
                    self.jumping=0
                if key[pygame.K_d] and key[pygame.K_s] and key[pygame.K_a]==0 and self.rolling==0 and self.cooldown<=0:
                    self.rolling=1
                    self.facing=1
                    self.still=0
                    self.plyry=self.plyry+30
                    for i in range(16*self.speed):
                        if i % self.speed == 0 :
                            self.plyr=Image.open("cannonBallKidRollR.png")
                            self.plyr=self.plyr.rotate(-22.5*(i/self.speed))
                        self.plyr=pygame.image.fromstring(self.plyr.tobytes("raw", 'RGBA'),(32,32),'RGBA')
                        self.cloudx=self.cloudx-3/self.speed
                        self.shipx=self.shipx-15/self.speed
                        self.mapPos=self.mapPos-15/self.speed
                        self.move(str.format("self.levelOn[{}]",self.level))
                        i=i+1
                        time.sleep(self.quick)
                    self.plyry=self.plyry-30
                    self.rolling=0
                    self.cooldown=50

                if key[pygame.K_a] and key[pygame.K_s] and key[pygame.K_d]==0 and self.rolling==0 and self.cooldown<=0:
                    self.rolling=1
                    self.facing=1
                    self.still=0
                    self.plyry=self.plyry+30
                    for i in range(16*self.speed):
                        if i % self.speed == 0 :
                            self.plyr=Image.open("Images/cannonBallKidRollL.png")
                            self.plyr=self.plyr.rotate(22.5*(i/self.speed))
                        self.plyr=pygame.image.fromstring(self.plyr.tobytes("raw", 'RGBA'),(32,32),'RGBA')
                        self.cloudx=self.cloudx+3/self.speed
                        self.shipx=self.shipx+15/self.speed
                        self.mapPos=self.mapPos+15/self.speed
                        self.move(str.format("self.levelOn[{}]",self.level))
                        i=i+1
                        time.sleep(self.quick)
                    self.plyry=self.plyry-30
                    self.rolling=0
                    self.cooldown=50
                if self.cooldown>0:
                    self.cooldown=self.cooldown-1

                self.walking()

            for event in events:
                if event.type==pygame.QUIT:
                    sys.exit()


            pygame.display.update()

    def setLevel(self, levelNum):
        self.layout=eval(levelNum+".layout")
        self.woodRect = []
        self.metalRect = []
        self.spikeRect = []
        self.cannonRect = []
        for i in range(len(self.layout)):
            for j in range(len(eval(levelNum+".row1"))):
                posNum=eval(levelNum+(str.format(".row{}[{}]",i,j)))
                if posNum==1:
                    spriteClasses.block(self.woodRect,j*80+self.mapPos,i*80)
                if posNum==2:
                    spriteClasses.block(self.metalRect,j*80+self.mapPos,i*80)
                if posNum==3:
                    spriteClasses.spike(self.spikeRect,j*80+self.mapPos,i*80)
                if posNum==4:
                    spriteClasses.cannon(self.cannonRect,j*80+self.mapPos,i*80)
                j+=1
            i+=1


    def move(self, levelNum):
        self.screen.fill(self.bGColor)
        if((self.sw/1920)>(self.sh/1080)):
            #like an ultrawide
            self.clouds = pygame.transform.scale(self.clouds,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.cloudsTwo = pygame.transform.scale(self.cloudsTwo,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.ship = pygame.transform.scale(self.ship,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.shipTwo = pygame.transform.scale(self.shipTwo,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.plyr = pygame.transform.scale(self.plyr,(math.floor(self.sh*4/27),math.floor(self.sh*4/27)))
            self.wood = pygame.transform.scale(self.wood,(math.floor(80*(self.sh*16/9)/1920),math.floor(80*(self.sh)/1080)))
            self.metal = pygame.transform.scale(self.metal,(math.floor(80*(self.sh*16/9)/1920),math.floor(80*(self.sh)/1080)))
            self.spike = pygame.transform.scale(self.spike,(math.floor(80*(self.sh*16/9)/1920),math.floor(80*(self.sh)/1080)))
            self.cannon = pygame.transform.scale(self.cannon,(math.floor(160*(self.sh*16/9)/1920),math.floor(160*(self.sh)/1080)))


            self.screen.blit(self.clouds, (self.cloudx*((self.sh*16/9)/1920),0))
            if self.cloudx<=0:
                self.screen.blit(self.cloudsTwo, ((self.cloudx*((self.sh*16/9)/1920)+self.sh*(16/9)),0))
            else:
                self.screen.blit(self.cloudsTwo, ((self.cloudx*((self.sh*16/9)/1920)-self.sh*(16/9)),0))

            for i in range(len(self.layout)):
                for j in range(len(eval(levelNum+".row1"))):
                    posNum=eval(levelNum+(str.format(".row{}[{}]",i,j)))
                    if posNum==1:
                        self.screen.blit(self.wood, ((j*80+self.mapPos)*((self.sh*16/9)/1920),i*80*((self.sh*16/9)/1920)))
                    if posNum==2:
                        self.screen.blit(self.metal, ((j*80+self.mapPos)*((self.sh*16/9)/1920),i*80*((self.sh*16/9)/1920)))
                    if posNum==3:
                        self.screen.blit(self.spike, ((j*80+self.mapPos)*((self.sh*16/9)/1920),i*80*((self.sh*16/9)/1920)))
                    if posNum==4:
                        self.screen.blit(self.cannon, ((j*80+self.mapPos)*((self.sh*16/9)/1920),i*80*((self.sh*16/9)/1920)))
                    j+=1
                i+=1
            self.screen.blit(self.plyr, (math.floor(self.sh*(16/9)*(23/54)),math.floor(self.plyry*self.sh)))
            self.screen.blit(self.ship, (self.shipx*((self.sh*16/9)/1920),math.floor(955*self.sh)))
            if self.shipx<=0:
                self.screen.blit(self.shipTwo, ((self.shipx*((self.sh*16/9)/1920)+self.sh*(16/9)),math.floor(955*self.sh)))
            else:
                self.screen.blit(self.shipTwo, ((self.shipx*((self.sh*16/9)/1920)-self.sh*(16/9)),math.floor(955*self.sh)))

        else:
            self.clouds = pygame.transform.scale(self.clouds,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.cloudsTwo = pygame.transform.scale(self.cloudsTwo,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.ship = pygame.transform.scale(self.ship,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.shipTwo = pygame.transform.scale(self.shipTwo,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.plyr = pygame.transform.scale(self.plyr,(math.floor(self.sw/12),math.floor(self.sw/12)))
            self.wood = pygame.transform.scale(self.wood,(math.floor(80*(self.sw)/1920),math.floor(80*(self.sw*9/16)/1080)))
            self.metal = pygame.transform.scale(self.metal,(math.floor(80*(self.sw)/1920),math.floor(80*(self.sw*9/16)/1080)))
            self.spike = pygame.transform.scale(self.spike,(math.floor(80*(self.sw)/1920),math.floor(80*(self.sw*9/16)/1080)))
            self.cannon = pygame.transform.scale(self.cannon,(math.floor(160*(self.sw)/1920),math.floor(160*(self.sw*9/16)/1080)))


            self.screen.blit(self.clouds, (self.cloudx*(self.sw/1920),0))
            if self.cloudx<=0:
                self.screen.blit(self.cloudsTwo, (self.cloudx*(self.sw/1920)+self.sw,0))
            else:
                self.screen.blit(self.cloudsTwo, (self.cloudx*(self.sw/1920)-self.sw,0))
            for i in range(len(self.layout)):
                for j in range(len(eval(levelNum+".row1"))):
                    posNum=eval(levelNum+(str.format(".row{}[{}]",i,j)))
                    if posNum==1:
                        self.screen.blit(self.wood, ((j*80+self.mapPos)*(self.sw/1920),i*80*((self.sw)/1920)))
                    if posNum==2:
                        self.screen.blit(self.metal, ((j*80+self.mapPos)*(self.sw/1920),i*80*((self.sw)/1920)))
                    if posNum==3:
                        self.screen.blit(self.spike, ((j*80+self.mapPos)*(self.sw/1920),i*80*((self.sw)/1920)))
                    if posNum==4:
                        self.screen.blit(self.cannon, ((j*80+self.mapPos)*(self.sw/1920),i*80*((self.sw)/1920)))
                    j+=1
                i+=1
            self.screen.blit(self.plyr, (math.floor(self.sw*(11/24)),math.floor(self.plyry*((self.sw*9/16)/1080))))

            self.screen.blit(self.ship, (self.shipx*(self.sw/1920),955*((self.sw*9/16)/1080)))
            if self.shipx<=0:
                self.screen.blit(self.shipTwo, (self.shipx*(self.sw/1920)+self.sw,955*((self.sw*9/16)/1080)))
            else:
                self.screen.blit(self.shipTwo, (self.shipx*(self.sw/1920)-self.sw,955*((self.sw*9/16)/1080)))
        #for any dimensions
        if self.shipx<=(-1920) or self.shipx>=(1920):
            self.shipx=0
        if self.cloudx<=(-1920) or self.cloudx>=(1920):
            self.cloudx20
        self.kiddo.plyrRect.move(910, self.plyry+30)
        k=0
        l=0
        m=0
        n=0
        for i in range(len(self.layout)):
            for j in range(len(eval(levelNum+".row1"))):
                posNum=eval(levelNum+(str.format(".row{}[{}]",i,j)))
                if posNum==1:
                    self.woodRect[k].move(j*80+self.mapPos,i*80)
                    k+=1
                if posNum==2:
                    self.metalRect[l].move(j*80+self.mapPos,i*80)
                    l+=1
                if posNum==3:
                    self.spikeRect[m].move(j*80+self.mapPos,i*80)
                    m+=1
                if posNum==4:
                    self.cannonRect[n].move(j*80+self.mapPos,i*80)
                    if pygame.sprite.collide_rect(self.kiddo.plyrRect,self.cannonRect[n]):
                        self.level+=1
                        self.mapPos=0
                        self.plyry=840
                        self.setLevel(str.format("self.levelOn[{}]",self.level))
                        self.move(str.format("self.levelOn[{}]",self.level))
                    n+=1
                j+=1
            i+=1
        pygame.display.update()
    def walking(self):
        if self.stuck==0:
            key=pygame.key.get_pressed()
            if key[pygame.K_d] and key[pygame.K_a]==0 and self.rolling==0:
                self.still=0
                if self.rt % self.speed == 0 and self.jumping==0:
                    self.facing=1
                    self.plyr=pygame.image.load(str.format("Images/cannonBallKid{}.png",math.floor((self.rt/self.speed)+1)))
                    self.move(str.format("self.levelOn[{}]",self.level))
                self.rt=self.rt+1
                if self.rt==16*self.speed-1:
                    self.rt=0
                self.cloudx=self.cloudx-2/self.speed
                self.shipx=self.shipx-10/self.speed
                self.mapPos=self.mapPos-10/self.speed
                if self.jumping==0:
                    time.sleep(self.quick)
            else:
                self.rt=0
                if self.jumping==0 and self.rolling==0 and self.facing==1 and self.still==0:
                    self.still=1
                    self.plyr=pygame.image.load("Images/cannonBallKidS.png")
                    self.move(str.format("self.levelOn[{}]",self.level))

            if key[pygame.K_a] and key[pygame.K_d]==0 and self.rolling==0:
                self.still=0
                if self.lt % self.speed == 0 and self.jumping==0:
                    self.facing=0
                    self.plyr=pygame.image.load(str.format("Images/cannonBallKidL{}.png",math.floor((self.lt/self.speed)+1)))
                    self.move(str.format("self.levelOn[{}]",self.level))
                self.lt=self.lt+1
                if self.lt==16*self.speed-1:
                    self.lt=0
                self.cloudx=self.cloudx+2/self.speed
                self.shipx=self.shipx+10/self.speed
                self.mapPos=self.mapPos+10/self.speed
                if self.jumping==0:
                    time.sleep(self.quick)
            else:
                self.lt=0
                if self.jumping==0 and self.rolling==0 and self.facing==0 and self.still==0:
                    self.still=1
                    self.plyr=pygame.image.load("Images/cannonBallKidLS.png")
                    self.move(str.format("self.levelOn[{}]",self.level))
def main():
    while True:
        main = Main()
        main.runGame()

main()
