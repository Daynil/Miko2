#-------------------------------------------------------------------------------
# Name:        Settings
# Purpose:     Consolidate Settings
#
# Author:      Danny
#
# Created:     04/07/2013
# Copyright:   (c) Danny 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SWIDTH = 700
SHEIGHT = 500
PSPEED = 4
FPS = 30
mikospeed = 4 # pixels per frame for proportionate ~30 mph
mikosize = (70, 60) # miko's width and height
mikowid = mikosize[0]
mikoht = mikosize[1]
ratsize = (70, 60)
ratwid = ratsize[0]
ratht = ratsize[1]

# Create all objects relative to game origin
GAMEORIGIN = (0, 0)



clock = pygame.time.Clock()

def terminate():
    pygame.quit()
    sys.exit()

class Texting():
    def __init__(self, fontface, size):
        self.fontface = fontface
        self.size = size
        self.font = pygame.font.Font(fontface, size)
    def drawText(self, color, x, y, content):
        screen.blit(self.font.render(content, True, color), [x, y])

score_font = Texting(None, 50)

def waitForPress():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()