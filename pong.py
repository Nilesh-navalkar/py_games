import pygame
import sys
import random
from pygame.locals import QUIT,KEYDOWN,K_RIGHT,K_LEFT

screen=0
x,y=0,200
xm=0
FPS=80
bounce=0
bx=int(random.randrange(50,450))
by=int(random.randrange(50,450))
clock=pygame.time.Clock()
cclock=pygame.time.Clock()
cFPS=65
delbx,delby=1,1
def quit():
    pygame.quit()
    sys.exit(0)

def restart_game():
    global screen,x,y,xm,bounce,bx,by,FPS,delby,delbx,cclock,cFPS
    x,y=0,200
    xm=0
    FPS=50
    bounce=0
    bx=int(random.randrange(50,450))
    by=int(random.randrange(50,450))
    clock=pygame.time.Clock()
    delbx,delby=1,1
    cclock=pygame.time.Clock()
    cFPS=65

def game(events):
    global screen,x,y,xm,bounce,bx,by,FPS,delby,delbx,cclock,cFPS
    for event in  events:
        if event.type==QUIT:
            quit()
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT:
                if x<456:
                    xm=5
            elif event.key==K_LEFT:
                if x>4:
                    xm=-5
    if x+xm<0 or x+xm>500-y:
        xm=-xm
    cclock.tick(cFPS)
    x=x+xm
    if bounce==3:
        bounce=0
        if y>40:
           y=y-40
        FPS=FPS+20
    clock.tick(FPS)
    bx=bx+delbx
    by=by+delby
    if bx<5:
        bx=5
        delbx=-1*delbx
    elif bx>495:
        bx=495
        delbx=-1*delbx
    if by<5:
        by=5
        delby=-1*delby
    elif by>490:
        by=495
        delby=-1*delby
    if by==485 and bx>=x and bx<=x+y:
        delby=-1*delby
        bounce=bounce+1
    if by>485:
        restart_game()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(60,240,120),(bx,by),5)
    pygame.draw.rect(screen,(255,0,0),(x,490,y,10))
    pygame.display.update()
    clock.tick(FPS)

def main():
    global screen
    pygame.init()
    window=pygame.display.set_mode((500,500))
    pygame.display.set_caption('learn')
    screen=pygame.display.get_surface()
    pygame.display.update()
    while True:
        game(pygame.event.get())

main()