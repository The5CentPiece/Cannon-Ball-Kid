import os
os.environ['SDL_VIDEO_WINDOW_POS']='%d, %d' % (0,0)
import pygame, sys, time, ctypes, math, level1
from PIL import Image
class Main():
    def __init__(self):
        self.sw=ctypes.windll.user32.GetSystemMetrics(0)
        self.sh=ctypes.windll.user32.GetSystemMetrics(1)
        self.playing=1
        self.speed=1
        self.quick=.025
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
        self.plyr=pygame.image.load("cannonBallKid.png")
        self.clouds=pygame.image.load("clouds.png")
        self.cloudsTwo=pygame.image.load("clouds.png")
        self.ship=pygame.image.load("ship.png")
        self.shipTwo=pygame.image.load("ship.png")
        self.wood=pygame.image.load("wood.png")
        self.metal=pygame.image.load("metal.png")
        self.spike=pygame.image.load("spike.png")
        self.shipx=0
        self.mapPos=0
        self.level1=level1.level1()
        self.level=1


    def runGame(self):
        pygame.init()
        self.setLevel(str.format("self.level{}",self.level))
        self.move(str.format("self.level{}",self.level))
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
                            self.plyr=pygame.image.load("cannonBallKidJumpR.png")
                        else:
                            self.plyr=pygame.image.load("cannonBallKidJumpL.png")
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
                        self.move(str.format("self.level{}",self.level))
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
                        self.move(str.format("self.level{}",self.level))
                        i=i+1
                        time.sleep(self.quick)
                    self.plyry=self.plyry-30
                    self.rolling=0
                    self.cooldown=5

                if key[pygame.K_a] and key[pygame.K_s] and key[pygame.K_d]==0 and self.rolling==0 and self.cooldown<=0:
                    self.rolling=1
                    self.facing=1
                    self.still=0
                    self.plyry=self.plyry+30
                    for i in range(16*self.speed):
                        if i % self.speed == 0 :
                            self.plyr=Image.open("cannonBallKidRollL.png")
                            self.plyr=self.plyr.rotate(22.5*(i/self.speed))
                        self.plyr=pygame.image.fromstring(self.plyr.tobytes("raw", 'RGBA'),(32,32),'RGBA')
                        self.cloudx=self.cloudx+3/self.speed
                        self.shipx=self.shipx+15/self.speed
                        self.mapPos=self.mapPos+15/self.speed
                        self.move(str.format("self.level{}",self.level))
                        i=i+1
                        time.sleep(self.quick)
                    self.plyry=self.plyry-30
                    self.rolling=0
                    self.cooldown=5
                if self.cooldown>0:
                    self.cooldown=self.cooldown-.1

                self.walking()

            for event in events:
                if event.type==pygame.QUIT:
                    sys.exit()


            pygame.display.update()

    def setLevel(self, levelNum):
        self.layout=eval(levelNum+".layout")



    def move(self, levelNum):
        self.screen.fill(self.bGColor)
        if((self.sw/1920)>(self.sh/1080)):
            #like an ultrawide
            self.clouds = pygame.transform.scale(self.clouds,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.cloudsTwo = pygame.transform.scale(self.cloudsTwo,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.ship = pygame.transform.scale(self.ship,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.shipTwo = pygame.transform.scale(self.shipTwo,(math.floor(self.sh*16/9),math.floor(self.sh/2)))
            self.plyr = pygame.transform.scale(self.plyr,(math.floor(self.sh*4/27),math.floor(self.sh*4/27)))

            self.screen.blit(self.clouds, (self.cloudx*((self.sh*16/9)/1920),0))
            if self.cloudx<=0:
                self.screen.blit(self.cloudsTwo, ((self.cloudx*((self.sh*16/9)/1920)+self.sh*(16/9)),0))
            else:
                self.screen.blit(self.cloudsTwo, ((self.cloudx*((self.sh*16/9)/1920)-self.sh*(16/9)),0))

            self.screen.blit(self.plyr, (math.floor(self.sh*(16/9)*(23/54)),math.floor(self.plyry*self.sh)))
            self.screen.blit(self.ship, (self.shipx*((self.sh*16/9)/1920),math.floor(955*self.sh)))
            if self.shipx<=0:
                self.screen.blit(self.shipTwo, ((self.shipx*((self.sh*16/9)/1920)+self.sh*(16/9)),math.floor(955*self.sh)))
            else:
                self.screen.blit(self.shipTwo, ((self.shipx*((self.sh*16/9)/1920)-self.sh*(16/9)),math.floor(955*self.sh)))

            for i in range(len(self.layout)):
                for j in range(len(eval(levelNum+".row1"))):
                    posNum=eval(levelNum+(str.format(".row{}[{}]",i+1,j)))
                    if posNum==1:
                        self.screen.blit(self.wood, (i*80*((self.sh*16/9)/1920)+(self.mapPos)*((self.sh*16/9)/1920),j*80*((self.sh*16/9)/1920)))

                    j+=1
                i+=1
        else:
            self.clouds = pygame.transform.scale(self.clouds,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.cloudsTwo = pygame.transform.scale(self.cloudsTwo,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.ship = pygame.transform.scale(self.ship,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.shipTwo = pygame.transform.scale(self.shipTwo,(math.floor(self.sw),math.floor(self.sw*9/32)))
            self.plyr = pygame.transform.scale(self.plyr,(math.floor(self.sw/12),math.floor(self.sw/12)))

            self.screen.blit(self.clouds, (self.cloudx*(self.sw/1920),0))
            if self.cloudx<=0:
                self.screen.blit(self.cloudsTwo, (self.cloudx*(self.sw/1920)+self.sw,0))
            else:
                self.screen.blit(self.cloudsTwo, (self.cloudx*(self.sw/1920)-self.sw,0))
            self.screen.blit(self.plyr, (math.floor(self.sw*(11/24)),math.floor(self.plyry*((self.sw*9/16)/1080))))

            self.screen.blit(self.ship, (self.shipx*(self.sw/1920),955*((self.sw*9/16)/1080)))
            if self.shipx<=0:
                self.screen.blit(self.shipTwo, (self.shipx*(self.sw/1920)+self.sw,955*((self.sw*9/16)/1080)))
            else:
                self.screen.blit(self.shipTwo, (self.shipx*(self.sw/1920)-self.sw,955*((self.sw*9/16)/1080)))
            for i in range(len(self.layout)):
                for j in range(len(eval(levelNum+".row1"))):
                    posNum=eval(levelNum+(str.format(".row{}[{}]",i+1,j)))
                    if posNum==1:
                        self.screen.blit(self.wood, (i*80*((self.sw)/1920)+(self.mapPos)*((self.sw)/1920),j*80*((self.sw)/1920)))

                    j+=1
                i+=1
        if self.shipx<=(-1920) or self.shipx>=(1920):
            self.shipx=0
        if self.cloudx<=(-1920) or self.cloudx>=(1920):
            self.cloudx=0
        pygame.display.update()
        print(self.mapPos)
    def walking(self):
        if self.stuck==0:
            key=pygame.key.get_pressed()
            if key[pygame.K_d] and key[pygame.K_a]==0 and self.rolling==0:
                self.still=0
                if self.rt % self.speed == 0 and self.jumping==0:
                    self.facing=1
                    self.plyr=pygame.image.load(str.format("cannonBallKid{}.png",math.floor((self.rt/self.speed)+1)))
                    self.move(str.format("self.level{}",self.level))
                self.rt=self.rt+1
                if self.rt==16*self.speed-1:
                    self.rt=0
                self.cloudx=self.cloudx-2/self.speed
                self.shipx=self.shipx-10/self.speed
                if self.jumping==0:
                    time.sleep(self.quick)
            else:
                self.rt=0
                if self.jumping==0 and self.rolling==0 and self.facing==1 and self.still==0:
                    self.still=1
                    self.plyr=pygame.image.load("cannonBallKidS.png")
                    self.move(str.format("self.level{}",self.level))

            if key[pygame.K_a] and key[pygame.K_d]==0 and self.rolling==0:
                self.still=0
                if self.lt % self.speed == 0 and self.jumping==0:
                    self.facing=0
                    self.plyr=pygame.image.load(str.format("cannonBallKidL{}.png",math.floor((self.lt/self.speed)+1)))
                    self.move(str.format("self.level{}",self.level))
                self.lt=self.lt+1
                if self.lt==16*self.speed-1:
                    self.lt=0
                self.cloudx=self.cloudx+2/self.speed
                self.shipx=self.shipx+10/self.speed
                if self.jumping==0:
                    time.sleep(self.quick)
            else:
                self.lt=0
                if self.jumping==0 and self.rolling==0 and self.facing==0 and self.still==0:
                    self.still=1
                    self.plyr=pygame.image.load("cannonBallKidLS.png")
                    self.move(str.format("self.level{}",self.level))
def main():
    while True:
        main = Main()
        main.runGame()

main()

class Kiddo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.plyrRectV = pygame.Rect(plyry+25, 938, 50, 130)
        self.plyrRectH = pygame.Rect(plyry+45, 910, 100, 70)
# class Block(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
