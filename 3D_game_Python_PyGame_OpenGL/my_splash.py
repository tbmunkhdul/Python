import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import all_func
import my_plane_splash



def printtext(x,y,text):
    glLineWidth(2)
    glColor3f(0, 0, 0)
    lengthtext = 0
    textlist = []
    xcordinate = 0
    lengthtext = len(text)
    textlist = list(text)
    xcordinate = x  
    for i in range(0,lengthtext):
        glRasterPos2f (xcordinate,y)
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15,ord(textlist[i]))
        xcordinate += 0.6


def mytriangles():
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex3f(3,-13,0)
    glVertex3f(4,-13,0)
    glVertex3f(3.5,-14,0)
    glEnd()

def mytrianglesleft():
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-3,-13,0)
    glVertex3f(-4,-13,0)
    glVertex3f(-3.5,-14,0)
    glEnd()


angle = 0
state = True


#state = False
def splash_running():
    global angle
    global state

    xrot = 3
    yrot = 1
    zrot = 1

    keyboard = "right"
    keyboard2 = "none"    



    while state:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                    keyboard = "left"
              if event.key == pygame.K_RIGHT:
                    keyboard = "right"
              if event.key == pygame.K_DOWN:
                    #state = False
                    keyboard2 = "down"
                  

        glClearColor (1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
        printtext(-20,+15,'PyOpenGL and PyGame and Python')
        printtext(10,+5,'LEFT keyboard -> turn left')
        printtext(10,+3,'RIGHT keyboard -> turn right')
        printtext(10,+1,'R keyboard -> fire')
        printtext(10,-1,'Q keyboard -> turn pitch to left')
        printtext(10,-3,'W keyboard -> turn pitch to right')
        printtext(10,-5,'Windows close -> quit game')
        printtext(-5,-15,'start')
        printtext(2.3,-15,'quit')

        if keyboard == "left":
            mytrianglesleft()
        if keyboard == "right":
            mytriangles()
        if keyboard2 == "down":
            if keyboard == "left":
                state = False
            if keyboard == "right":
                pygame.quit()
                quit()
        
        keyboard2 = ""    

        if angle == 720:
            if xrot == 3:
                yrot = 3
                xrot = 1
                zrot = 1
                angle = 0

        if angle == 720:
            if yrot == 3:
                zrot = 3
                yrot = 1
                xrot = 1
                angle = 0

        if angle == 720:
            if zrot == 3:
                xrot = 3
                yrot = 1
                zrot = 1
                angle = 0

        glPushMatrix()
        glRotatef(angle, xrot, yrot, zrot)
        my_plane_splash.Myobj()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
        angle += 1	
