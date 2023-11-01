import pygame
import math
import time

pygame.init()


def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False
WIDTH,HEIGHT = 800,800

sprite_img = pygame.image.load('231007 - Filip top down car1.png')
window = pygame.display.set_mode((WIDTH,HEIGHT))

def angle (angle):
    
    ddx = 0
    ddy = 0
    if angle < 22.5 or angle > 337.5:
        ddx = 0
        ddy = -1
            
    if angle > 22.5 and angle <= 67.5:
        ddx = -0.7
        ddy = -0.7

        
    if angle > 67.5 and angle <= 112.5:
        ddx = -1
        ddy = 0
        
    if angle > 112.5 and angle <= 157.5:
        ddx = -0.7
        ddy = 0.7
            
    if angle > 157.5 and angle <= 202.5:
        ddx = 0
        ddy = 1
        
    #225 angle       
    if angle > 202.5 and angle <= 247.5:
        ddx = 0.7
        ddy = 0.7
        
    #270
    if angle > 247.5 and angle <= 292.5:
        ddx = 1
        ddy = 0
        
            
    if angle > 292.5 and angle <= 337.5:
        ddx = 0.7
        ddy = -0.7

    return [ddx,ddy]

#bullet goes faster so faster dx and dy

def angle1(angle):
    
    ddx = 0
    ddy = 0
    if angle < 22.5 or angle > 337.5:
        ddx = 0
        ddy = -280
            
    if angle > 22.5 and angle <= 67.5:
        ddx = -160
        ddy = -160

        
    if angle > 67.5 and angle <= 112.5:
        ddx = -280
        ddy = 0
        
    if angle > 112.5 and angle <= 157.5:
        ddx = -160
        ddy = 160
            
    if angle > 157.5 and angle <= 202.5:
        ddx = 0
        ddy = 280
        
    #225 angle       
    if angle > 202.5 and angle <= 247.5:
        ddx = 160
        ddy = 160
        
    #270
    if angle > 247.5 and angle <= 292.5:
        ddx = 280
        ddy = 0
        
            
    if angle > 292.5 and angle <= 337.5:
        ddx = 160
        ddy = -160

    return [ddx,ddy]

