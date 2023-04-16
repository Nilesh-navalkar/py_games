import pygame
import os
import sys
from pygame.locals import QUIT,KEYDOWN,K_RIGHT,K_LEFT
screen=0
x,y=0,0
def quit():
    pygame.quit()
    sys.exit(0)

def game(events):
    global screen,x,y
    for event in  events:
        if event.type==QUIT:
            quit()
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT:
                if x<456:
                    x=x+5
            elif event.key==K_LEFT:
                if x>4:
                    x=x-5
        else:
            print(event)
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(255,0,0),(x,0,50,10))
        pygame.display.update()

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

