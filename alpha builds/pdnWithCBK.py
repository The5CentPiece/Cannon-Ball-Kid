import pygame, sys, time
# from win32api import GetSystemMetrics
class Main():
    def __init__(self):
        # self.screen=pygame.display.set_mode(GetSystemMetrics(0),GetSystemMetrics(1))
        self.sx=1920
        self.sy=1080
        self.screen=pygame.display.set_mode((self.sx,self.sy),pygame.FULLSCREEN)
        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert
        self.screen_color=(0,0,0)
        self.plyrx=200
        self.plyry=200
        self.clock=pygame.time.Clock()
        self.plyr=pygame.image.load("cannonBallKid.png")
        self.plyr = pygame.transform.scale(self.plyr,(200,200))
        self.screen.blit(self.plyr, (self.plyrx,self.plyry))

    def runGame(self):
        pygame.init()
        self.clock.tick(1000/60)
        while True:
            events=pygame.event.get()
            key=pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.plyrx=self.plyrx+1
                self.screen.blit(self.plyr, (self.plyrx,self.plyry))
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
