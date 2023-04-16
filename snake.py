import pygame
import sys
from pygame.locals import QUIT,KEYDOWN,K_RIGHT,K_LEFT,K_DOWN,K_UP,K_SPACE,K_ESCAPE
import random
xm,ym=0,0
sx,sy=250,250
screen=0
clock=pygame.time.Clock()
FPS=5
randx=(int(random.randrange(0,500))*10)%500
randy=(int(random.randrange(0,500))*10)%500
slen=1
body = [(sx, sy)]



def quit():
    pygame.quit()
    sys.exit(0)


def game(events):
    global screen,sx,sy,randx,randy,slen,xm,ym,FPS,score,body
    if sx<0 or sx>500 or sy<0 or sy>500:
                    screen.fill((0,0,0))
                    style=pygame.font.SysFont(None,40,True)
                    style1=pygame.font.SysFont(None,15,True)
                    txt=style.render(" score : "+str(FPS*slen),True,(240,120,60))
                    txtr=style1.render("press space to restart ".title(),True,(60,120,240))
                    screen.blit(txt,(170,200))
                    screen.blit(txtr,(180,250))
                    pygame.display.flip()   
                    pygame.display.update()
                    return 0
    for event in events:
            print((sx,sy),(randx,randy))
            # screen.fill((255,255,255))
            # pygame.display.update()
            if event.type==QUIT:
                quit()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    xm=10
                    ym=0
                    # sx=sx+10
                elif event.key==K_LEFT:
                    xm=-10
                    ym=0
                    # sx=sx-10
                elif event.key==K_DOWN:
                    xm=0
                    ym=10
                    # sy=sy+10
                elif event.key==K_UP:
                    xm=0
                    ym=-10
                    # sy=sy-10
    sx=sx+xm
    sy=sy+ym
    body.insert(0, (sx, sy))
    if len(body) > slen:
        body.pop()
   
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,100,150),(randx,randy,10,10))
    if (sx==randx and sy==randy):
                    slen=slen+1
                    FPS=FPS+1
                    randx=(int(random.randrange(0,500))*10)%500
                    randy=(int(random.randrange(0,500))*10)%500
    for x,y in body:
        pygame.draw.rect(screen,(0,0,0),(x,y,10,10))
    pygame.display.update()
    clock.tick(FPS)
        
def restart_game():
    global sx, sy, randx, randy, slen, xm, ym, FPS,body
    sx, sy = 250, 250
    randx = (int(random.randrange(0, 500)) * 10) % 500
    randy = (int(random.randrange(0, 500)) * 10) % 500
    slen = 1
    xm, ym = 0, 0
    FPS = 5
    body = [(250, 250)]

def main():
    global screen,ran
    pygame.init()
    window=pygame.display.set_mode((500,500))
    pygame.display.set_caption('snake game') 
    screen=pygame.display.get_surface()
    pygame.display.update()
    rtn=None
    while True:
        rtn=game(pygame.event.get())
        if rtn!=None:
            for event in pygame.event.get():
                print(event)
                if event.type==QUIT:
                    quit()
                elif event.type==KEYDOWN:
                    if event.key==K_SPACE:
                          restart_game()
                    elif event.key==K_ESCAPE:
                          quit()
              

main()

