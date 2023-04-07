import pygame.time
from pygame import *
from sys import exit

init()

window = pygame.display.set_mode((800,800))

clock = pygame.time.Clock()

class Platform_1(pygame.Rect):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = Surface((50,200))
        self.IMAGE.fill((255,255,255))
    def move(self,dy):
        if dy == 5:
            self.y -= 5
        if dy == -5:
            self.y += 5

class Platform_2(pygame.Rect):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = Surface((50,200))
        self.IMAGE.fill((255,255,255))
    def move(self,dy):
        if dy == 5:
            self.y -= 5
        if dy == -5:
            self.y += 5







platform_1 = Platform_1(0,400,50,50)
platform_2 = Platform_2(750,400,50,50)


while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            exit()
    window.fill((0,0,0))
    keys = pygame.key.get_pressed()
    if keys[K_s]:
        platform_1.move(-5)
    if keys[K_w]:
        platform_1.move(5)

    
    
    
    




    window.blit(platform_1.IMAGE,(platform_1.x,platform_1.y))
    window.blit(platform_2.IMAGE,(platform_2.x,platform_2.y))
    
    

    







    clock.tick(60)
    pygame.display.flip()
