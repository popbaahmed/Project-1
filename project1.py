#Project1
#Noir Game

import pygame
import random
import sys

# for trun on the engine
pygame.init()
pygame.mixer.init()

# screen control
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("POPBETO")

# FPS
clock = pygame.time.Clock()

# images
by = pygame.image.load("byc.png").convert()
by_dead = pygame.image.load("you_lost.png").convert()
fade_image = pygame.image.load("fade.png").convert()

# sounds
bullet_hit_sound = pygame.mixer.Sound("sound\\bullet_hit.wav")
punch_sound = pygame.mixer.Sound("sound\punch.wav")
punch_sound.set_volume(0.5)
player_sound1 = [pygame.mixer.Sound("sound\Player_5od_ya9.wav"),pygame.mixer.Sound("sound\Player_ely_hykarp_H3OARO.wav"),pygame.mixer.Sound("sound\Player_hrkabku_wa7ed_wa7ed.wav"),pygame.mixer.Sound("sound\Player_moot_ya9.wav")]
player_sound_random = random.randint(0, 20)
hit_enemy_sound = [pygame.mixer.Sound("sound\\ay.wav"),pygame.mixer.Sound("sound\\a7a.wav"),pygame.mixer.Sound("sound\\ahh.wav"),pygame.mixer.Sound("sound\offa.wav"),pygame.mixer.Sound("sound\\ahh_edy_ya_ebn_alkalba.wav")]
spawn_enemy_sound = [pygame.mixer.Sound("sound\\7al2_3leh_yala.wav"),pygame.mixer.Sound("sound\\7al2_3shan_mayhrabsh.wav")]
spawn_enemy = random.randint(0,2)
hit_enemy = random.randint(0,4)
bullet_sound = pygame.mixer.Sound("sound\shot.wav")
bullet_sound.set_volume(.6)
walk_sound = pygame.mixer.Sound("sound\walk_sound.wav")
walk_sound.set_volume(.5)
walk_channel = pygame.mixer.Channel(1)
walk_channel2 = pygame.mixer.Channel(2)

# color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,200, 0)

# counter death and kills
kills = 0
deads = 0

# fonts
font = pygame.font.SysFont("Monospaced", 35, True)
font2 = pygame.font.SysFont("verdana", 30, True)

