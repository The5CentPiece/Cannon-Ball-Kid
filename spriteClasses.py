import pygame
class kiddo(pygame.sprite.Sprite):
    def __init__(self,y):
        pygame.sprite.Sprite.__init__(self)
        self.plyrRect = pygame.Rect(910, y+30, 100, 130)
class wood(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.woodRect = pygame.Rect(x, y, 80, 80)
class metal(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.metalRect = pygame.Rect(x, y, 80, 80)
class spike(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.spikeRect = pygame.Rect(x+20, y, 40, 80)
