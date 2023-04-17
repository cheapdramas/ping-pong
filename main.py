import pygame.time
from pygame import *
from sys import exit
from random import randint
import math


init()
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((800,800))
pygame.display.set_caption('Ping Pong')
FPS = 60


clock = pygame.time.Clock()

class Platform_1(pygame.Rect):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = Surface((width,height))
        self.IMAGE.fill((255,255,255))
        self.move_up = False
        self.move_down = False
    def move(self,dy):
        if dy >= 0 and self.y >= 0:
            self.y -= 8
            self.move_up = True
        if dy <= 0 and self.bottom <= 800:
            self.move_down = True
            self.y += 8

class Platform_2(pygame.Rect):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = Surface((width,height))
        self.IMAGE.fill((255,255,255))
        self.speed = 5
    

        self.ai = 0
        self.friend = 0
    def move(self,dy):
        if dy >= 0 and self.y >= 0:
            self.y -= self.speed

        if dy <= 0 and self.bottom <= 800:
            self.y += self.speed
    

    

speed = 2

font = pygame.font.Font('Samson.ttf',50)

ball = pygame.Rect(WIDTH/2,HEIGHT/2,30,30)
print(ball.width)
print(ball.height)
platform_1 = Platform_1(0,400,10,140)
platform_2 = Platform_2(790,400,10,140)

menu_check = 1
game_check = 0
  

prev_platf_y = platform_1.y



class Menu:
    def __init__(self,game):
        self._option_surfaces = []
        self._callbacks = []
        self.current_option_index = 0
        self.game_i = game
       
    
    def to_ai(self):
        global game_check
        
        platform_2.ai = 1
        game_check = 1
        
       
    def to_friend(self):
        global game_check
        
        game_check = 1
        platform_2.friend = 1
        print(game_check)
    def append_option(self,option,callback):
        self._option_surfaces.append(font.render(option,True,(255,255,255)))
        self._callbacks.append(callback)
    def switch(self,direction):
        self.current_option_index = max(0,min(self.current_option_index + direction,len(self._option_surfaces)- 1))
    def select(self):
        self._callbacks[self.current_option_index]()
    def draw(self,surf,x,y,option_y_padding):
        for i,option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x,y + i * option_y_padding)
            if i == self.current_option_index:
                draw.rect(surf,(255,0,0),option_rect)
            surf.blit(option,option_rect)




def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0



menu = Menu(game_check)


r = randint(1,50)


random_move = True
ball_speed_x = 7
ball_speed_y = 7
score_1 = 0
score_2 = 0



if r <= 50:
    ball_speed_x = -5
    ball_speed_y = 0
if r >= 50:
    ball_speed_x = 5
    ball_speed_y = 5



menu.append_option('Play With Bot',menu.to_ai)
menu.append_option('Play with Friend',menu.to_friend)
   



while True:
    platform_1.move_up = False
    platform_1.move_down = False
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            exit()
        if menu_check == 1:
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_w:
                    menu.switch(-1)
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_s:
                    menu.switch(1)
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_SPACE:
                    menu.select()
        
    if menu_check == 1:
        window.fill((0,0,0))
        menu.draw(window,250,350,75)

        
            
    
    
    

    
   
    if game_check == 1:

        
        
        
        



        score_textfirst_p = font.render(f"{score_1}",True,(255,255,255))
        score_textsecond_p = font.render(f'{score_2}',True,(255,255,255))
        
        menu_check = 0
    
    
        window.fill((0,0,0))
        keys = pygame.key.get_pressed()
        if platform_2.friend == 1:
            if keys[K_DOWN]:
                platform_2.move(-platform_2.speed)
            if keys[K_UP]:
                platform_2.move(platform_2.speed)
        if platform_2.ai == 1:
            distance = (platform_2.y - ball.y)
            if distance >= 0 and platform_2.y >= 0:
                
                platform_2.y -= distance
            if distance <= 0 and platform_2.bottom <= 800:
                platform_2.y -= distance
            
        
        if keys[K_s]:
            platform_1.move(-5)
        if keys[K_w]:
            platform_1.move(5)

        ball.x += ball_speed_x 
        ball.y += ball_speed_y
    
        


        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1


        if ball.left <= 0:
            ball.x,ball.y = 400,400
            
            score_2 += 1

        if ball.right >= 837:
            ball.x,ball.y = 400,400
            
            score_1 += 1
        
       
        #if ball.collidepoint(thirds[0]):
        #    ball_speed_y *= -1

         

        

        if ball.colliderect(platform_1) and platform_1.move_up == True:
            ball_speed_x *= -1
            ball_speed_y = -1
        
        print(ball_speed_y)
            
            


        





        pygame.draw.ellipse(window,(255,255,255),ball)

        pygame.draw.rect(window,(255,255,255),platform_1)
        pygame.draw.rect(window,(255,255,255),platform_2)
        prev_platf_y = platform_1.y
        

        window.blit(score_textfirst_p,(20,20))
        window.blit(score_textsecond_p,(750,700))
    
    
        
    

    



        


   
    clock.tick(FPS)
    #time_elapsed = clock.tick(60) / 1000.0
    pygame.display.flip()
