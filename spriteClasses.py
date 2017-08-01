import pygame
class Kiddo(pygame.sprite.Sprite):
    def __init__(self,y):
        pygame.sprite.Sprite.__init__(self)
        self.plyrRect = pygame.Rect(910, y+30, 100, 130)
class Blocks(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.woodRect=[]
        self.metalRect=[]
        self.spikeRect=[]
        self.cannonRect=[]
class Wood(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x, y, 80, 80))
class Metal(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x, y, 80, 80))
class Spike(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x+20, y, 40, 80))
class Cannon(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x, y, 160, 160))
