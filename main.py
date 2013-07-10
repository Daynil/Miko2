#-------------------------------------------------------------------------------
# Name:        Miko 2.0
# Purpose:     Main game file
#sssss
# Author:      Danny
#
# Created:     04/07/2013
# Copyright:   (c) Danny 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, pygame
from pygame.locals import *
from settings import *
from playerclass import *
from engine import *

# start up the game
pygame.init()

screen = pygame.display.set_mode([SWIDTH, SHEIGHT])
pygame.display.set_caption("Miko 2.0")
bgimage = pygame.image.load('mikobg.png').convert()

# Create miko at center of screen at game origin
miko = Player((SWIDTH//2 - (mikowid/2)), (SHEIGHT-mikoht))

# Create rat off screen by 1/2 screen width
ratA = Rat((700-ratwid), SHEIGHT-60)
camx = 0


# Create sprites list and players/enemies

# Create main game loop
def main():
    global camx
    global screen
    while True:
        # Detect and process events
        eventProcessor(miko)

        # Game Mechanics
        camxstart = camx
        camxchange = 0
        # Adjust camera based on player position
        playercenterx = (miko.x + (mikowid//2))
        camx = playercenterx - (SWIDTH//2)
        camxchange = camx - camxstart

        # Draw everything and flip screen
        miko.update()
        #ratA.update()
        screen.blit(bgimage, [0, 0])
        mikoRect = pygame.Rect(miko.x - camx, miko.y, mikowid, mikoht)
        ratARect = pygame.Rect(ratA.x - camx, ratA.y, ratwid, ratht)
        screen.blit(miko.image, mikoRect)
        screen.blit(ratA.image, ratARect)

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main()
