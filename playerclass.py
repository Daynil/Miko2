#-------------------------------------------------------------------------------
# Name:        Sprite classes
# Purpose:     All the sprites in game
#
# Author:      Danny
#
# Created:     04/07/2013
# Copyright:   (c) Danny 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
from settings import *

pygame.init()

# Determines of object item is off the screen
#def isOffScreen(item):
    #if (item.rect.top < 0 or item.rect.bottom > SHEIGHT or item.rect.left < 0
        #or item.rect.right > SWIDTH):
        #return True

# Return object item to within bounds of screen if off screen
#def returnToScreen(item):
    #if isOffScreen(item):
        #if item.rect.top < 0: item.rect.top = 0
        #if item.rect.bottom > SHEIGHT: item.rect.bottom = SHEIGHT
        #if item.rect.left < 0: item.rect.left = 0
        #if item.rect.right > SWIDTH: item.rect.right = SWIDTH

# Cannot reference sprites_lists


class Player:
    ''' Our hero, Miko '''
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        self.image = pygame.image.load('miko.png').convert()
        self.image.set_colorkey(WHITE)
        self.x = x
        self.y = y

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        #returnToScreen(self)
        self.x += self.change_x
        self.y += self.change_y

class Rat:
    '''' The enemies -- Rats '''
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        self.image = pygame.image.load('rat.png').convert()
        self.image.set_colorkey(WHITE)
        self.x = x
        self.y = y

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # This function would be used to change the objects absolute position
    # like if the rat paces around like enemies tend to in platformers
    def update(self):
        self.x += self.change_x
        self.y += char.change_y



