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
        self.IMAGE = Surface((width,height))
        self.IMAGE.fill((255,255,255))
    def move(self,dy):
        if dy == 5:
            self.y -= 5
        if dy == -5:
            self.y += 5

class Platform_2(pygame.Rect):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = Surface((width,height))
        self.IMAGE.fill((255,255,255))
    def move(self,dy):
        if dy == 5:
            self.y -= 5
        if dy == -5:
            self.y += 5
    
ball_obj = pygame.draw.circle(window,(255,255,255),(400,400),40)
speed = 2

ball = pygame.Rect(WIDTH/2,HEIGHT/2,30,30)
print(ball.width)
print(ball.height)
  















platform_1 = Platform_1(0,400,10,140)
platform_2 = Platform_2(790,400,10,140)

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
        
    if ball.left <= 5 or ball.right >= WIDTH:
        #print(ball.left)
        ball_speed_x *= -1  
    
    if ball.colliderect(platform_1) or ball.colliderect(platform_2):
        ball_speed_x *= -1

     
    
        
    pygame.draw.ellipse(window,(255,255,255),ball)
    
   

    
    
    
    




    pygame.draw.rect(window,(255,255,255),platform_1)
    pygame.draw.rect(window,(255,255,255),platform_2)
    
    
    
    
    

    







    clock.tick(60)
    pygame.display.flip()
