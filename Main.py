

#first lets call the modules we will need for the example

#pygame is the light wait framework to handle events
import pygame as py
#random has a but load of function and uses
#import random as r
#we will save any data with numphy.  its very easy once you work it out
#import numphy as ny

#my own list of functions.
#from fools import *

#if you dont initilize py game in the begining.  it just doesnt work lol
py.init()

py.font.init()


#this is really just a grid but since cell phone pygame
#scripts  ingnore phone size and input of disired
# screen size,  to stop shit gettin all muddled up
#we need a way to make a game with out using the standered
#pixels.  also..  as im making this now on no sleep after
# a bitch of a day... let me say.  know fucking idea if
#any of this will work
class UltimatePos:
    #add the standered fooliery sytle g
    #depth will be how the game coops with the size modulation
    #it will also take a turple for the width and height
    def __init__(self,g,depth):
        #lets get the screen size in a turple of (width and height)
        self.w = g.screen.get_size()
        print(str(self.w) + ' self.w')
        #need 2 list to hold the values
        self.x = []
        self.y = []
        #and some temporary vars to use in our forLoops
        xpos = 0
        ypos = 0
        for i in range(depth[0]):
            self.x.append(xpos)
            print(str(self.w[0]) + 'ffff')
            qqx = int(self.w[0])
            p = (qqx//depth[0])
            xpos += p
        for i in range(depth[1]):
            self.y.append(ypos)
            qqy  = int(self.w[1])
            ypos += (qqy//depth[1])
            #now we need a way to acess thees and return the acuall xy pos we need
    def Pos(self,xy):
        return (self.x[xy[0]] , self.y[xy[1]])




def showText(text,xy  ,size ,color, screen):

    font = py.font.SysFont(None, size)
    img = font.render(text, True, color)
    screen.blit(img, xy)





class Game:
    def __init__(self):
        self.screen = py.display.set_mode((500,500))
        self.zed = UltimatePos(self,[50,50])
        #py.set_captian('Hey man check this out')
        self.KeepRunning = True
        self.time = py.time.Clock()


        self.BasicOFallEXAMPLESofGAMEtime = 0

        self.ticker = 0

        self.counter = 0

        self.myx = 25
        self.myy = 25


    def DoThisFirstOnlyOnce(self):
        print('working just fine boss')


    def Run(self):

        self.DoThisFirstOnlyOnce()

        while self.KeepRunning:
            self.time.tick(60)
            self.Events()
            self.Update()
            self.Draw()

    def Update(self):

        self.ticker += 1
        if self.ticker > 60:
            self.counter += 1
            self.ticker = 0
            print('Were just counting the seconds - ' + str(self.counter))

    def Draw(self):
        self.screen.fill((0,0,255))
        zx = self.zed.Pos((self.myx,self.myy))
        showText('did  ;) - ' + str(self.counter) , zx,25,(0,0,0),self.screen)

        py.display.flip()


    def Events(self):
        for e in py.event.get():
            if e.type == py.QUIT:
                py.quit()
            if e.type == py.MOUSEBUTTONDOWN:
                self.myy += 1
            if e.type == py.MOUSEBUTTONUP:
                self.myy -= 1




g = Game()
g.Run()
