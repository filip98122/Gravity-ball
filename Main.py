import pygame
import math

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

my_font = pygame.font.SysFont('Comic Sans MS', 70)
window = pygame.display.set_mode((WIDTH,HEIGHT))

class Player:
    def __init__(self,x,y,dx,dy,speed,gold):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = 0.001
        self.ddy = 0.001
        self.maxdy = 2.5
        self.maxdx = 2.5
        self.speed = speed
        self.size = 35
        self.sprite_img = pygame.image.load('231007 - Filip top down car.png')
        self.width = self.sprite_img.get_width()*0.5
        self.height = self.sprite_img.get_height()*0.5
        self.scaled_img = pygame.transform.scale(self.sprite_img, (self.width, self.height))
        self.gold = gold
    
    def draw(self, window):
        window.blit(self.scaled_img, (self.x, self.y))
        
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
        
        if self.maxdx < self.dx:
            self.dx = self.maxdx
        if self.maxdy < self.dy:
            self.dy = self.maxdy


        if keys[pygame.K_w]:
            self.dy -= self.ddy
        elif keys[pygame.K_s]:
            self.dy += self.ddy
            
        elif self.dy > 0:
            self.dy -= self.ddy
        
        if keys[pygame.K_a]:
            self.dx -= self.ddx
        elif keys[pygame.K_d]:
            self.dx += self.ddx
        
        elif self.dx > 0:
            self.dx -= self.ddx
        
        newX = self.x + self.dx*self.speed
        newY = self.y + self.dy*self.speed
        
        if newX < WIDTH-(self.width+9) and newX > 10:
            self.x += self.dx*self.speed
        else:
            self.dx = 0
        if newY < HEIGHT-self.height+1 and newY > 0:
            self.y += self.dy*self.speed
        else:
            self.dy = 0
        
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
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self,window,player):
        pygame.draw.rect(window, pygame.Color("Black"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        text_surface = my_font.render(f"Play", True, (255,255,255))
        window.blit(text_surface, (self.x + self.width / 2 - 65,self.y + self.height / 2 - 65))
        text_surface = my_font.render(f"Main Menu", True, (255,0,0))
        window.blit(text_surface, (self.x + self.width / 2 - 135,self.y + self.height / 2 - 325))


p1 = Player(300,300,0,0,0.1,0)
ball = Bouncing_Ball(300,300,1,1,0,0.002,75,75,0.06)
button = Button(250,300,300,150)

#if collison(p1.x,p1.y,p1.size,ball.x,ball.y,ball.size)

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

def debugMode(window,gold):
    text_surface = my_font.render(f"Player Gold {int(gold)}", True, (0, 0, 0))
    window.blit(text_surface, (0,0))
    text_surface = my_font.render(f"10 000 000 gold to win!", True, (0, 0, 0))
    window.blit(text_surface, (0,100))
    text_surface = my_font.render(f"Have fun and grind!", True, (0, 0, 0))
    window.blit(text_surface, (0,175))
prev = 0
game = 0
while True:
    window.fill("White")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if game != 1:
        button.draw(window,p1)
        
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    
    if button_colision(button.width,button.height,button.x,button.y,mousePos,mouseState):
        game = 1
    if keys[pygame.K_ESCAPE]:
        exit()
    
    if game == 1:
        ball.move()
        p1.move(keys)
        
        
        p1.draw(window)
        ball.draw(window)
        if prev == 0:
            if game == 1:
                p1.gold += 0.0005
        if p1.gold >= 100:
            if keys[pygame.K_c]:
                prev = 1
        
        if prev == 1:
            if game == 1:
                p1.gold += 0.001
                
        if p1.gold >= 10000000:
            exit()
            
            
    pygame.display.update()