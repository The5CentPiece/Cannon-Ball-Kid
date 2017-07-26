import os
os.environ['SDL_VIDEO_WINDOW_POS']='%d, %d' % (0,0)
import pygame, sys, time, ctypes, math
class Main():
    def __init__(self):
        self.sw=ctypes.windll.user32.GetSystemMetrics(0)
        self.sh=ctypes.windll.user32.GetSystemMetrics(1)
        self.playing=1
        self.speed=1
        self.quick=.025
        self.rolling=0
        self.facing=1
        self.jumping=0
        self.still=1
        self.rt=0
        self.lt=0
        self.screen=pygame.display.set_mode((self.sw,self.sh),pygame.NOFRAME)
        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert
        self.screen_color=(0,0,0)
        self.plyry=840
        self.cloudx=0
        self.clock=pygame.time.Clock()
        self.plyr=pygame.image.load("cannonBallKid.png")
        self.clouds=pygame.image.load("clouds.png")
        self.cloudsTwo=pygame.image.load("clouds.png")
        self.ship=pygame.image.load("ship.png")
        self.shipTwo=pygame.image.load("ship.png")
        self.shipx=0
        self.move()



    def runGame(self):
        pygame.init()
        while True:
            self.clock.tick(60)
            #movement
            events=pygame.event.get()
            key=pygame.key.get_pressed()
            if self.playing==1:
                if key[pygame.K_d] and key[pygame.K_a]==0 and self.rolling==0:
                    self.still=0
                    if self.rt % self.speed == 0 :
                        self.facing=1
                        self.plyr=pygame.image.load(str.format("cannonBallKid{}.png",math.floor((self.rt/self.speed)+1)))
                    self.rt=self.rt+1
                    if self.rt==16*self.speed-1:
                        self.rt=0
                    self.cloudx=self.cloudx-2/self.speed
                    self.shipx=self.shipx-10/self.speed
                    self.move()
                    time.sleep(self.quick)
                else:
                    self.rt=0
                    if self.jumping==0 and self.rolling==0 and self.facing==1 and self.still==0:
                        self.still=1
                        self.plyr=pygame.image.load("cannonBallKidS.png")
                        self.move()

                if key[pygame.K_a] and key[pygame.K_d]==0 and self.rolling==0:
                    self.still=0
                    if self.lt % self.speed == 0 :
                        self.facing=0
                        self.plyr=pygame.image.load(str.format("cannonBallKidL{}.png",math.floor((self.lt/self.speed)+1)))
                    self.lt=self.lt+1
                    if self.lt==16*self.speed-1:
                        self.lt=0
                    self.cloudx=self.cloudx+2/self.speed
                    self.shipx=self.shipx+10/self.speed
                    self.move()
                    time.sleep(self.quick)
                else:
                    self.lt=0
                    if self.jumping==0 and self.rolling==0 and self.facing==0 and self.still==0:
                        self.still=1
                        self.plyr=pygame.image.load("cannonBallKidLS.png")
                        self.move()
                # while key[pygame.K_d]==:
                    # if self.rt % self.speed == 0 :
                    #     self.facing=1
                    #     self.plyr=pygame.image.load(str.format("cannonBallKid{}.png",math.floor((self.rt/self.speed)+1)))
                    #     self.move()
                    # self.rt=self.rt+1
                    # if self.rt==16*self.speed-1:
                    #     self.rt=0
                    # time.sleep(.025)
                # if key[pygame.K_a] and self.rolling==0:
                #     #print(0)
                #     self.facing=0
                #     for i in range(16*self.speed):
                #         if i % self.speed == 0 :
                #             self.plyr=pygame.image.load(str.format("cannonBallKidL{}.png",math.floor((i/self.speed)+1)))
                #             self.move()
                #         if i==self.speed-1 :
                #             i=0
                #         time.sleep(.025)
            for event in events:
                if event.type==pygame.QUIT:
                    sys.exit()


            pygame.display.update()

    def move(self):
        self.screen.fill([221,253,255])
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

            self.screen.blit(self.plyr, (math.floor(self.sh*(16/9)*(15/32)),math.floor(self.plyry*self.sh)))
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

            self.screen.blit(self.clouds, (self.cloudx*(self.sw/1920),0))
            if self.cloudx<=0:
                self.screen.blit(self.cloudsTwo, (self.cloudx*(self.sw/1920)+self.sw,0))
            else:
                self.screen.blit(self.cloudsTwo, (self.cloudx*(self.sw/1920)-self.sw,0))
            self.screen.blit(self.plyr, (math.floor(self.sw*(15/32)),math.floor(self.plyry*((self.sw*9/16)/1080))))

            self.screen.blit(self.ship, (self.shipx*(self.sw/1920),955*((self.sw*9/16)/1080)))
            if self.shipx<=0:
                self.screen.blit(self.shipTwo, (self.shipx*(self.sw/1920)+self.sw,955*((self.sw*9/16)/1080)))
            else:
                self.screen.blit(self.shipTwo, (self.shipx*(self.sw/1920)-self.sw,955*((self.sw*9/16)/1080)))
        if self.shipx==(-1920) or self.shipx==(1920):
            self.shipx=0
        if self.cloudx==(-1920) or self.cloudx==(1920):
            self.cloudx=0
        pygame.display.update()

def main():
    while True:
        main = Main()
        main.runGame()

main()
