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

sprite_img = pygame.image.load('231007 - Filip top down car1.png')
window = pygame.display.set_mode((WIDTH,HEIGHT))

class Player:
    def __init__(self,x,y,dx,dy,height,speed,gold,angle):
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
        ddx = 0
        ddy = 0
        
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
        
        if self.angle < 0:
            self.angle = self.angle + 360
            
        if self.angle > 360:
            self.angle = self.angle - 360
        
        if self.angle < 22.5 or self.angle > 337.5:
            ddx = 0
            ddy = -1
                
        if self.angle > 22.5 and self.angle <= 67.5:
            ddx = -0.7
            ddy = -0.7
            
        if self.angle > 67.5 and self.angle <= 112.5:
            ddx = -1
            ddy = 0
            
        if self.angle > 112.5 and self.angle <= 157.5:
            ddx = -0.7
            ddy = 0.7
                
        if self.angle > 157.5 and self.angle <= 202.5:
            ddx = 0
            ddy = 1
            
        #225 angle       
        if self.angle > 202.5 and self.angle <= 247.5:
            ddx = 0.7
            ddy = 0.7
            
        #270
        if self.angle > 247.5 and self.angle <= 292.5:
            ddx = 1
            ddy = 0
            
                
        if self.angle > 292.5 and self.angle <= 337.5:
            ddx = 0.7
            ddy = -0.7
                
        acceleration = 0
        if self.x > 0 and self.x < 800 and self.y > 0 and self.y < 800:
            if keys[pygame.K_w]:
                acceleration = 0.0008
                
                
        if self.x > 0 and self.x < 800 and self.y > 0 and self.y < 800:
            if keys[pygame.K_s]:
                acceleration = -0.0008
        
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
        self.my_font = pygame.font.SysFont('Comic Sans MS', 70)
    def draw(self,window,player):
        pygame.draw.rect(window, pygame.Color("Black"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        text_surface = self.my_font.render(f"Play", True, (255,255,255))
        window.blit(text_surface, (self.x + self.width / 2 - 65,self.y + self.height / 2 - 65))
        text_surface = self.my_font.render(f"Main Menu", True, (255,0,0))
        window.blit(text_surface, (self.x + self.width / 2 - 135,self.y + self.height / 2 - 325))


class Debug_mode:
    def __init__(self,window):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
        self.myfont1 = pygame.font.SysFont('Comic Sans MS', 20)
        self.window = window
    def draw(self,angle,game,y,gold):
        text_surface = self.myfont1.render(f"Player angle {int(angle)}", True, (0, 0, 0))
        text_surface2 = self.myfont1.render(f"Player y {int(y)}", True, (0, 0, 0))
        text_surface3 = self.myfont1.render(f"Player gold {int(p1.gold)}", True, (0, 0, 0))

        self.window.blit(text_surface3, (0,100))
        self.window.blit(text_surface2, (0,50))
        self.window.blit(text_surface, (0,0))

p1 = Player(300,300,0,0,sprite_img.get_height()*0.15,0.1,0,0)
ball = Bouncing_Ball(300,300,1,1,0,0.002,75,75,0.06)
button = Button(250,300,300,150)
text = Debug_mode(window)
#if collison(p1.x,p1.y,p1.size,ball.x,ball.y,ball.size)

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False


prev = 0

#f = open("test.txt", "r")
#contents = f.read()
#lines = contents.split("\n")
#f.close()


d = 0
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
        text.draw(p1.angle,game,p1.y,p1.gold)
        ball.move()
        p1.move(keys)
        
        if d <= 0:
            if collison(p1.x,p1.y,p1.height,ball.x,ball.y,ball.rad):
                p1.gold = p1.gold + 5
                d = 900
        p1.draw(window)
        ball.draw(window)
        if p1.gold >= 100:
            if keys[pygame.K_c]:
                prev = 1
                
        if p1.gold >= 10000000:
            exit()
            
        d -= 1
    pygame.display.update()