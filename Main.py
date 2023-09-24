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

window = pygame.display.set_mode((WIDTH,HEIGHT))

class Player:
    def __init__(self,x,y,dx,dy,speed):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = 0.001
        self.ddy = 0.001
        self.maxdy = 2.5
        self.maxdx = 2.5
        self.speed = speed
        self.size = 75
    def draw(self,window):
        pygame.draw.circle(window,pygame.Color("Red"),(self.x,self.y),self.size)
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
        
        if newX < WIDTH-self.size and newX > self.size:
            self.x += self.dx*self.speed
        else:
            self.maxdx = 0
        if newY < HEIGHT-self.size and newY > self.size:
            self.y += self.dy*self.speed
        else:
            self.maxdy = 0
        
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
p1 = Player(300,300,0,0,0.3)
ball = Bouncing_Ball(300,300,1,1,0,0.002,75,75,0.1)
while True:
    window.fill("White")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    #if collison(p1.x,p1.y,p1.size,ball.x,ball.y,ball.size):
        
    if keys[pygame.K_ESCAPE]:
        exit()
    
    ball.move()
    p1.move(keys)
    
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()    
    
    p1.draw(window)
    ball.draw(window)
    
    pygame.display.update()