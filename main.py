import pygame.time
from pygame import *
from sys import exit
from random import randint
import math
import time
import json
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
        self.move_down = False
        self.move_up = False
    def move(self,dy):
        if dy >= 0 and self.y >= 0:
            self.y -= self.speed
            self.move_up = True

        if dy <= 0 and self.bottom <= 800:
            self.y += self.speed
            self.move_down = True
    



speed = 2

font = pygame.font.Font('Samson.ttf',50)

ball = pygame.Rect(WIDTH/2,HEIGHT/2,30,30)
print(ball.width)
print(ball.height)
platform_1 = Platform_1(0,400,10,140)
platform_2 = Platform_2(790,400,10,140)

menu_check = 1
game_check = 0
  

start_time = time.time()

prev_platf_y = platform_1.y



class Menu:
    def __init__(self,game):
        self._option_surfaces = []
        self._callbacks = []
        self.current_option_index = 0
        self.game_i = game
        self.continuee = 0

    def to_continue(self):
        global esc
        global game_check
        print(esc)
        esc = 0
        game_check = 1      
       
    
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


esc = 0

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0



menu = Menu(game_check)


r = randint(1,100)


random_move = True
ball_speed_x = 7 
ball_speed_y = 7





if r <= 50:
    ball_speed_x = -7
    ball_speed_y = 0
if r >= 50:
    ball_speed_x = 7
    ball_speed_y = 0

ball_increase = 0











   
game_history = 0




def restart():
    global esc,game_check,ball

    


    esc = 0
    
    game_check = 1
    ball.x , ball.y = 400,400
def game_plus():
    global game_history
    game_history += 1

data_score = {'score1': 0, 'score2' : 0}

#with open('scores_data.txt') as f:
#    data_score = json.load(f)
num = 0 

some_list = [

]



while True:
    with open('num.txt','r') as f:
        num = json.load(f)
    
    
    platform_2.move_down = False
    platform_2.move_up = False
    platform_1.move_up = False
    platform_1.move_down = False
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            num += 1
            with open("num.txt",'w') as f:
                f.write(str(num))
            
            with open('scores_data.txt','a')as f:
                f.write(str(data_score))

            
            

            

            
            

        
            exit()
        if game_check == 1:
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_ESCAPE:
                    esc = 1
        if esc == 1 or game_history == 1 or menu_check == 1:
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
        menu._callbacks.clear()
        menu._option_surfaces.clear()
        menu.append_option('Play With Bot',menu.to_ai)
        menu.append_option('Play with Friend',menu.to_friend)   
        
        window.fill((0,0,0))
        menu.draw(window,250,350,75)
    if esc == 1:
        menu._callbacks.clear()
        menu._option_surfaces.clear()
        
        game_check = 0
        text = font.render('Pause',True,(255,255,255))
        menu.append_option('Continue',menu.to_continue)
        menu.append_option('Restart',restart)
        menu.append_option('Game History',game_plus)
        print(game_history)
        menu.append_option('Exit',exit)
        
        #menu.append_option('Continue',lambda: print('sad'))
        window.fill((0,0,0))
        menu.draw(window,250,350,75)
        window.blit(text,(350,10))

        


        

    if game_history == 1:
        menu._option_surfaces.clear()
        menu._callbacks.clear()
        game_check = 0
        esc = 0
        window.fill((0,0,0))
        
        
        
        with open('scores_data.txt','r') as f:
            print(json.loads()))  
             
            #menu.append_option(str('score_1:  '+ f'{text["score1"]}       '       +     'score_2:    ' +      f"{text['score2']}"),lambda:print('asd'))
        #    menu.append_option(str(text),lambda:print('asd'))
        text_my = font.render('Game History',True,(255,255,255))
        #menu.append_option(f'{game_data}',lambda: print('asd'))           
        menu.draw(window,250,250,75)
        window.blit(text_my,(270,20))
    
        

    
   
    if game_check == 1:

        
        
        
        



        score_textfirst_p = font.render(f'{data_score["score1"]}',True,(255,255,255))
        score_textsecond_p = font.render(f'{data_score["score2"]}',True,(255,255,255))
        
        menu_check = 0
    
    
        window.fill((0,0,0))
        keys = pygame.key.get_pressed()
        if platform_2.friend == 1:
            if keys[K_DOWN]:
                platform_2.move(-platform_2.speed)
            if keys[K_UP]:
                platform_2.move(platform_2.speed)
            if ball.colliderect(platform_2) and platform_2.move_up == True:
                ball_speed_y = -1

                ball_speed_x *= -1
            if ball.colliderect(platform_2) and platform_2.move_down == True:
                ball_speed_y = 1
                ball_speed_x *= -1
            if ball.colliderect(platform_2) and platform_2.move_down == False and platform_2.move_up == False:
                ball_speed_x *= -1
            
            
        if platform_2.ai == 1:
            distance = (platform_2.y - ball.y)
            if distance >= 0 and platform_2.y >= 0:
                
                platform_2.y -= distance
            if distance <= 0 and platform_2.bottom <= 800:
                platform_2.y -= distance / 1
            
            if ball.colliderect(platform_2):
                ball_speed_x *= -1  
            
        
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
            ball_speed_x = 7 
            data_score['score2'] += 1
            
            

        if ball.right >= 837:
            ball_speed_x = -7
            ball.x,ball.y = 400,400
            
            data_score['score1'] += 1
        
       
        #if ball.collidepoint(thirds[0]):
        #    ball_speed_y *= -1

         

        

        if ball.colliderect(platform_1) and platform_1.move_up == True:
            ball_speed_x = ball_speed_x - 1
            ball_speed_y = ball_speed_y - 1 
            ball_speed_x *= -1
            ball_speed_y = -1
        if ball.colliderect(platform_1) and platform_1.move_down == True:
            ball_speed_x = ball_speed_x - 1 
            
            ball_speed_x *= -1
            ball_speed_y = 1
        if ball.colliderect(platform_1) and platform_1.move_down == False and platform_1.move_up == False:
            ball_speed_x *= -1
        
        
        
        print(ball_speed_x)
        
       
            
            


        





        pygame.draw.ellipse(window,(255,255,255),ball)

        pygame.draw.rect(window,(255,255,255),platform_1)
        pygame.draw.rect(window,(255,255,255),platform_2)
        prev_platf_y = platform_1.y
        

        window.blit(score_textfirst_p,(20,20))
        window.blit(score_textsecond_p,(750,700))
    
    
        
    

    



        


    
    
    
    clock.tick(FPS)
    
    pygame.display.flip()
