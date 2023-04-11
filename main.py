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
        if dy == 5 and self.y >= 0:
            self.y -= 5
        if dy == -5 and self.bottom <= 800:
            self.y += 5

class Platform_2(pygame.Rect):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = Surface((width,height))
        self.IMAGE.fill((255,255,255))

        self.ai = 0
        self.friend = 0
    def move(self,dy):
        if dy == 5 and self.y >= 0:
            self.y -= 5
        if dy == -5 and self.bottom <= 800:
            self.y += 5
    def move_ai(self,ball):
        None

    
ball_obj = pygame.draw.circle(window,(255,255,255),(400,400),40)
speed = 2

font = pygame.font.Font('Samson.ttf',50)

ball = pygame.Rect(WIDTH/2,HEIGHT/2,30,30)
print(ball.width)
print(ball.height)
platform_1 = Platform_1(0,400,10,140)
platform_2 = Platform_2(790,400,10,140)


  

menu_i = 1
game_check = 1


class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self.current_option_index = 0
    
    def to_ai(self):
        
        game_check = 1
        menu_i = 0
        
        
       
    def to_friend(self):
        game_check = 1
        menu_i = 0
        print(game_check)
        platform_2.friend = 1
        
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









menu_i = 1
game_check = 1

menu = Menu()


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



menu.append_option('Play With Bot',menu.to_ai)
menu.append_option('Play with Friend',menu.to_friend)
   



while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            exit()
        if menu_i == 1:
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_w:
                    menu.switch(-1)
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_s:
                    menu.switch(1)
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_SPACE:
                    menu.select()
            

        
            
    
    if menu_i == 1:
        game_check = 0
        window.fill((0,0,0))
        
       
        
        menu.draw(window,250,350,75)

    
   
    if game_check == 1:
        menu_i = 0
        print('хуй')
    
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
