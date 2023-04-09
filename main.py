import pygame.time
from pygame import *
from sys import exit
from random import randint


init()
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((800,800))
pygame.display.set_caption('Ping Pong')


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
    
ball_obj = pygame.draw.circle(window,(255,255,255),(400,400),40)
speed = 2

class Ball(pygame.Rect):
    def __init__(self,x,y,width,platform1,platform2,height):
        super().__init__(x,y,width,height)
        self.x = x
        self.y = y
        self.platform_1 = platform1
        self.platform_2 = platform2
        self.speed = 2

        self.radius = 20
    def draw(self):
        pygame.draw.circle(window,(255,255,255),(self.x,self.y),self.radius)
    
   















platform_1 = Platform_1(0,400,50,50)
platform_2 = Platform_2(750,400,50,50)
ball = Ball(400,400,50,platform_1,platform_2,50)
r = randint(1,100)
random_move = True
ball_speed_x = 7
ball_speed_y = 7

if r <= 50:
    ball_speed_x = -7
    ball_speed_y = -7
if r >= 50:
    ball_speed_x = 7
    ball_speed_y = 7

    



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
    
    ball.x += ball_speed_x 
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
        
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1  
    
    if ball.colliderect(platform_1) or ball.colliderect(platform_2):
        ball_speed_x *= -1

     
    
        
    ball.draw()
    
   

    
    
    
    




    window.blit(platform_1.IMAGE,(platform_1.x,platform_1.y))
    window.blit(platform_2.IMAGE,(platform_2.x,platform_2.y))
    
    
    
    
    

    







    clock.tick(60)
    pygame.display.flip()
