import pygame, sys, time
# from win32api import GetSystemMetrics
class Main():
    def __init__(self):
        # self.screen=pygame.display.set_mode(,)
        #self.sw=2160
        #self.sh=1440
        #variable for if the game is running
        self.playing=1;
        self.screen=pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert
        self.screen_color=(0,0,0)
        self.screen.fill([221,253,255])
        self.plyry=640
        self.clock=pygame.time.Clock()
        self.plyr=pygame.image.load("cannonBallKid.png")
        self.plyr = pygame.transform.scale(self.plyr,(160,160))
        self.clouds=pygame.image.load("clouds.png")
        self.clouds = pygame.transform.scale(self.clouds,(1920,1080))
        self.screen.blit(self.plyr, (880,(self.plyry)))
        self.screen.blit(self.clouds, (0,0))
        # if((self.sw/1920)>(self.sh/1080)):
        #     self.screen.blit(self.plyr, (880+((((self.sw/self.sh)*(9/16)*1920)-1920)/2),(self.plyry)))
        #     self.screen.blit(self.clouds, (0+((((self.sw/self.sh)*(9/16)*1920)-1920)/2),0))
        # else:
        #     self.screen.blit(self.plyr, (880,(self.plyry+((((self.sh/self.sw)*(16/9)*1080)-1080)/2))))
        #     self.screen.blit(self.clouds, (0,0+((((self.sh/self.sw)*(16/9)*1080)-1080)/2)))
    def runGame(self):
        pygame.init()
        self.clock.tick(1000/60)
        while True:
            #movement
            events=pygame.event.get()
            key=pygame.key.get_pressed()
            if self.playing==1:
                if key[pygame.K_d]:
                    pygame.display.update()

            for event in events:
                if event.type==pygame.QUIT:
                    sys.exit()


            pygame.display.update()


def main():
    while True:
        main = Main()
        main.runGame()

main()
