import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import all_func



wing_vertices = (
    (-6, 1, 0),
    (-6 , -1, 0),
    (6, -1, 0),
    (6, 1, 0)
    )

wing_edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0)
    )    

  
	
def Myobj():

    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    for edge in wing_edges:
        for vertex in edge:
            glVertex3fv(wing_vertices[vertex])
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    for edge in wing_edges:
        for vertex in edge:
            glVertex3fv(wing_vertices[vertex])
    glEnd()
    glPushMatrix()
    glTranslatef(6.0,0.0,0.0)    
    glRotatef(-45,0,1,0) # wind
    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0,1.0,0)
    glVertex3f(0.0,-1.0,0)
    glVertex3f(1.0,0.0,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.0,1.0,0)
    glVertex3f(0.0,-1.0,0)
    glVertex3f(1.0,0.0,0)
    glVertex3f(0.0,1.0,0)
    glEnd()
    glPopMatrix()
	
    glPushMatrix()
    glTranslatef(-6.0,0.0,0.0)    
    glRotatef(45,0,1,0) # wind
    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0,1.0,0)
    glVertex3f(0.0,-1.0,0)
    glVertex3f(-1.0,0.0,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.0,1.0,0)
    glVertex3f(0.0,-1.0,0)
    glVertex3f(-1.0,0.0,0)
    glVertex3f(0.0,1.0,0)
    glEnd()
    glPopMatrix()


    # a side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-1,3,0.5)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-1,-3,-0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-1,3,0.5)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-1,3,-0.5)
    glEnd()
	
    # b side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(1,3,-0.5)
    glVertex3f(1,3,0.5)
    glVertex3f(1,-3,0.5)
    glVertex3f(1,-3,-0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(1,3,-0.5)
    glVertex3f(1,3,0.5)
    glVertex3f(1,-3,0.5)
    glVertex3f(1,-3,-0.5)
    glVertex3f(1,3,-0.5)
    glEnd()
	
    # c side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,-1)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(0.5,-3,-1)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,-1)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(0.5,-3,-1)
    glVertex3f(0.5,3,-1)
    glEnd()
    
    # d side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,1)
    glVertex3f(-0.5,3,1)
    glVertex3f(-0.5,-3,1)
    glVertex3f(0.5,-3,1)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,1)
    glVertex3f(-0.5,3,1)
    glVertex3f(-0.5,-3,1)
    glVertex3f(0.5,-3,1)
    glVertex3f(0.5,3,1)
    glEnd()
    # ac side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-0.5,-3,-1)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(-0.5,3,-1)
    glEnd()	
    # cb side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,-1)
    glVertex3f(1,3,-0.5)
    glVertex3f(1,-3,-0.5)
    glVertex3f(0.5,-3,-1)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,-1)
    glVertex3f(1,3,-0.5)
    glVertex3f(1,-3,-0.5)
    glVertex3f(0.5,-3,-1)
    glVertex3f(0.5,3,-1)
    glEnd()
    # cb side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,3,1)
    glVertex3f(-1,3,0.5)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-0.5,-3,1)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5,3,1)
    glVertex3f(-1,3,0.5)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-0.5,-3,1)
    glVertex3f(-0.5,3,1)
    glEnd()	
    # db side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,1)
    glVertex3f(1,3,0.5)
    glVertex3f(1,-3,0.5)
    glVertex3f(0.5,-3,1)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,1)
    glVertex3f(1,3,0.5)
    glVertex3f(1,-3,0.5)
    glVertex3f(0.5,-3,1)
    glVertex3f(0.5,3,1)
    glEnd()	
 
    # body2
    # a1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-0.5,-7,0.25)
    glVertex3f(-0.5,-7,-0.25)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-0.5,-7,0.25)
    glVertex3f(-0.5,-7,-0.25)
    glVertex3f(-1,-3,-0.5)
    glEnd()
	
    # b1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(1,-3,-0.5)
    glVertex3f(1,-3,0.5)
    glVertex3f(0.5,-7,0.25)
    glVertex3f(0.5,-7,-0.25)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(1,-3,-0.5)
    glVertex3f(1,-3,0.5)
    glVertex3f(0.5,-7,0.25)
    glVertex3f(0.5,-7,-0.25)
    glVertex3f(1,-3,-0.5)
    glEnd()
	
    # c1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,-3,-1)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(-0.25,-7,-0.5)
    glVertex3f(0.25,-7,-0.5)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,-3,-1)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(-0.25,-7,-0.5)
    glVertex3f(0.25,-7,-0.5)
    glVertex3f(0.5,-3,-1)
    glEnd()
    
    # d1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,-3,1)
    glVertex3f(-0.5,-3,1)
    glVertex3f(-0.25,-7,0.5)
    glVertex3f(0.25,-7,0.5)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,-3,1)
    glVertex3f(-0.5,-3,1)
    glVertex3f(-0.25,-7,0.5)
    glVertex3f(0.25,-7,0.5)
    glVertex3f(0.5,-3,1)
    glEnd()
   # ac1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-0.5,-7,-0.25)
    glVertex3f(-0.25,-7,-0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5,-3,-1)
    glVertex3f(-1,-3,-0.5)
    glVertex3f(-0.5,-7,-0.25)
    glVertex3f(-0.25,-7,-0.5)
    glVertex3f(-0.5,-3,-1)
    glEnd()	
    # cb1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,-3,-1)
    glVertex3f(1,-3,-0.5)
    glVertex3f(0.5,-7,-0.25)
    glVertex3f(0.25,-7,-0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,-3,-1)
    glVertex3f(1,-3,-0.5)
    glVertex3f(0.5,-7,-0.25)
    glVertex3f(0.25,-7,-0.5)
    glVertex3f(0.5,-3,-1)
    glEnd()
    # cb1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,-3,1)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-0.5,-7,0.25)
    glVertex3f(-0.25,-7,0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5,-3,1)
    glVertex3f(-1,-3,0.5)
    glVertex3f(-0.5,-7,0.25)
    glVertex3f(-0.25,-7,0.5)
    glVertex3f(-0.5,-3,1)
    glEnd()	
    # db1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,-3,1)
    glVertex3f(1,-3,0.5)
    glVertex3f(0.5,-7,0.25)
    glVertex3f(0.25,-7,0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,-3,1)
    glVertex3f(1,-3,0.5)
    glVertex3f(0.5,-7,0.25)
    glVertex3f(0.25,-7,0.5)
    glVertex3f(0.5,-3,1)
    glEnd()	
 
    glColor3f(1, 0, 0) # back polygon
    glBegin(GL_POLYGON)
    glVertex3f(-0.5,-7,-0.25)
    glVertex3f(-0.25,-7,-0.5)
    glVertex3f(0.25,-7,-0.5)
    glVertex3f(0.5,-7,-0.25)
    glVertex3f(0.5,-7,0.25)
    glVertex3f(0.25,-7,0.5)
    glVertex3f(-0.25,-7,0.5)
    glVertex3f(-0.5,-7,0.25)
    glEnd()

    #### front side start
    # a front side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-1,3,0.5)
    glVertex3f(-0.5,4,0.25)
    glVertex3f(-0.5,4,-0.25)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-1,3,0.5)
    glVertex3f(-0.5,4,0.25)
    glVertex3f(-0.5,4,-0.25)
    glVertex3f(-1,3,-0.5)
    glEnd()
	
    # b1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(1,3,-0.5)
    glVertex3f(1,3,0.5)
    glVertex3f(0.5,4,0.25)
    glVertex3f(0.5,4,-0.25)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(1,3,-0.5)
    glVertex3f(1,3,0.5)
    glVertex3f(0.5,4,0.25)
    glVertex3f(0.5,4,-0.25)
    glVertex3f(1,3,-0.5)
    glEnd()
	
    # c1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,-1)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-0.25,4,-0.5)
    glVertex3f(0.25,4,-0.5)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,-1)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-0.25,4,-0.5)
    glVertex3f(0.25,4,-0.5)
    glVertex3f(0.5,3,-1)
    glEnd()
    
    # d1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,1)
    glVertex3f(-0.5,3,1)
    glVertex3f(-0.25,4,0.5)
    glVertex3f(0.25,4,0.5)
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,1)
    glVertex3f(-0.5,3,1)
    glVertex3f(-0.25,4,0.5)
    glVertex3f(0.25,4,0.5)
    glVertex3f(0.5,3,1)
    glEnd()
   # ac1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-0.5,4,-0.25)
    glVertex3f(-0.25,4,-0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5,3,-1)
    glVertex3f(-1,3,-0.5)
    glVertex3f(-0.5,4,-0.25)
    glVertex3f(-0.25,4,-0.5)
    glVertex3f(-0.5,3,-1)
    glEnd()	
    # cb1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,-1)
    glVertex3f(1,3,-0.5)
    glVertex3f(0.5,4,-0.25)
    glVertex3f(0.25,4,-0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,-1)
    glVertex3f(1,3,-0.5)
    glVertex3f(0.5,4,-0.25)
    glVertex3f(0.25,4,-0.5)
    glVertex3f(0.5,3,-1)
    glEnd()
    # cb1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,3,1)
    glVertex3f(-1,3,0.5)
    glVertex3f(-0.5,4,0.25)
    glVertex3f(-0.25,4,0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5,3,1)
    glVertex3f(-1,3,0.5)
    glVertex3f(-0.5,4,0.25)
    glVertex3f(-0.25,4,0.5)
    glVertex3f(-0.5,3,1)
    glEnd()	
    # db1 side
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(0.5,3,1)
    glVertex3f(1,3,0.5)
    glVertex3f(0.5,4,0.25)
    glVertex3f(0.25,4,0.5)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.5,3,1)
    glVertex3f(1,3,0.5)
    glVertex3f(0.5,4,0.25)
    glVertex3f(0.25,4,0.5)
    glVertex3f(0.5,3,1)
    glEnd()	
 
    glColor3f(0,0,1) # front polygon
    glBegin(GL_POLYGON)
    glVertex3f(-0.5,4,-0.25)
    glVertex3f(-0.25,4,-0.5)
    glVertex3f(0.25,4,-0.5)
    glVertex3f(0.5,4,-0.25)
    glVertex3f(0.5,4,0.25)
    glVertex3f(0.25,4,0.5)
    glVertex3f(-0.25,4,0.5)
    glVertex3f(-0.5,4,0.25)
    glEnd()
	
 
    #### front side end
    #### back triangles start
    glColor3f(0,0,1) # red side back triangles
    glBegin(GL_TRIANGLES)
    glVertex3f(0,-4,0)
    glVertex3f(3,-6.5,0)
    glVertex3f(0,-6.5,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0,-4,0)
    glVertex3f(3,-6.5,0)
    glVertex3f(0,-6.5,0)
    glVertex3f(0,-4,0)
    glEnd()
    
    glColor3f(0,0,1) # left side back triangles
    glBegin(GL_TRIANGLES)
    glVertex3f(0,-4,0)
    glVertex3f(-3,-6.5,0)
    glVertex3f(0,-6.5,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0,-4,0)
    glVertex3f(-3,-6.5,0)
    glVertex3f(0,-6.5,0)
    glVertex3f(0,-4,0)
    glEnd()
    
    glColor3f(0,0,1) # vertical back triangles
    glBegin(GL_TRIANGLES)
    glVertex3f(0,-4,0)
    glVertex3f(0,-6.5,3)
    glVertex3f(0,-6.5,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0,-4,0)
    glVertex3f(0,-6.5,3)
    glVertex3f(0,-6.5,0)
    glVertex3f(0,-4,0)
    glEnd()

	###  wind back triangle right
    glColor3f(0,0,1) # left side back triangles
    glBegin(GL_TRIANGLES)
    glVertex3f(1,-1,0)  
    glVertex3f(1,-1.5,0)
    glVertex3f(6,-1,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(1,-1,0)
    glVertex3f(1,-1.5,0)
    glVertex3f(6,-1,0)
    glVertex3f(1,-1,0)
    glEnd()
	###  wind back triangle left
    glColor3f(0,0,1) # left side back triangles
    glBegin(GL_TRIANGLES)
    glVertex3f(-1,-1,0)  
    glVertex3f(-1,-1.5,0)
    glVertex3f(-6,-1,0)
    glEnd()
    glLineWidth(1)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,-1.5,0)
    glVertex3f(-6,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
	
	#### back triangles end
 
    glColor3f(0.4,0.6,0.9) 
    all_func.circle_plane(3,0,0.8,30,0.15) # x,y,radius,number_of_triangle,z
    all_func.circle_plane(-3,0,0.8,30,0.15) # x,y,radius,number_of_triangle,z
	