# player class
class Player:
    character = pygame.image.load("idle_right\idle1.png").convert()
    character2 = pygame.image.load("idle_left\idle1.png").convert()

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
        self.walk = 1

        # for down the hitbox
        if self.shift == True:
            self.hitbox = self.hitbox = (self.x + 50 , self.y + 85 , self.width - 80 , self.height - 100)

        else:
            self.hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
        

    # for player animations and sounds
    def draw(self, screen):
        global move
        global p
        global walk_sound
        p = p_is_normal
        
        if not self.is_jumping:
            shadow.set_alpha(100)
            screen.blit(shadow, (self.x ,self.y ))

        
            

        # if move left
        if self.left == True and self.is_jumping == False:
            screen.blit(run_left[move%len(run_right)//2], (self.x,self.y))
            move += 1
            
            self.walk += 1
            if self.walk >= 5:

                if not walk_channel.get_busy():
                    walk_channel.play(walk_sound)

                else:

                    walk_channel.stop()   

                self.walk = 0    
                
        # if move right 
        elif self.right and self.is_jumping == False :
            screen.blit(run_right[move%len(run_right)//2], (self.x,self.y))
            move += 1
            
            self.walk += 1
            if self.walk >= 5:

                if not walk_channel.get_busy():
                    walk_channel.play(walk_sound)

                else:

                    walk_channel.stop()  

                self.walk = 0    
        # if move and jumping left 
        elif self.left == True and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_left[move%len(jump_left)//2] , (self.x,self.y))
            move += 1

        # if move and jumping right
        elif self.right == True and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_right[move%len(jump_right)//2], (self.x,self.y))
            move += 1

        # if jumping right 
        elif self.c == [0] and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_right[move%len(jump_right)//2] , (self.x,self.y))
            move += 1

        # if jumping left 
        elif self.c == [1] and self.is_jumping == True and self.is_shot == False:
            screen.blit(jump_left[move%len(jump_left)//2] , (self.x,self.y))
            move += 1

            if move == len(idle_right):
                move = 0
        # if shot right
        elif self.is_shot == True and self.c == [0] and self.right ==False and self.left == False and self.is_jumping == False:
            screen.blit(shot_right[self.shift_move], (self.x,self.y))
            self.shift_move += 1  

            if self.shift_move == 4:
                self.shift_move = 0 

        # if shot left        
        elif self.is_shot == True and self.c == [1] and self.right ==False and self.left == False and self.is_jumping == False:
            screen.blit(shot_left[self.shift_move], (self.x,self.y))         
            self.shift_move += 1  

            if self.shift_move == 4:
                self.shift_move = 0  

        # if shift right
        elif self.c == [0] and self.shift == True and self.right == False and self.left == False and self.is_jumping == False:
            if self.is_jumping == True:
                self.shift = False            
            screen.blit(shift_move[0], (self.x,self.y))  

        # if shift right    
        elif self.c == [1] and p1.shift == True and self.right == False and self.left == False and self.is_jumping == False:
            screen.blit(shift_move[1], (self.x,self.y))

            if self.is_jumping == True:
                self.shift = False        

        # if shift idle right
        elif self.c == [0] and self.right == False and self.left == False and self.is_jumping == False and p1.is_shot == False:
            screen.blit(idle_right[self.idle_move], (self.x,self.y))
            walk_channel.stop()  
            p = p_is_normal
            self.idle_move += 1

            if self.idle_move >= 6:
                self.idle_move = 0

        # if shift idle left
        elif self.c == [1] and self.right == False and self.left == False and self.is_jumping == False and p1.is_shot == False:
            screen.blit(idle_lift[self.idle_move], (self.x,self.y))
            walk_channel.stop()  
            p = p_is_normal
            self.idle_move += 1

            if self.idle_move >= 6:
                self.idle_move = 0

        # to draw player hitbox while he shift
        if self.shift == True:
            self.hitbox = self.hitbox = (self.x + 40 , self.y + 85 , self.width - 80 , self.height - 100)
            p = p_is_normal

        # to rest hitbox after is up
        else:
            self.hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
            p = p_is_normal

        # to draw player portrait is_hurted
        if can_attack == True and not enemys == []:
            p = p_is_hurted

        # to draw player portrait angery
        elif self.is_shot == True:
            p = p_is_angery
        elif self.health <= 0:
            p = p_is_dead    
            
        else:
            p = p_is_normal    
        

        # to draw hitbox
        #pygame.draw.rect(screen, RED,self.hitbox, 2)
        
        

        # to draw health par
        pygame.draw.rect(screen, BLACK, (750,50, 10, 10))
        pygame.draw.rect(screen, RED, (750,50 , self.health * 6, 10))
    def move(self):
        global keys
        
        keys = pygame.key.get_pressed()
    
        # to move right
        if (keys[pygame.K_RIGHT ] or keys[pygame.K_d]) and self.x < screen_width - 90 and self.shift == False:
            
            self.x += self.speed
            self.back_x -= self.speed -4
            for blood in bloods:
                blood.x -= self.speed -4
            self.right = True
            self.left = False
            self.c = [0]
        # to move left    
        elif (keys[pygame.K_LEFT ] or keys[pygame.K_a]) and self.x > 0 - 40 and self.shift == False:
            
            self.x -= self.speed
            self.back_x += self.speed -4
            for blood in bloods:
                blood.x += self.speed -4
            self.right = False 
            self.left = True 
            self.c = [1]
        # to shift    
        elif keys[pygame.K_LSHIFT] and self.is_jumping == False:
            
            self.shift = True
            self.right = False
            self.left = False
            self.is_jumping = False
            self.is_shot = False
        # to shot 
        elif keys[pygame.K_l] and self.y > 400 and self.y < screen_height - 120 and self.is_jumping == False:
            self.is_shot = True
            self.right =False  
            self.left = False  
            self.is_jumping = False
            self.idle_move = False

            if len(bullets) < 3:
                bullet_sound.play()
                self.direction = 0

                if self.c == [0]:
                    self.direction = 1

                elif self.c == [1]:
                    self.direction = -1

                bullets.append(Bullet(round(self.x + self.width // 2 ), round(self.y + self.height // 2 + 23), 50 ,self.direction ))       
                        
        else:
            self.right = False
            self.left = False
            self.shift = False
            self.is_shot = False
            
        # if not jumping 
        if not self.is_jumping:
            # to move up 
            if (keys[pygame.K_UP ] or keys[pygame.K_w]) and self.y > 420 :
                self.y -= self.speed - 3

                if self.c == [0]:
                    self.right =True 
                    self.left = False

                elif self.c == [1]:
                    self.right = False 
                    self.left = True   
            # to move down 
            elif (keys[pygame.K_DOWN ] or keys[pygame.K_s]) and self.y < screen_height - 130:
                self.y += self.speed - 3

                if self.c == [0]:
                    self.right =True 
                    self.left = False

                elif self.c == [1]:
                    self.right = False 
                    self.left = True   

            # to inable jump  
            elif keys[pygame.K_SPACE]:
                self.is_jumping = True
                self.is_shot = False

        
                    
        # to disable shift and shot while he is jumping
        elif self.is_jumping and self.y > 350 and self.shift == False and self.is_shot == False:
            self.shift = False
            self.is_shot = False

            # for add limt to jump            
            if self.speed_jump >= -8:
                p = 1
                self.shift = False

                if self.speed_jump <= 0 and self.y < screen_height - 130:
                    p = -1
                # jumping mecanic
                self.y -= (self.speed_jump ** 2) * 0.25 * p
                self.speed_jump -= 1

            else:
                self.is_jumping = False
                self.speed_jump = 8 
            
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
        time = 0
        while time < 500:
            pygame.display.update()
            time += 1

            if time >= 500:
                time = 0

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
# bullet class 
class Bullet:
    def __init__(self, x,y ,speed, direction) :

        self.x =x
        self.y = y
        self.speed = speed * direction
        self.direction = direction  
                       
# enemy class
class Enemy:
    def __init__(self,x,y,width,height,speed,end):
        self.x = x
        self.y = y
        self.width = 128
        self.height = 128
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
        # enemy hitbox
        self.e_hitbox = (self.x + 20 , self.y + 75 , self.width - 80 , self.height - 10)
        self.attack = False
        self.o = 1
        self.k = 0
        self.is_death = False
        self.dead_move = 0
        self.blood = 0
    def draw(self, screen):

        shadow.set_alpha(100)
        screen.blit(shadow, (self.x,self.y ))

        if self.is_death == False:
        
            if self.attack and self.right:
                screen.blit(enemy_attack_right[self.attack1//2],(self.x,self.y)) 
                self.attack1 += 1

                if self.attack1 >= 10:
                    self.attack1 = 0  
                    punch_sound.play()  
                    

            elif self.attack and self.left:
                screen.blit(enemy_attack_left[self.attack2//2],(self.x,self.y)) 
                self.attack2 += 1

                if self.attack2 >= 10:
                    self.attack2 = 0      
                    punch_sound.play()      

            if self.right and self.attack == False:
                screen.blit(enemy_run_right[self.move1//2], (self.x,self.y))
                self.move1 += 1

                if self.move1 > 9*2:
                    self.move1 = 0
                    walk_sound.play()

            elif self.left and self.attack == False:
                screen.blit(enemy_run_left[self.move1//2], (self.x,self.y))
                self.move1 += 1

                if self.move1 > 9*2:
                    self.move1 = 0       
                    walk_sound.play() 
            
            self.e_hitbox = (self.x + 40 , self.y + 75 , self.width - 80 , self.height - 100)
            pygame.draw.rect(screen, RED, (self.e_hitbox), 2)       
            pygame.draw.rect(screen, RED, (self.e_hitbox[0], self.e_hitbox[1] - 30, 50, 5))
            pygame.draw.rect(screen, GREEN, (self.e_hitbox[0] , self.e_hitbox[1] - 30, self.health * 5, 5))

        elif self.is_death == True :  
            pass

    def move(self):

        global p
        global can_attack
        
        if self.is_death == False:

            if self.x < p1.x :

                if self.x > p1.x -30:
                    
                    if self.o > 30 and not enemys == []:
                        can_attack =True
                        self.attack = True
                        p = p_is_hurted
                        if self.attack1 >= 0:
                            p1.health -= 1

                        if self.o > 30:
                            self.o = 1
                else:    
                    self.x += self.speed
                    self.left = False
                    self.right = True
                    self.attack = False
                    can_attack = False
            
            elif self.x > p1.x :
                if self.x < p1.x +30:
                    
                    if self.o > 30 and not enemys == [] :
                        can_attack = True
                        self.attack = True
                        p = p_is_hurted
                        if self.attack2 >= 0:
                            p1.health -= 1
                        
                        if self.o > 30:
                            self.o = 1

                else:    
                    self.x -= self.speed
                    self.left =  True
                    self.right = False
                    self.attack = False
                    can_attack = False

        else:
            pass           
       
    def e_hit(self):
        if self.is_death == False:
            global enemys
            global kills
            self.health -= 1
            for i in range(0, 9):
                screen.blit(blood_effect[self.blood], (self.x, self.y)) 
                self.blood += 1  
                if self.blood >= 9:
                    self.blood = 0
            if self.health == 0:
                kills += 1   
                self.health -= 1
        else:
            pass    
    
    def e_dead(self, screen):
        # for knwon if enemy id dead or on to run animations
        if self.is_death == True :
            # if dead right 
            if self.right == True:
                screen.blit(enemy_dead_right[self.dead_move//2], (self.x,self.y))
                self.dead_move += 1
                self.k += 1
                if self.dead_move >= 10 * 2:
                    self.dead_move = 7
            # if dead left        
            if self.left == True:
                screen.blit(enemy_dead_left[self.dead_move//2], (self.x,self.y)) 
                self.dead_move += 1
                self.k += 1
                if self.dead_move >= 10 * 2:
                    self.dead_move = 7   
            
        else: pass        

class Particals:
    def __init__(self, x,y) :
        self.x = x
        self.y= y
        self.blood_effect = [pygame.image.load("blood\\blood_1.png").convert_alpha(),pygame.image.load("blood\\blood_2.png").convert_alpha(),pygame.image.load("blood\\blood_3.png").convert_alpha(),pygame.image.load("blood\\blood_4.png").convert_alpha(),pygame.image.load("blood\\blood_5.png").convert_alpha(),pygame.image.load("blood\\blood_6.png").convert_alpha(),pygame.image.load("blood\\blood_7.png").convert_alpha(),pygame.image.load("blood\\blood_8.png").convert_alpha(),pygame.image.load("blood\\blood_9.png").convert_alpha()]        
        self.index = 0
        self.image = self.blood_effect[self.index]
        self.counter = 0
        self.speed = 1
        self.finished = False

    def update_effect(self):
        self.counter += 1 
        if self.counter >= self.speed :
            self.counter = 0
            if self.index <= len(self.blood_effect) - 5:
                self.index += 1
                self.image = self.blood_effect[self.index]
            else :
                self.finished = True

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))     
         
class Blood:
    def __init__(self, x,y):
        self.x =x
        self.y = y
    def draw(self, screen):
        random_blood = 0
        screen.blit(floor_blood[random_blood] ,(self.x, self.y))

def fade_def():
    fade = 0
    
    for i in range(0,100):
            pygame.time.delay(10)
            fade += 1 
            fade_image.set_alpha(fade) 
            screen.blit(fade_image,(0,0))
            pygame.display.update()
            
            if i >= 100:
                fade =0
                pygame.display.update()
    
    fade_image.set_alpha(fade) 
    screen.blit(fade_image,(0,0))
    pygame.display.update()       
                     
p1 = Player(400,450,5,8,128,128) 

move = 0
enemys = []
by_menu = pygame.image.load("by_menu.png").convert()
character = pygame.image.load("idle_right\idle1.png").convert()
character2 = pygame.image.load("idle_left\idle1.png").convert()

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
                    sys.exit()

def uptdate_fill_chr_by_pleyer():
    text_kill = font2.render("KILL : " +str(kills)  , False, WHITE )
    text_dead = font2.render("DEAD : " +str(deads), False, WHITE )
    # health = font2.render("Heath ", False, WHITE )
    global move 
    global by
    screen.blit(by, (p1.back_x,p1.back_y))
    screen.blit(text_kill, (10,10))
    screen.blit(text_dead, (10,50))
    
    global c
    global jump
    jump = random.randrange(0, 9)
    for blood in bloods:
        
        blood.draw(screen)

    p1.draw(screen)
    p1.move()
    
    for enemy in enemys:

        if enemy.health <= 0:
            enemy.is_death = True
            enemy.e_dead(screen)

        else:    
            enemy.move()
            enemy.draw(screen)

    for part in effect_blood:
        part.draw(screen)
    # screen.blit(health, (700,40))

    for bullet in bullets:

        if p1.direction == 1:
            screen.blit(bullet_right, (bullet.x, bullet.y))  

        elif p1.direction == -1:
            screen.blit(bullet_left, (bullet.x, bullet.y))  

    screen.blit(p, (800,0))                            
    screen.blit(health_par_fram, (700, 20))
    
    pygame.display.update()

#import the image in list
health_par_fram = pygame.image.load("health_par_fram.png").convert_alpha()

character_portrait = [pygame.image.load("portrait\character_normal.png").convert_alpha(),pygame.image.load("portrait\character_angery.png").convert_alpha(),pygame.image.load("portrait\character_hurted.png").convert_alpha(),pygame.image.load("portrait\character_dead.png").convert_alpha()]

p_is_normal = character_portrait[0]
p_is_angery = character_portrait[1]
p_is_hurted = character_portrait[2]
p_is_dead = character_portrait[3]

p = p_is_normal

shadow = pygame.image.load("shadow.png").convert_alpha()

floor_blood = [pygame.image.load("floor_blood\\blood_floor.png").convert_alpha(), pygame.image.load("floor_blood\\blood_floor2.png").convert_alpha()]

blood_effect = [pygame.image.load("blood\\blood_1.png").convert_alpha(),pygame.image.load("blood\\blood_2.png").convert_alpha(),pygame.image.load("blood\\blood_3.png").convert_alpha(),pygame.image.load("blood\\blood_4.png").convert_alpha(),pygame.image.load("blood\\blood_5.png").convert_alpha(),pygame.image.load("blood\\blood_6.png").convert_alpha(),pygame.image.load("blood\\blood_7.png").convert_alpha(),pygame.image.load("blood\\blood_8.png").convert_alpha(),pygame.image.load("blood\\blood_9.png").convert_alpha()]

idle = pygame.image.load("idle_left\idle1.png")

run_right = [pygame.image.load("run_right\\run1.png").convert_alpha(),pygame.image.load("run_right\\run2.png").convert_alpha(),pygame.image.load("run_right\\run3.png").convert_alpha(),pygame.image.load("run_right\\run4.png").convert_alpha(),pygame.image.load("run_right\\run5.png").convert_alpha(),pygame.image.load("run_right\\run6.png").convert_alpha(),pygame.image.load("run_right\\run7.png").convert_alpha(),pygame.image.load("run_right\\run8.png").convert_alpha(),pygame.image.load("run_right\\run9.png").convert_alpha(),pygame.image.load("run_right\\run10.png").convert_alpha()]
run_left = [pygame.image.load("run_left\\run1.png").convert_alpha(),pygame.image.load("run_left\\run2.png").convert_alpha(),pygame.image.load("run_left\\run3.png"),pygame.image.load("run_left\\run4.png"),pygame.image.load("run_left\\run5.png").convert_alpha(),pygame.image.load("run_left\\run6.png").convert_alpha(),pygame.image.load("run_left\\run7.png").convert_alpha(),pygame.image.load("run_left\\run8.png").convert_alpha(),pygame.image.load("run_left\\run9.png").convert_alpha(),pygame.image.load("run_left\\run10.png").convert_alpha()]

jump_left = [pygame.image.load("jump_left\jump5.png").convert_alpha(),pygame.image.load("jump_left\jump5.png").convert_alpha(),pygame.image.load("jump_left\jump5.png").convert_alpha(),pygame.image.load("jump_left\jump6.png").convert_alpha(),pygame.image.load("jump_left\jump6.png").convert_alpha(),pygame.image.load("jump_left\jump6.png").convert_alpha(),pygame.image.load("jump_left\jump7.png").convert_alpha(),pygame.image.load("jump_left\jump7.png").convert_alpha()]
jump_right = [pygame.image.load("jump_right\jump5.png").convert_alpha(),pygame.image.load("jump_right\jump5.png").convert_alpha(),pygame.image.load("jump_right\jump5.png").convert_alpha(),pygame.image.load("jump_right\jump6.png").convert_alpha(),pygame.image.load("jump_right\jump6.png").convert_alpha(),pygame.image.load("jump_right\jump6.png").convert_alpha(),pygame.image.load("jump_right\jump7.png").convert_alpha(),pygame.image.load("jump_right\jump7.png").convert_alpha(),pygame.image.load("jump_right\jump7.png").convert_alpha()]

idle_lift = [pygame.image.load("idle_left\idle1.png").convert_alpha(),pygame.image.load("idle_left\idle2.png").convert_alpha(),pygame.image.load("idle_left\idle3.png").convert_alpha(),pygame.image.load("idle_left\idle4.png").convert_alpha(),pygame.image.load("idle_left\idle5.png").convert_alpha(),pygame.image.load("idle_left\idle6.png").convert_alpha()]
idle_right = [pygame.image.load("idle_right\idle1.png").convert_alpha(),pygame.image.load("idle_right\idle2.png").convert_alpha(),pygame.image.load("idle_right\idle3.png").convert_alpha(),pygame.image.load("idle_right\idle4.png").convert_alpha(),pygame.image.load("idle_right\idle5.png").convert_alpha(),pygame.image.load("idle_right\idle6.png").convert_alpha()]

shift_move = [pygame.image.load("shift\shift_R.png").convert_alpha(),pygame.image.load("shift\shift_L.png").convert_alpha()]

bullet_right = pygame.image.load("bullet_right.png").convert_alpha()
bullet_left = pygame.image.load("bullet_left.png").convert_alpha()

shot_right = [pygame.image.load("shot_right\shot1.png").convert_alpha(),pygame.image.load("shot_right\shot2.png").convert_alpha(),pygame.image.load("shot_right\shot3.png").convert_alpha(),pygame.image.load("shot_right\shot4.png").convert_alpha()]
shot_left = [pygame.image.load("shot_left\shot1.png").convert_alpha(),pygame.image.load("shot_left\shot2.png").convert_alpha(),pygame.image.load("shot_left\shot3.png").convert_alpha(),pygame.image.load("shot_left\shot4.png").convert_alpha()]

enemy_run_right = [pygame.image.load("enemy_run_right\\run1.png").convert_alpha(),pygame.image.load("enemy_run_right\\run2.png").convert_alpha(),pygame.image.load("enemy_run_right\\run3.png").convert_alpha(),pygame.image.load("enemy_run_right\\run4.png").convert_alpha(),pygame.image.load("enemy_run_right\\run5.png").convert_alpha(),pygame.image.load("enemy_run_right\\run6.png").convert_alpha(),pygame.image.load("enemy_run_right\\run7.png").convert_alpha(),pygame.image.load("enemy_run_right\\run8.png").convert_alpha(),pygame.image.load("enemy_run_right\\run9.png").convert_alpha(),pygame.image.load("enemy_run_right\\run10.png").convert_alpha(),pygame.image.load("enemy_run_right\\run10.png").convert_alpha()]
enemy_run_left = [pygame.image.load("enemy_run_left\\run1.png").convert_alpha(),pygame.image.load("enemy_run_left\\run2.png").convert_alpha(),pygame.image.load("enemy_run_left\\run3.png").convert_alpha(),pygame.image.load("enemy_run_left\\run4.png").convert_alpha(),pygame.image.load("enemy_run_left\\run5.png"),pygame.image.load("enemy_run_left\\run6.png").convert_alpha(),pygame.image.load("enemy_run_left\\run7.png"),pygame.image.load("enemy_run_left\\run8.png").convert_alpha(),pygame.image.load("enemy_run_left\\run9.png").convert_alpha(),pygame.image.load("enemy_run_left\\run10.png").convert_alpha(),pygame.image.load("enemy_run_left\\run10.png").convert_alpha()]

enemy_attack_right =[pygame.image.load("enemy_attack_right\\attack_1.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_2.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_3.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_4.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_5.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_6.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_6.png").convert_alpha(),pygame.image.load("enemy_attack_right\\attack_6.png").convert_alpha()]
enemy_attack_left =[pygame.image.load("enemy_attack_left\\attack_1.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_2.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_3.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_4.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_5.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_6.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_6.png").convert_alpha(),pygame.image.load("enemy_attack_left\\attack_6.png").convert_alpha()]

enemy_dead_right = [pygame.image.load("enemy_dead_right\dead_1.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_2.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_3.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_4.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_5.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_6.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_right\dead_7.png").convert_alpha()]
enemy_dead_left = [pygame.image.load("enemy_dead_left\dead_1.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_2.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_3.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_4.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_5.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_6.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_7.png").convert_alpha(),pygame.image.load("enemy_dead_left\dead_7.png").convert_alpha()]   

is_game = False
is_dead = False

by1_music = ["sound\konstantinpazuzustudio-police-interrogation-asmr-noir-jazz-520244.mp3", "sound\lilliben-cinematic-shadows-noir-soundscapes-365176.mp3", "sound\joelfazhari-donx27t-look-down-the-basement-true-crime-thriller-loopable-music-132133.mp3"]
music = 0

pygame.mixer.music.fadeout(1000)
pygame.mixer.music.load(by1_music[0])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.5)

can_attack = False
bloods = []
effect_blood = []
bullets = []
new_bullets = []
number_enemys = 0
i = 0

while True:
    clock.tick(30)
    x = random.choice([-300, 1000])
    y = random.randint(420, 440)
    # Quit event
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        # start game 
        if event.type == pygame.KEYDOWN:

            if is_game == False:

                if event.key == pygame.K_RETURN:
                    fade_def()
                    bloods = []
                    effect_blood = []
                    is_dead = False
                    is_game = True    
                    kills = 0
                    p1 = Player(400,450,5,8,128,128)
                    enemys = []
                    pygame.mixer.music.fadeout(1000)
                    pygame.mixer.music.load(by1_music[1])
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(-1)
                
        # to back to the main menu
        if event.type == pygame.KEYDOWN:
            if is_dead == True and  event.key == pygame.K_BACKSPACE:
                fade_def()
                deads =0
                bloods = []
                effect_blood = []
                is_dead = False 
                is_game = False
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load(by1_music[0])
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)          
    
    if p1.health <= 0: 
        p = p_is_dead
        fade_def()
        if is_game == False and p == p_is_dead:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load(by1_music[2])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        
    if is_dead == True :
               
        p1 = Player(400,450,5,8,128,128)
        enemys = []
        screen.blit(by_dead, (0,0))
        pygame.display.update()  
        
    # the main menu
    if is_game == False and is_dead == False :
        music = 0
        screen.blit(by_menu, (0,0))
        pygame.display.update()  

    # the game loop
    if is_game == True :

        music = 1
        # to test the enemy
        try:
            keys1 = pygame.key.get_pressed()
            if keys1[pygame.K_1]:
                enemys.append(Enemy(x,y,128,128,4,900))
        except:
            pass        

        if p1.health <= 0 :
            deads = 1
            is_game = False
            is_dead = True
        # respawn enemys   
        if len(enemys) == 0 :
                     
            if kills >= 5 and kills <= 9:
                spawn_enemy = random.randint(0,1)
                spawn_enemy_sound[spawn_enemy].play()
                x1 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y1 = random.randint(425, 430)
                enemys.append(Enemy(x1,y1,128,128,4,900))
                x2 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y2 = random.randint(440, 470)            
                enemys.append(Enemy(x2,y2,128,128,4,900))

            elif kills >= 10 and kills <= 29:
                x1 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y1 = random.randint(425, 430)
                enemys.append(Enemy(x1,y1,128,128,4,900))
                x2 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y2 = random.randint(445, 455)            
                spawn_enemy = random.randint(0,1)
                spawn_enemy_sound[spawn_enemy].play()
                enemys.append(Enemy(x2,y2,128,128,4,900))
                x3 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y3 = random.randint(460, 470)            
                enemys.append(Enemy(x3,y3,128,128,4,900))

            elif kills >= 30 and kills <= 50:
                x1 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y1 = random.randint(425, 430)
                enemys.append(Enemy(x1,y1,128,128,4,900))
                x2 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y2 = random.randint(435, 445)            
                enemys.append(Enemy(x2,y2,128,128,4,900))
                x3 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y3 = random.randint(450, 455)            
                enemys.append(Enemy(x3,y3,128,128,4,900))  
                x4 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y4 = random.randint(460, 470)            
                enemys.append(Enemy(x4 ,y4,128,128,4,900))
                spawn_enemy = random.randint(0,1)
                spawn_enemy_sound[spawn_enemy].play()
                
            if kills < 5:
                x1 = random.choice([-400,-300, -200, 900, 1000, 1100])
                y1 = random.randint(425, 470)
                enemys.append(Enemy(x1,y1,128,128,4,900)) 

            else:
                pass   
        # enemy time attack
        for enemy in enemys:
            enemy.o += 1

            if i > 5:
                can_attack = True
                
            i = 1

        # mave and collison for bullet
        for bullet in bullets: 
            # calculating coordinates for bullet 
            bullet_rect = pygame.Rect(bullet.x,bullet.y, 5, 10)

            for enemy in enemys:  
                # collison with enemy 
                if bullet_rect.colliderect(enemy.e_hitbox) and enemy.is_death == False:
                    try:
                        if not len(bullets) == len(new_bullets):
                            bullet_hit_sound.set_volume(.3)
                            bullet_hit_sound.play()
                            bullets.remove(bullet)
                                                        
                    except:
                        pass    
                    try:
                        hit_enemy = random.randint(0,10)
                        hit_enemy_sound[hit_enemy].set_volume(0.5)
                        hit_enemy_sound[hit_enemy].play()    
                    except:
                        pass
                    effect_blood.append(Particals(enemy.x + 40, enemy.y + 70))

                    enemy.e_hit()
                                       
                    if enemy.health <= 0:
                        try:
                            player_sound_random = random.randint(0, 9)
                            player_sound1[player_sound_random].set_volume(2)
                            player_sound1[player_sound_random].play()
                        except:
                            pass                      
                        random_blood = random.randint(0, 1)        
                        bloods.append(Blood(enemy.x ,enemy.y))                   
                        enemy.is_death = True
                        enemy.e_dead(screen)
                        enemy.k += 1
                        
                        break
                        
                    else:
                        bullet.x += bullet.speed           
            if bullet.x > 0 and bullet.x < screen_width :
                bullet.x += bullet.speed 
                
            else :
                try:
                    if not len(bullets) == len(new_bullets):
                        bullets.remove(bullet)
                        break
                except:
                    pass    
                    break

        for enemy in enemys:

            if enemy.health <= 0:

                enemy.is_death = True
                enemy.e_dead(screen)
                enemy.k += 1

                if enemy.k >= 20:
                    enemys.remove(enemy)        
        for part in effect_blood[:]:
            try:
                part.update_effect()  
                part.draw(screen)
                if part.finished:
                    effect_blood.remove(part)  
            except:
                pass                
        uptdate_fill_chr_by_pleyer()