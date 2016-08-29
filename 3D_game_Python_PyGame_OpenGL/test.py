import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
import pygame , pygame.image
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def ground():
    glColor3f(0.5, 1.0, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-20,-20,0)
    glVertex3f(-20,20,0)
    glVertex3f(20,20,0)
    glVertex3f(20,-20,0)
    glEnd()

    glLineWidth(2)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-20,-20,0)
    glVertex3f(-20,20,0)
    glVertex3f(20,20,0)
    glVertex3f(20,-20,0)
    glVertex3f(-20,-20,0)
    glEnd()


def plane():
    glColor3f(0.5, 0.5, 1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-2,-2,5)
    glVertex3f(0,2,5)
    glVertex3f(2,-2,5)
    glEnd()

    glLineWidth(2)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-2,-2,5)
    glVertex3f(0,2,5)
    glVertex3f(2,-2,5)
    glVertex3f(-2,-2,5)
    glEnd()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_ALPHA )
    glutInitWindowSize(1024, 650)
    glutInitWindowPosition(50,50)    
    pygame.init()

    display = (1024,650) # 1024,768
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90,(display[0]/display[1]),0.1,1500.0)
    glViewport(0,0,display[0],display[1])
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt(0, 0, 100, 0, 0, 0, 0, 1, 0) # on top nice viewing
    gluLookAt(0, -30, 10, 0, 0, 0, 0, 1, 0) # nice viewing
              


    rotation = 0
    keyboard = ""
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:
                    keyboard = "up"
              if event.key == pygame.K_DOWN:
                    keyboard = "down"

        glClearColor (1.0, 1.0, 1.0, 1.0);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)



        if keyboard == "up":
            rotation = 1
            glRotatef(1,1,0,0)
        if keyboard == "down":
            rotation = -1
            glRotatef(-1,1,0,0) 

        keyboard = "" 

        ground()
        plane()


        pygame.display.flip()
        pygame.time.wait(10)


main()