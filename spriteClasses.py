import pygame
class kiddo(pygame.sprite.Sprite):
    def __init__(self,y):
        pygame.sprite.Sprite.__init__(self)
        self.plyrRect = pygame.Rect(910, y+30, 100, 130)
class block(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x, y, 80, 80))
class spike(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x+20, y, 40, 80))
class cannon(pygame.sprite.Sprite):
    def __init__(self,r,x,y):
        pygame.sprite.Sprite.__init__(self)
        r.append(pygame.Rect(x, y, 160, 160))
