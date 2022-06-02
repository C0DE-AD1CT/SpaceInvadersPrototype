
import pygame as pg
import keyboard as k
from time import sleep
from random import *
import random as r
import os 
from launcher import *

from pygame.constants import K_LEFT, K_RIGHT ,K_DOWN, K_UP



class values():
    window_xy = (800 ,600)
    defaultxy=(window_xy[0]/2,window_xy[1]/2)
    gamewin = ((100,100),(250,50),(400,200),(600,100),(700,300),
                (200,250),(400,400),(100,100),(600,400),(100,500))
class game_tools():    
    def Boundry(x,y):
        if x<=0 :
            x+=6
        elif x>=715:
            x-=6
        if y<=0 :
            y+=6
        elif y>=499:
            y-=6
        return x,y
    def draw_rectangle(surface,x,y,x2,y2,color):
        pg.draw.rect(surface,color,pg.Rect(x,y,x2,y2))
    def game_window(window):
        game_tools.draw_rectangle(window,0,0,800,600,(0,0,0))
        for z in values.gamewin:
            x=z[0]
            y=z[1]
            game_tools.displayIMAGE(window,"star.png",x,y,0)
    def displayIMAGE(window,IMAGE,x,y,angle):
        image=pg.image.load(IMAGE)
       # print("[x:\t"+str(x)+",\t\ty:\t"+str(y)+",\tangle:\t\t"+str(angle)+"\t]")
        image=pg.transform.rotate(image,angle)
        window.blit(image,(x,y))
    def game_end_check(player_coords,enemy__coords):
        #enemys = enemy()
        enemy_prev_coords = enemy__coords#enemys.prev_coords
        #print(enemy_prev_coords,player_coords)
        enemy_y = enemy_prev_coords[1]
        enemy_x = enemy_prev_coords[0]
        player_y = player_coords[1]
        player_x = player_coords[0]
        # print(enemy_y,player_y)
        counter=0

        for i in range(len(enemy_y)-1):
           # print(i)
            #end_F = open ("endcond.txt","w")
            game=True
            y_enemy = enemy_y[i]
            x_enemy = enemy_x[i]
            
            if y_enemy +50  >= player_y  and x_enemy-50<=player_x<=x_enemy+50:
               print("enemy x :"+str(x_enemy)+" enemy y :"+str(y_enemy)+" player y :"+str(player_y)+str(i)+" player x :"+str(player_x)+" "+str(i))
              # print("enemy y :"+str(y_enemy)+" player y :"+str(player_y)+str(i))
               game=False
               break
               
            elif y_enemy ==499 :
               game=True
               quit()
        return game
              # end_F.close()
           
               # end_F.close()
""" 
            if y_enemy >= player_y and x_enemy == player_x :#and x_enemy== player_x :
                print(y_enemy,player_y)
                return False
            else:
                return True
            """

class laser (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_y_1 = -6.5
        self.pos_y_2 =  6.5
        #self.pos_y = 0 
        self.image = pg.image.load("laser.png")
        self.rect = self.image.get_rect()
    def update(self,entity_xy,x):
        if x == 100:
            self.rect.y = entity_xy[1] 
            self.rect.x = entity_xy[0] + 45
        self.rect.y+=self.pos_y_1 
class player1 (pg.sprite.Sprite):
    def __init__(self):

        super().__init__()
        
        self.image = pg.image.load("ASSET1.PNG")
       # pg.draw.rect(self.image,(255,255,255), [0, 0, 50, 50])
        self.rect = self.image.get_rect() 
    def start_player(self):
        self.rect.x = 500
        
        self.rect.y = 500
    def player_move(self,laserI):
        keys=pg.key.get_pressed()
        self.movex = 0
        self.movey = 0
        if keys[pg.K_UP]:
            self.movey = -5
        if keys[pg.K_DOWN]:
            self.movey = 5
        if keys[pg.K_LEFT]:
            self.movex = -5
        if keys[pg.K_RIGHT]:
            self.movex = 5
        if keys[pg.K_SPACE] and laserI<=0:
            laserI= 100
        #print("x :"+str(self.rect.x)+" y:"+str(self.rect.y))
        return laserI
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey
        print(self.rect.x,self.rect.y)

        return self.rect.x , self.rect.y
        #image=pg.image.load("ASSET1.PNG")
        #self.image = screen.blit(image,(self.rect.x,self.rect.y))
    def boundry(self):
        if self.rect.x < -10:
            self.rect.x += 6
        if self.rect.x > 715:
            self.rect.x -= 6 
        if self.rect.y < -10:
            self.rect.y += 6
        if self.rect.y > 523:
            self.rect.y -= 6 
class enemy():
    def wave1_coords():
        xy=[]
        x1=[]
        y1=[]
        for i in range (0,10):
            x=round(725*i*0.10-10)
            x1.append(x)
        for i in range(0,1):
            for i in range (0,5):
                y=round(-533*i*0.10-10)
                y1.append(y)
            for i in range (5,0,-1):
                y=round(-533*i*0.10-10)
                y1.append(y)
        xy.append(x1)
        xy.append(y1)
        return xy
    def __init__(self) :
        super().__init__()
        self.prev_coords = []
        self.wave1_xy = enemy.wave1_coords ()       
        #print(temp)  
    def spawn_enemy(self,incr,window):
        x_coords = self.wave1_xy [0]
        y_coords = self.wave1_xy [1]
       # print(x_coords,y_coords,incr)
        for y in y_coords:
            index_i = y_coords.index(y)
            y_coords.pop(index_i)
            y_coords.insert(index_i,(y+incr))
        x_coords_len = len(x_coords)
       # print(x_coords,y_coords,incr,x_coords_len)
        try:
            for i in range(0,x_coords_len+1):
            #print(i)
                x=x_coords[i]
                y=y_coords[i]
                image1 ="ENEMY\enemy1.png"
                game_tools.displayIMAGE(window,image1,x,y,0)
               # print(x,y)
        except : IndexError
        self.prev_coords = [x_coords,y_coords]
        incr +=1
        #print(x_coords,y_coords,incr)
        return incr , [x_coords,y_coords]
      
        
def main():
    laserI=0
    enemy_incr = -1
   
    #enemy_spawn = False
    player_xy=[]
    x=values.window_xy[0]
    y=values.window_xy[1]
    pg.init()
    screen=pg.display.set_mode((x,y))
    player_group = pg.sprite.Group()
    player = player1()
    player.start_player()
    laser1 = laser()
    player_group.add(player)
    player_group.draw(screen)
    game=True
    
    while game==True:#game=="0":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        laserI=player.player_move(laserI)
        player_xy=player.update()
        player.boundry()
        
        pg.display.flip()
        if laserI == 100 :
            player_group.add(laser1)
        if laserI > 0 :
            laser1.update(player_xy,laserI)
            laserI -=1.5
        else: 
            player_group.remove(laser1)
        
        pg.time.wait(10)
        game_tools.game_window(screen)
        player_group.draw(screen)
        #draw enemys
        enemys=enemy()
        enemy_spawn = enemys.spawn_enemy(enemy_incr,screen)
        enemy_incr = enemy_spawn [0]
        enemy_xy = enemy_spawn [1]
        #
        game=game_tools.game_end_check(player_xy,enemy_xy)
    pg.quit()  
        # get the results of game end check
       
        #print(game)
   
    
main()
a= []
#a.insert()
##a.pop()#

