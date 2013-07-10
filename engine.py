#-------------------------------------------------------------------------------
# Name:        Game Engine
# Purpose:     Starts up screen, handles events
#
# Author:      Danny
#
# Created:     06/07/2013
# Copyright:   (c) Danny 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
from playerclass import *
from settings import *


# Draw background and all sprites to screen
# Background comes first to wipe the previous frame

# Detect and process events
def eventProcessor(char):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                char.changespeed(-1*mikospeed, 0)
            if event.key == K_RIGHT or event.key == ord('d'):
                char.changespeed(mikospeed, 0)
            if event.key == K_UP or event.key == ord('w'):
                char.changespeed(0, -1*mikospeed)
            if event.key == K_DOWN or event.key == ord('s'):
                char.changespeed(0, mikospeed)

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                char.changespeed(mikospeed, 0)
            if event.key == K_RIGHT or event.key == ord('d'):
                char.changespeed(-1*mikospeed, 0)
            if event.key == K_UP or event.key == ord('w'):
                char.changespeed(0, mikospeed)
            if event.key == K_DOWN or event.key == ord('s'):
                char.changespeed(0, -1*mikospeed)
            if event.key == K_ESCAPE:
                terminate()


'''
To Do:

    Implement camera screen and movement with 'slack' of 1/4-1/2 SWIDTH

    Figure out how to create pixel art for games where there is no background
    (like a program for it?) and figure out how to animate images

Ideas:

    Cats run at full speed at a 'gallop' where they leap between steps,
    so miko will run by hopping. You can only jump if he is not mid-hop.

    Miko can kill enemies by scratching them - draw a frame where he
    extends his paw and has a 'slash' image in front of him and if an
    enemy is in range, it dies.



'''