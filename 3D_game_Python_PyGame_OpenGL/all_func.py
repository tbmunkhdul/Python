import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import all_func


def printtext(x,y,z,text):
    glLineWidth(2)
    glColor3f(0, 0, 0)
    lengthtext = 0
    textlist = []
    xcordinate = 0
    lengthtext = len(text)
    textlist = list(text)
    xcordinate = x  
    for i in range(0,lengthtext):
        glRasterPos3f (xcordinate,y,z)
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15,ord(textlist[i]))
        xcordinate += 0.8

def printtextwarning(x,y,z,text):
    glLineWidth(2)
    glColor3f(1, 0, 0)
    lengthtext = 0
    textlist = []
    xcordinate = 0
    lengthtext = len(text)
    textlist = list(text)
    xcordinate = x  
    for i in range(0,lengthtext):
        glRasterPos3f (xcordinate,y,z)
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15,ord(textlist[i]))
        xcordinate += 0.9

def printtextwarningnormal(x,y,z,text):
    glLineWidth(2)
    glColor3f(0, 0, 0)
    lengthtext = 0
    textlist = []
    xcordinate = 0
    lengthtext = len(text)
    textlist = list(text)
    xcordinate = x  
    for i in range(0,lengthtext):
        glRasterPos3f (xcordinate,y,z)
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15,ord(textlist[i]))
        xcordinate += 0.9

def printtextgoingdown(x,y,z,text):
    glLineWidth(2)
    glColor3f(0, 0, 0)
    lengthtext = 0
    textlist = []
    xcordinate = 0
    lengthtext = len(text)
    textlist = list(text)
    xcordinate = x  
    for i in range(0,lengthtext):
        glRasterPos3f (xcordinate,y,z)
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15,ord(textlist[i]))
        xcordinate += 0.8


def qrange(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0
    if step < 0:
        while start > stop:
            yield start   # makes this a generator for new start value
            start += step
    else:
        while start < stop:
            yield start
            start += step

def circle_plane(x, y, radius, number_of_triangles,z_degree):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, number_of_triangles):    
        angle = i * math.pi * 2.0 / number_of_triangles
        glVertex3f(x + radius * math.cos(angle), y + radius * math.sin(angle), z_degree )
    glEnd() 