class Player:
    def __init__(self,x,y,dx,dy,height,speed,gold,angle,ddx,ddy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = 0.001
        self.ddy = 0.001
        self.maxdy = 2.5
        self.maxdx = 2.5
        self.speed = speed
        self.angle = angle
        self.size = 35
        self.sprite_img = pygame.image.load('231007 - Filip top down car1.png')
        self.width = self.sprite_img.get_width()*0.15
        self.height = height
        self.scaled_img = pygame.transform.scale(self.sprite_img, (self.width, self.height))
        self.gold = gold
        self.ddx = ddx
        self.ddy = ddy
        
        
    def draw(self, window):
        rotated_img = pygame.transform.rotate(self.scaled_img, self.angle)
        self.width = rotated_img.get_width()
        self.height = rotated_img.get_height()
        window.blit(rotated_img, (self.x - self.width/2, self.y - self.height/2))
        
    def draw_above(self,window):
        pygame.draw.rect(window, pygame.Color("Red"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        pygame.draw.rect(window, pygame.Color("blue"), 
        pygame.Rect(self.x + 3, self.y + 5,74,50))
        pygame.draw.rect(window, pygame.Color("black"), 
        pygame.Rect(self.x - 10, self.y + 20,10,40))
        pygame.draw.rect(window, pygame.Color("black"), 
        pygame.Rect(self.x + self.width, self.y + 20,10,40))
        pygame.draw.rect(window, pygame.Color("black"), 
        pygame.Rect(self.x - 10, self.y + 70,10,40))
        pygame.draw.rect(window, pygame.Color("black"), 
        pygame.Rect(self.x + self.width, self.y + 70,10,40))
        
    def draw_side(self,window):
        pygame.draw.rect(window, pygame.Color("Red"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        pygame.draw.circle(window, pygame.Color("Black"), (self.x,self.y + self.height), self.size)
        pygame.draw.circle(window, pygame.Color("Gray"), (self.x,self.y + self.height), 15)
        pygame.draw.rect(window, pygame.Color("blue"), 
        pygame.Rect(self.x + 50, self.y,70,50))
        pygame.draw.circle(window, pygame.Color("Black"), (self.x + self.width,self.y + self.height), self.size)
        pygame.draw.circle(window, pygame.Color("Gray"), (self.x + self.width,self.y + self.height), 15)
    
    def move(self, keys):
        self.maxdy = 2.5
        self.maxdx = 2.5
        
        ddx, ddy = angle(self.angle)
        

        
        rotated_img = pygame.transform.rotate(self.scaled_img, self.angle)
        self.width = rotated_img.get_width()
        self.height = rotated_img.get_height()
        
        if self.y <= 31:
            self.y = 31
        
        if self.y >= 769:
            self.y = 769
        
        if self.x >= 769:
            self.x = 769
        
        if self.x <= 31:
            self.x = 31
        
        if keys[pygame.K_a]:
            self.angle += 0.1
        elif keys[pygame.K_d]:
            self.angle -= 0.1
        

                
        acceleration = 0
        if self.x > 0 and self.x < 800 and self.y > 0 and self.y < 800:
            if keys[pygame.K_w]:
                acceleration = self.speed

                
        if self.x > 0 and self.x < 800 and self.y > 0 and self.y < 800:
            if keys[pygame.K_s]:
                acceleration = -self.speed
        
        self.dx = self.dx + ddx * acceleration
        self.dy = self.dy + ddy * acceleration
        
        NEWx = self.x + self.dx
        NEWy = self.y + self.dy
        if NEWx > 10 + self.width/2 and NEWx < 790 - self.width/2 and NEWy > 10 + self.height/2 and NEWy < 790 - self.height/2:
            self.y = NEWy
            self.x = NEWx
        friction = 0.9975
        self.dx = self.dx * friction
        self.dy = self.dy * friction
        
        if self.angle < 0:
            self.angle = self.angle + 360
        
        if self.angle > 360:
            self.angle = self.angle - 360
        


p1 = Player(300,300,0,0,sprite_img.get_height()*0.15,0.0008,0,0,0,0)

class Laser:
    def __init__(self,x,y,rad,dx,dy,speed,active):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.speed = speed
        self.active = active
        self.angle = p1.angle
    def draw(self,window):
        pygame.draw.circle(window, pygame.Color("Red"), (self.x, self.y),self.rad) # Draws a laser
    def move(self):
        self.dx, self.dy = angle1(self.angle)
        
        if self.angle < 0:
            self.angle = self.angle + 360
        
        if self.angle > 360:
            self.angle = self.angle - 360
        
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        
    
    
    
    
class Bouncing_Ball:
    def __init__(self,x,y,dx,dy,ddx,ddy,rad,size,speed):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = ddx
        self.ddy = ddy
        self.rad = rad
        self.size = size
        self.speed = speed
        self.coverd = 0
    def draw(self,window):
        pygame.draw.circle(window,pygame.Color("Blue"),(self.x,self.y),self.size)
    def move(self):
        self.y += self.dy*self.speed
        self.dy+=self.ddy
        self.x += self.dx*self.speed
        if self.x <= self.size:
            self.dx = 1
        if self.dx != 0:
            self.x += self.dx*self.speed
        if self.x >= WIDTH - self.size:
            self.dx = -1
        if self.y >= HEIGHT - self.size:
            self.dy = -1*self.dy
        else:
            self.coverd = self.coverd + self.dx*self.speed
            
class Button:
    def __init__(self,x,y,width,height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.my_font = pygame.font.SysFont('Comic Sans MS', 70)
        self.my_font1 = pygame.font.SysFont('Comic Sans MS', 20)
    def draw(self,window,player):
        pygame.draw.rect(window, pygame.Color("Black"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        
write_gold = 0
main_menu = 1
myfont1 = pygame.font.SysFont('Comic Sans MS', 15)

ball = Bouncing_Ball(300,300,1,1,0,0.002,75,75,0.06)


l_lasers = []


l_buttons = []
button = Button(250,300,250,150, "Play")
l_buttons.append(button)

shop = Button(250,600,250,150, "Shop")
l_buttons.append(shop)

upgrade_speed = Button(50,50,110,46.5,"upgrade speed")
l_buttons.append(upgrade_speed)

upgrade_speed2 = Button(210,50,110,46.5,"upgrade speed 2")
l_buttons.append(upgrade_speed2)

was_holding = False

class Debug_mode:
    def __init__(self,window):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 15)
        self.window = window
    def draw(self,angle,game,y,gold,button,tet,shop,shop_inside):
        if game == 1:
            text_surface = self.myfont1.render(f"Player angle {int(angle)}", True, (0, 0, 0))
            text_surface2 = self.myfont1.render(f"Player y {int(y)}", True, (0, 0, 0))
            text_surface3 = self.myfont1.render(f"Player gold {int(p1.gold)}", True, (0, 0, 0))
            
            self.window.blit(text_surface3, (0,100))
            self.window.blit(text_surface2, (0,50))
            self.window.blit(text_surface, (0,0))
            
        if main_menu == 1:
            text_surface1 = self.myfont.render("Main menu", True, (255,0,0))
            window.blit(text_surface1, (button.x + button.width / 2 - 135,button.y + button.height / 2 - 325))
            
            text_surface7 = self.myfont.render(shop.text, True, (255,255,255))
            window.blit(text_surface7, (shop.x + shop.width / 2 - 100,shop.y + shop.height / 2 - 55))
            
            text_surface6 = self.myfont.render(button.text, True, (255,255,255))
            window.blit(text_surface6, (button.x + button.width / 2 - 100,button.y + button.height / 2 - 55))
            
        if shop_inside == 1:
            text_surface11 = self.myfont1.render("Upgrade speed", True, (255,255,255))
            window.blit(text_surface11, (upgrade_speed.x + upgrade_speed.width / 2 - 50,upgrade_speed.y + upgrade_speed.height / 2 - 20))

            text_surface11 = self.myfont1.render("Upgrade speed 2", True, (255,255,255))
            window.blit(text_surface11, (upgrade_speed2.x + upgrade_speed2.width / 2 - 50,upgrade_speed2.y + upgrade_speed2.height / 2 - 20))

            text_surface11 = self.myfont1.render("500 gold", True, (255,255,255))
            window.blit(text_surface11, (upgrade_speed2.x + upgrade_speed2.width / 2 - 50,upgrade_speed2.y + upgrade_speed2.height / 2))
        
            text_surface11 = self.myfont1.render("300 gold", True, (255,255,255))
            window.blit(text_surface11, (upgrade_speed.x + upgrade_speed.width / 2 - 50,upgrade_speed.y + upgrade_speed.height / 2))


text = Debug_mode(window)
es = 0
ab = 0
def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False



s = 0

prev = 0
"""
f = open("test.txt", "w")
contents = f.read(w)
lines = contents.split("\n")
write_gold = write_gold + p1.gold
f.write(write_gold)
f.close()
"""
shop_inside = 0
d = 0
game = 0
g = 0

was_holding = False

def read(writegold):
    f = open("test.txt", "w")
    writegold += p1.gold
    f.write(str(writegold))
    f.close()
    return writegold

clock = pygame.time.Clock()
cool = 0
while True:

    window.fill("White")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    
    for event in events:
        if event.type == pygame.QUIT:
            read(write_gold)
            exit()
            
    if main_menu == 1:
        
        button.draw(window,p1)
        shop.draw(window,p1)
        myfont = pygame.font.SysFont('Comic Sans MS', 70)
        my_font = pygame.font.SysFont('Comic Sans MS', 70)
        if button_colision(button.width,button.height,button.x,button.y,mousePos,mouseState):
            game = 1
            main_menu = 0
            shop_inside = 0
        if button_colision(shop.width,shop.height,shop.x,shop.y,mousePos,mouseState):
            game = 0
            main_menu = 0
            shop_inside = 1
    
    
    
    if shop_inside == 1:
        if g == 0:
            f = open("test.txt", "r")
            write_gold = int(f.read()) + p1.gold
            f.close()
            g = 1
        upgrade_speed.draw(window,p1)
        upgrade_speed2.draw(window,p1)
        if write_gold >= 300:
            if button_colision(upgrade_speed.width,upgrade_speed.height,upgrade_speed.x,upgrade_speed.y,mousePos,mouseState):
                p1.speed = 0.0015
                write_gold -= 300
                ab = 1
                
        else:
            if ab != 1:
                text_surface22 = myfont1.render("Not enough gold", True, (0,0,0))
                window.blit(text_surface22, (upgrade_speed.x + upgrade_speed.width / 2 - 50,upgrade_speed.y + upgrade_speed.height / 2 + 20))

                
                
        if ab == 1:
            text_surface12 = myfont1.render("Bought", True, (0,0,0))
            window.blit(text_surface12, (upgrade_speed.x + upgrade_speed.width / 2 - 50,upgrade_speed.y + upgrade_speed.height / 2 + 20))

        if write_gold >= 500:
            if s == 0:
                if p1.speed == 0.0015:
                    if button_colision(upgrade_speed2.width,upgrade_speed2.height,upgrade_speed2.x,upgrade_speed2.y,mousePos,mouseState):
                        p1.speed = 0.0020
                        write_gold -= 500
                        s = 1
                        
        else: 
            if s != 1:          
                text_surface263 = myfont1.render("Not enough gold", True, (0,0,0))
                window.blit(text_surface263, (upgrade_speed2.x + upgrade_speed2.width / 2 - 50,upgrade_speed2.y + upgrade_speed2.height / 2 + 20))

        
                
        if s == 1:
            text_surface12 = myfont1.render("Bought", True, (0,0,0))
            window.blit(text_surface12, (upgrade_speed2.x + upgrade_speed2.width / 2 - 50,upgrade_speed2.y + upgrade_speed2.height / 2 + 20))

        

        
    if main_menu == 0:
        if keys[pygame.K_ESCAPE]:
            game = 0
            main_menu = 1
            shop_inside = 0
            was_holding = True
    if main_menu == 1:
        if keys[pygame.K_ESCAPE]:
            if was_holding == False:
                0
                read(write_gold)
                exit()
        else:
            was_holding = False
    if game == 1:
        main_menu = 0
        shop_inside = 0
        
        ball.move()
        p1.move(keys)
        
        for laser in l_lasers:
            if laser.active == 1:
                laser.move()
                laser.draw(window)
                
        if keys[pygame.K_SPACE]:
            if cool <= 0:
                laser = Laser(p1.x,p1.y + 15,5,p1.dx,p1.dy,0.0013,1)
                l_lasers.append(laser)
                cool = 800
                es = 1
        
        if d <= 0:
            if collison(p1.x,p1.y,p1.height,ball.x,ball.y,ball.rad):
                p1.gold += 5
                d = 900
        p1.draw(window)
        ball.draw(window)
        d -= 1
        cool -= 1
        
        clock.tick(850)
    text.draw(p1.angle,game,p1.y,p1.gold,button,text,shop,shop_inside)
    pygame.display.update()