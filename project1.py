#Project1

import pygame
import random

random_place = []

pygame.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("popba")
clock = pygame.time.Clock()
by1 = pygame.image.load("byc.png")
by_dead = pygame.image.load("by_dead.png")
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255, 0)
kills = 0
deads = 0
font = pygame.font.SysFont("Monospaced", 35, True)
font2 = pygame.font.SysFont("vardana", 50, True)

class Player:
    character = pygame.image.load("idle_right\idle1.png")
    character2 = pygame.image.load("idle_left\idle1.png")

    def __init__(self, x,y,speed,speed_jump,width,height):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height
        self.right = False
        self.left = False
        self.is_jumping = False
        self.shift = False
        self.is_shot = False
        self.speed = speed
        self.c = [0]
        self.speed_jump = speed_jump
        self.idle_move = 0
        self.shift_move = 0
        self.back_x = x - 500
        self.back_y = y - 450
        self.health = 10
        self.direction = 0
        if self.shift == True:
            self.hitbox = self.hitbox = (self.x + 50 , self.y + 85 , self.width - 80 , self.height - 100)

        else:
            self.hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
            
    def draw(self, screen):
        global move
        
        

        if self.left == True and self.is_jumping == False:
            screen.blit(run_left[move%len(run_right)//2], (self.x,self.y))
            move += 1

                    
        elif self.right and self.is_jumping == False :
            screen.blit(run_right[move%len(run_right)//2], (self.x,self.y))
            move += 1

        
        elif self.left == True and self.is_jumping == True and self.is_shot == False:
            pygame.time.delay(0)
            screen.blit(jump_left[move%len(jump_left)//2] , (self.x,self.y))
            move += 1


        elif self.right == True and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_right[move%len(jump_right)//2], (self.x,self.y))
            move += 1


        elif self.c == [0] and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_right[move%len(jump_right)//2] , (self.x,self.y))
            move += 1


        elif self.c == [1] and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_left[move%len(jump_left)//2] , (self.x,self.y))
            move += 1
            if move == len(idle_right):
                move = 0

        elif self.is_shot == True and self.c == [0] and self.right ==False and self.left == False and self.is_jumping == False:
            screen.blit(shot_right[self.shift_move], (self.x,self.y))
            self.shift_move += 1  
            if self.shift_move == 4:
                self.shift_move = 0 
        elif self.is_shot == True and self.c == [1] and self.right ==False and self.left == False and self.is_jumping == False:
            screen.blit(shot_left[self.shift_move], (self.x,self.y))
            self.shift_move += 1  
            if self.shift_move == 4:
                self.shift_move = 0      

        elif self.c == [0] and self.shift == True and self.right == False and self.left == False and self.is_jumping == False:
            if self.is_jumping == True:
                self.shift = False
            
            screen.blit(shift_move[0], (self.x,self.y))    
        elif self.c == [1] and p1.shift == True and self.right == False and self.left == False and self.is_jumping == False:
            screen.blit(shift_move[1], (self.x,self.y))
            if self.is_jumping == True:
                self.shift = False        




        elif self.c == [0] and self.right == False and self.left == False and self.is_jumping == False and p1.is_shot == False:
            screen.blit(idle_right[self.idle_move], (self.x,self.y))
            self.idle_move += 1
            if self.idle_move >= 6:
                self.idle_move = 0


        elif self.c == [1] and self.right == False and self.left == False and self.is_jumping == False and p1.is_shot == False:
            screen.blit(idle_lift[self.idle_move], (self.x,self.y))
            self.idle_move += 1
            if self.idle_move >= 6:
                self.idle_move = 0

        if self.shift == True:
            self.hitbox = self.hitbox = (self.x + 40 , self.y + 85 , self.width - 80 , self.height - 100)
        else:
            self.hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
        pygame.draw.rect(screen, RED,self.hitbox, 2)
        pygame.draw.rect(screen, RED, (750 , 20, 100, 50))
        pygame.draw.rect(screen, GREEN, (750, 20 , self.health * 10, 50))
    def move(self):
        global keys
        keys = pygame.key.get_pressed()
    

        if (keys[pygame.K_RIGHT ] or keys[pygame.K_d]) and self.x < screen_width - 90 and self.shift == False:
            self.x += self.speed
            self.back_x -= self.speed -4
            self.right = True
            self.left = False
            self.c = [0]
        elif (keys[pygame.K_LEFT ] or keys[pygame.K_a]) and self.x > 0 - 40 and self.shift == False:
            self.x -= self.speed
            self.back_x += self.speed -4
            self.right = False 
            self.left = True 
            self.c = [1]
        elif keys[pygame.K_LSHIFT] and self.is_jumping == False:
            self.shift = True
            self.right = False
            self.left = False
            self.is_jumping = False
            self.is_shot = False
        elif keys[pygame.K_l] and self.y > 400 and self.y < screen_height - 120 and self.is_jumping == False:
            self.is_shot = True
            self.right =False  
            self.left = False  
            self.is_jumping = False
            self.idle_move = False

            if len(bullets) < 9:
                self.direction = 0
                if self.c == [0]:
                    self.direction = 1
                else:
                    self.direction = -1
                bullets.append(Bullet(round(self.x + self.width // 2), round(self.y + self.height // 2 + 23), 50 ,self.direction ))       
                        
            
        
        else:
            self.right = False
            self.left = False
            self.shift = False
            self.is_shot = False
            
            
        
                                
        if not self.is_jumping:
            if (keys[pygame.K_UP ] or keys[pygame.K_w]) and self.y > 420 :
                self.y -= self.speed - 3
                if self.c == [0]:
                    self.right =True 
                    self.left = False
                elif self.c == [1]:
                    self.right = False 
                    self.left = True   
            elif (keys[pygame.K_DOWN ] or keys[pygame.K_s]) and self.y < screen_height - 130:
                self.y += self.speed - 3
                if self.c == [0]:
                    self.right =True 
                    self.left = False
                elif self.c == [1]:
                    self.right = False 
                    self.left = True   
            elif keys[pygame.K_SPACE]:
                self.is_jumping = True
                self.is_shot = False

        
                    
        
        elif self.is_jumping and self.y > 350 and self.shift == False and self.is_shot == False:
            self.shift = False
            self.is_shot = False
            
            if self.speed_jump >= -8:
                p = 1
                self.shift = False
                if self.speed_jump <= 0 and self.y < screen_height - 130:
                    self.is_shot = False
                    self.is_jumping = True
                    p = -1
                self.y -= (self.speed_jump ** 2) * 0.25 * p
                self.speed_jump -= 1
            else:
                self.is_jumping = False
                self.speed_jump = 8 
        elif self.is_jumping == True and self.shift == True:
            self.is_jumping = False
            self.shift = False         
            
            
        else:
            self.right = False
            self.left = False
            self.is_jumping = False
            self.shift = False   
            self.is_shot = False         
    def hit(self):
       
        text2 = font2.render("You Dead ", 1,RED)
        screen.blit(text2, (450, 250))
        text3 = font2.render("Try Agin ", 1,RED)
        screen.blit(text3, (450, 350))
        time = 1
        while time < 500:
            pygame.display.update()
            time += 1
            pygame.time.delay(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
class Bullet:
    def __init__(self, x,y ,speed, direction) :
        self.x =x
        self.y = y
        self.speed = speed * direction
        self.direction = direction  
                       

class Enemy:
    def __init__(self,x,y,width,height,speed,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.end = end
        self.start = self.x
        self.right = False
        self.left = False
        self.health = 10
        self.visable = True
        self.move1 = 0
        self.attack1 = 0
        self.attack2 = 0
        self.hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
        self.attack = False
        self.o = 1
    def draw(self, screen):
        if self.visable:
        
            if self.attack and self.right:
                screen.blit(enemy_attack_right[self.attack1],(self.x,self.y)) 
                self.attack1 += 1
                if self.attack1 >= 7:
                    self.attack1 = 0    
            elif self.attack and self.left:
                screen.blit(enemy_attack_left[self.attack2],(self.x,self.y)) 
                self.attack2 += 1
                if self.attack2 >= 7:
                    self.attack2 = 0            
            if self.right and self.attack == False:
                screen.blit(enemy_run_right[self.move1//2], (self.x,self.y))
                self.move1 += 1
                if self.move1 > 9*2:
                    self.move1 = 1
            elif self.left and self.attack == False:
                screen.blit(enemy_run_left[self.move1//2], (self.x,self.y))
                self.move1 += 1
                if self.move1 > 9*2:
                    self.move1 = 1        
            

            self.hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
            pygame.draw.rect(screen, RED,self.hitbox, 2)        
            pygame.draw.rect(screen, RED, (self.hitbox[0], self.hitbox[1] - 30, 50, 5))
            pygame.draw.rect(screen, GREEN, (self.hitbox[0] , self.hitbox[1] - 30, self.health * 5, 5))
    def move(self):
        
        
        if self.x < p1.x :
            if self.x > p1.x -30:
                
                if self.o > 30:
                    self.attack = True
                    p1.health -= 1
                    if self.o > 30:
                        self.o = 1
            else:    
                self.x += self.speed
                self.left = False
                self.right = True
                self.attack = False
        
        elif self.x > p1.x :
            if self.x < p1.x +30:
                
                if self.o > 30:
                    self.attack = True
                    p1.health -= 1
                    if self.o > 30:
                        self.o = 1
            else:    
                self.x -= self.speed
                self.left =  True
                self.right = False
                self.attack = False
        
       
       
    def hit(self):
        self.health -= 1
        if self.health == 0:
            self.visable = False           

p1 = Player(400,450,5,8,128,128) 


move = 0
enemys = []
by = pygame.image.load("byc.png")
character = pygame.image.load("idle_right\idle1.png")
character2 = pygame.image.load("idle_left\idle1.png")
enemys.append(Enemy(-100,450,128,128,4,900))

def win():
    p1.x =  p1.start_x
    p1.y =  p1.start_y
        
    text_win = font2.render("You Win ", 1,GREEN)
    screen.blit(text_win, (450, 250))
    time = 1
    while time < 500:
            pygame.display.update()
            time += 1
            pygame.time.delay(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
def uptdate_fill_chr_by_pleyer():
    text_kill = font2.render("KILL : " +str(kills)  , False, WHITE )
    text_dead = font2.render("DEAD : " +str(deads), False, WHITE )
    health = font2.render("Heath ", False, WHITE )
    global move 
    global by
    screen.blit(by, (p1.back_x,p1.back_y))
    screen.blit(text_kill, (10,10))
    screen.blit(text_dead, (10,50))
    
    global c
    global jump
    jump = random.randrange(0, 9)
    for enemy in enemys:
        if p1.y <= enemy.y:
            p1.draw(screen)
            p1.move()
            
            enemy.draw(screen)
            enemy.move()
        if p1.y > enemy.y:
            
            enemy.draw(screen)
            enemy.move()
            p1.draw(screen)
            p1.move()
    screen.blit(health, (750,20))

    for bullet in bullets:
        if p1.direction == 1:
            screen.blit(bullet_right, (bullet.x, bullet.y))  
        elif p1.direction == -1:
            screen.blit(bullet_left, (bullet.x, bullet.y))                      
    
    #for enemy in enemys:
        #e1.draw(screen)
        #e1.move()
    pygame.display.update()



#import the image in list
idle = pygame.image.load("idle_left\idle1.png")

run_right = [pygame.image.load("run_right\\run1.png"),pygame.image.load("run_right\\run2.png"),pygame.image.load("run_right\\run3.png"),pygame.image.load("run_right\\run4.png"),pygame.image.load("run_right\\run5.png"),pygame.image.load("run_right\\run6.png"),pygame.image.load("run_right\\run7.png"),pygame.image.load("run_right\\run8.png"),pygame.image.load("run_right\\run9.png"),pygame.image.load("run_right\\run10.png")]
run_left = [pygame.image.load("run_left\\run1.png"),pygame.image.load("run_left\\run2.png"),pygame.image.load("run_left\\run3.png"),pygame.image.load("run_left\\run4.png"),pygame.image.load("run_left\\run5.png"),pygame.image.load("run_left\\run6.png"),pygame.image.load("run_left\\run7.png"),pygame.image.load("run_left\\run8.png"),pygame.image.load("run_left\\run9.png"),pygame.image.load("run_left\\run10.png")]

jump_left = [pygame.image.load("jump_left\jump5.png"),pygame.image.load("jump_left\jump5.png"),pygame.image.load("jump_left\jump5.png"),pygame.image.load("jump_left\jump6.png"),pygame.image.load("jump_left\jump6.png"),pygame.image.load("jump_left\jump6.png"),pygame.image.load("jump_left\jump7.png"),pygame.image.load("jump_left\jump7.png")]
jump_right = [pygame.image.load("jump_right\jump5.png"),pygame.image.load("jump_right\jump5.png"),pygame.image.load("jump_right\jump5.png"),pygame.image.load("jump_right\jump6.png"),pygame.image.load("jump_right\jump6.png"),pygame.image.load("jump_right\jump6.png"),pygame.image.load("jump_right\jump7.png"),pygame.image.load("jump_right\jump7.png"),pygame.image.load("jump_right\jump7.png")]

idle_lift = [pygame.image.load("idle_left\idle1.png"),pygame.image.load("idle_left\idle2.png"),pygame.image.load("idle_left\idle3.png"),pygame.image.load("idle_left\idle4.png"),pygame.image.load("idle_left\idle5.png"),pygame.image.load("idle_left\idle6.png")]
idle_right = [pygame.image.load("idle_right\idle1.png"),pygame.image.load("idle_right\idle2.png"),pygame.image.load("idle_right\idle3.png"),pygame.image.load("idle_right\idle4.png"),pygame.image.load("idle_right\idle5.png"),pygame.image.load("idle_right\idle6.png")]

shift_move = [pygame.image.load("shift\shift_R.png"),pygame.image.load("shift\shift_L.png")]

bullet_right = pygame.image.load("bullet_right.png")
bullet_left = pygame.image.load("bullet_left.png")

shot_right = [pygame.image.load("shot_right\shot1.png"),pygame.image.load("shot_right\shot2.png"),pygame.image.load("shot_right\shot3.png"),pygame.image.load("shot_right\shot4.png")]
shot_left = [pygame.image.load("shot_left\shot1.png"),pygame.image.load("shot_left\shot2.png"),pygame.image.load("shot_left\shot3.png"),pygame.image.load("shot_left\shot4.png")]

enemy_run_right = [pygame.image.load("enemy_run_right\\run1.png"),pygame.image.load("enemy_run_right\\run2.png"),pygame.image.load("enemy_run_right\\run3.png"),pygame.image.load("enemy_run_right\\run4.png"),pygame.image.load("enemy_run_right\\run5.png"),pygame.image.load("enemy_run_right\\run6.png"),pygame.image.load("enemy_run_right\\run7.png"),pygame.image.load("enemy_run_right\\run8.png"),pygame.image.load("enemy_run_right\\run9.png"),pygame.image.load("enemy_run_right\\run10.png"),pygame.image.load("enemy_run_right\\run10.png")]
enemy_run_left = [pygame.image.load("enemy_run_left\\run1.png"),pygame.image.load("enemy_run_left\\run2.png"),pygame.image.load("enemy_run_left\\run3.png"),pygame.image.load("enemy_run_left\\run4.png"),pygame.image.load("enemy_run_left\\run5.png"),pygame.image.load("enemy_run_left\\run6.png"),pygame.image.load("enemy_run_left\\run7.png"),pygame.image.load("enemy_run_left\\run8.png"),pygame.image.load("enemy_run_left\\run9.png"),pygame.image.load("enemy_run_left\\run10.png"),pygame.image.load("enemy_run_left\\run10.png")]

enemy_attack_right =[pygame.image.load("enemy_attack_right\\attack_1.png"),pygame.image.load("enemy_attack_right\\attack_2.png"),pygame.image.load("enemy_attack_right\\attack_3.png"),pygame.image.load("enemy_attack_right\\attack_4.png"),pygame.image.load("enemy_attack_right\\attack_5.png"),pygame.image.load("enemy_attack_right\\attack_6.png"),pygame.image.load("enemy_attack_right\\attack_6.png"),pygame.image.load("enemy_attack_right\\attack_6.png")]
enemy_attack_left =[pygame.image.load("enemy_attack_left\\attack_1.png"),pygame.image.load("enemy_attack_left\\attack_2.png"),pygame.image.load("enemy_attack_left\\attack_3.png"),pygame.image.load("enemy_attack_left\\attack_4.png"),pygame.image.load("enemy_attack_left\\attack_5.png"),pygame.image.load("enemy_attack_left\\attack_6.png"),pygame.image.load("enemy_attack_left\\attack_6.png"),pygame.image.load("enemy_attack_left\\attack_6.png")]

is_game = True
is_dead = False

can_attack = True
timer = 1
bullets = []
new_bullets = []
i = 0
while True:
    clock.tick(30)
    if p1.health > 10:
        p1.health = 10
    if p1.health <= 10:
        for enemy in enemys:
            if enemy.health <= 1:
                p1.health += 1 
    for enemy in enemys:
        enemy.o += 1
        if i > 10:
            can_attack = True
        timer += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                is_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                is_dead = False        
        if is_game == False:
            screen.blit(by1, (0,0))
            pygame.display.update()
            
    if kills == 2 and len(enemys) < 2:
        
          
        enemys.append(Enemy(-100,450,128,128,4,900))
    if is_game == True:
        is_dead = False
        uptdate_fill_chr_by_pleyer()

        if p1.health == 0 :
            for enemy in enemys:
                p1.hit()
                deads += 1
                is_game = False
                p1.x = p1.start_x
                p1.health = 10
                
                
                enemy.x = enemy.start
                enemy.health = 10
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        is_game = True
                        p1.x = p1.start_x
                        p1.health = 10

                        enemy.x = enemy.start
                        enemy.health = 10
                        break
        for enemy in enemys:
            if enemy.health == 0:
                #win()
                is_game = True
                kills += 1
                enemy.x = random.choice([-300,1000])
                enemy.y = random.randint(420, 470)
                enemy.visable = True
                enemy.health = 10

        for bullet in bullets[:]:
            for enemy in enemys:
                if bullet.x > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
                    if bullet.y > enemy.hitbox[1] and bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                        bullets.remove(bullet)
                        enemy.hit()
                        
                        
                        

                        print("hit " + str(kills))
                        break
                    else:
                        bullet.x += bullet.speed   
                elif bullet.x < screen_width and bullet.x > 0 :
                    bullet.x += bullet.speed
                else:
                    bullets.remove(bullet)
        
                    break