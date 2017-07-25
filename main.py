import os
os.environ['SDL_VIDEO_WINDOW_POS']='%d, %d' % (0,0)
import pygame, sys, time, ctypes, math
class Main():
    def __init__(self):
        self.sw=ctypes.windll.user32.GetSystemMetrics(0)
        self.sh=ctypes.windll.user32.GetSystemMetrics(1)
        self.playing=1
        self.speed=32000
        self.screen=pygame.display.set_mode((self.sw,self.sh),pygame.NOFRAME)
        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert
        self.screen_color=(0,0,0)
        self.plyry=840
        self.clock=pygame.time.Clock()
        self.plyr=pygame.image.load("cannonBallKid.png")
        self.clouds=pygame.image.load("clouds.png")
        self.move()



    def runGame(self):
        pygame.init()
        self.clock.tick(1000/60)
        while True:
            #movement
            events=pygame.event.get()
            key=pygame.key.get_pressed()
            if self.playing==1:
                if key[pygame.K_d] :
                    for i in range(16*self.speed):
                        if i % self.speed == 0 :
                            self.plyr=pygame.image.load(str.format("cannonBallKid{}.png",math.floor((i/self.speed)+1)))
                            self.move()
                            pygame.display.update()
                        if i==self.speed-1 :
                            i=0
                if key[pygame.K_a] :
                    for i in range(16*self.speed):
                        if i % self.speed == 0 :
                            self.plyr=pygame.image.load(str.format("cannonBallKidL{}.png",math.floor((i/self.speed)+1)))
                            self.move()
                            pygame.display.update()
                        if i==self.speed-1 :
                            i=0

            for event in events:
                if event.type==pygame.QUIT:
                    sys.exit()


            pygame.display.update()

    def move(self):
        self.screen.fill([221,253,255])
        if((self.sw/1920)>(self.sh/1080)):
            #like an ultrawide
            self.clouds = pygame.transform.scale(self.clouds,(math.floor(self.sh*16/9),math.floor(self.sh)))
            self.plyr = pygame.transform.scale(self.plyr,(math.floor(self.sh*4/27),math.floor(self.sh*4/27)))
            self.screen.blit(self.plyr, (math.floor(self.sh*(16/9)*(15/32)),math.floor(self.plyry*self.sh)))
        else:
            self.clouds = pygame.transform.scale(self.clouds,(math.floor(self.sw),math.floor(self.sw*9/16)))
            self.plyr = pygame.transform.scale(self.plyr,(math.floor(self.sw/12),math.floor(self.sw/12)))
            self.screen.blit(self.plyr, (math.floor(self.sw*(15/32)),math.floor(self.plyry*((self.sw*9/16)/1080))))
        self.screen.blit(self.clouds, (0,0))

def main():
    while True:
        main = Main()
        main.runGame()

main()
