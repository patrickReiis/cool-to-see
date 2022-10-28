import pygame, sys, random, copy
from pygame.locals import *


FPSCLOCK = pygame.time.Clock()
FPS = 80
WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
BLACK = (0,0,0)
GREEN = (48, 200,113)
PURPLE = (198,76,190)
WHITE = (255,255,255)
ORANGE = (255,165,0)

def main():
    locations = []
    circle = []
    sub_circle = []
    cratio = 1
    width = 160
    counter =1
    options = True

    color = WHITE


    print("Press 'W' for WHITE.\nPress 'P' for PURPLE.\nPress 'G' for GREEN.\nPress 'O' for ORANGE.")

    while True:

        DISPLAYSURF.fill(BLACK)
        checkForQuit()

        for event in pygame.event.get(): # event queue gets full if click with 2 buttons
              if event.type == KEYUP:
                  if event.key == K_g:
                      color = GREEN
                  if event.key == K_p:
                      color = PURPLE
                  if event.key == K_w:
                      color = WHITE
                  if event.key == K_o:
                      color = ORANGE

        if pygame.mouse.get_pressed()[0] == True:
            location = pygame.mouse.get_pos()
            locations.append(location)

        for location in locations:
            
            if len(locations) == counter:
                sub_circle.append(cratio)
                sub_circle.append(width)

                circle.append(sub_circle)
                sub_circle = []
                counter+= 1

        for i in range(len(circle)):
            circle[i][0] += 1 # 0 stands for the radius of the circle
            circle[i][1] -= 1 # 1 stands for the width of the circle
            if circle[i][1] < 0:
                circle[i][1] = 0 # messy system with the purpose to save memory. If width is less than 0 than set it to 0 so it doesn't update all the time even if it was already drew. A better system would be to reset the circle variable once it was drew but I'm too lazy for that. I will focus on another project maybe on the future I fix this 

        for i in range(len(circle)):
            draw_epic_circle(locations[i],circle[i][0],circle[i][1], color)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def draw_epic_circle(location,cratio,width,color):

    if width != 0: # in pygame if the width is 0 it fill the circle which gives an ugly effect for this project 

        pygame.draw.circle(DISPLAYSURF,color,location,cratio,width)



def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
        
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back
        
    for event in pygame.event.get(KEYUP):
        if event.key == K_LCTRL and event.key == K_w: # it ain't working
            terminate()
        pygame.event.post(event)

if __name__ == '__main__':
    main()
