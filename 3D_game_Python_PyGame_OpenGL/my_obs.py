import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
import pygame , pygame.image
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import all_func
import my_plane
import my_splash
import random
import my_obs


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_ALPHA )
glutInitWindowSize(1024, 650)
glutInitWindowPosition(50,50)    
pygame.init()

display = (1024,650) # 1024,768
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)



     	
def grace(x,y):

    glColor3f(0,0.5,0) 
    glBegin(GL_TRIANGLES)
    glVertex3f(x-0.5,y,1500.5)
    glVertex3f(x,y,1503)
    glVertex3f(x+0.5,y,1500.5)
    glEnd()
    glColor3f(0,0.5,0) 
    glBegin(GL_TRIANGLES)
    glVertex3f(x+0.5,y,1500.5)
    glVertex3f(x+1,y,1502.5)
    glVertex3f(x+1.5,y,1500.5)
    glEnd()
    glColor3f(0,0.5,0) 
    glBegin(GL_TRIANGLES)
    glVertex3f(x-0.5,y,1500.5)
    glVertex3f(x-1,y,1501.5)
    glVertex3f(x-1.5,y,1500.5)
    glEnd()
    glLineWidth(2)
    #color red 0.36 green 0.25 blue 0.20
    glColor3f(0.36,0.25,0.20)     
    #glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex3f(x-1.5,y,1500.5)
    glVertex3f(x+1.5,y,1500.5)
    glEnd()



def treekk(x,y,image):
    # img = pygame.image.load('leaf.bmp')
    # textureData = pygame.image.tostring(img, "RGBA", 1)
    # width = img.get_width()
    # height = img.get_height()
    # im = glGenTextures(1)
    # glBindTexture(GL_TEXTURE_2D, im)
    # glTexEnvf (GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)    
    # glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    # glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
 

    glColor3f(0,0.5,0) # bottom

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x-3,y-2,1500)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1505)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1500)
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x+3,y-2,1500)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1505)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1500)
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x,y+2,1500)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1505)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1500)
    glEnd()

    glColor3f(0,0.5,0) # middle
    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x-5,y-3,1503)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1508)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1503)
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x+5,y-3,1503)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1508)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1503)
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x,y+3,1503)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1508)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1503)
    glEnd()

    glColor3f(0,0.5,0) # top
    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x-5,y-3,1507)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1516)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1507)
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x+5,y-3,1507)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1516)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1507)
    glEnd()

    glBegin(GL_TRIANGLES)
    glTexCoord3f (0,0,1501)   
    glVertex3f(x,y+3,1507)
    glTexCoord3f (1,1,1501)   
    glVertex3f(x,y,1516)
    glTexCoord3f (1,0,1501)   
    glVertex3f(x,y,1507)
    glEnd()



def obstacles1(x): 
    glColor3f(0,0,1)
    glBegin(GL_QUADS) # left front vertical
    glVertex3f(x-14,0,1500) 
    glVertex3f(x-14,0,1524) 
    glVertex3f(x-10,0,1524) 
    glVertex3f(x-10,0,1500) 
    glEnd()

    glColor3f(0,0,1)
    glBegin(GL_QUADS) # right front vertical
    glVertex3f(x+14,0,1500) 
    glVertex3f(x+14,0,1524) 
    glVertex3f(x+10,0,1524) 
    glVertex3f(x+10,0,1500) 
    glEnd()

    glColor3f(0,0,1)
    glBegin(GL_QUADS) # top back 
    glVertex3f(x-10,0,1520) 
    glVertex3f(x-10,0,1524) 
    glVertex3f(x+10,0,1524) 
    glVertex3f(x+10,0,1520) 
    glEnd()

    glLineWidth(2)
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x-14,0,1500)
    glVertex3f(x-14,0,1524)
    glVertex3f(x+14,0,1524)
    glVertex3f(x+14,0,1500)
    glVertex3f(x+10,0,1500)
    glVertex3f(x+10,0,1520)
    glVertex3f(x-10,0,1520)
    glVertex3f(x-10,0,1500)
    glVertex3f(x-14,0,1500)
    glEnd()

def obstacles2(x): 
    glColor3f(0,0,1)
    glBegin(GL_QUADS) # left front vertical
    glVertex3f(x-11,0,1500) 
    glVertex3f(x-11,0,1550) 
    glVertex3f(x-7,0,1550) 
    glVertex3f(x-7,0,1500) 
    glEnd()

    glColor3f(0,0,1)
    glBegin(GL_QUADS) # right front vertical
    glVertex3f(x+11,0,1500) 
    glVertex3f(x+11,0,1550) 
    glVertex3f(x+7,0,1550) 
    glVertex3f(x+7,0,1500) 
    glEnd()

    glColor3f(0,0,1)
    glBegin(GL_QUADS) # top back 
    glVertex3f(x-7,0,1546) 
    glVertex3f(x-7,0,1550) 
    glVertex3f(x+7,0,1550) 
    glVertex3f(x+7,0,1546) 
    glEnd()

    glLineWidth(2)
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x-11,0,1500)
    glVertex3f(x-11,0,1550)
    glVertex3f(x+11,0,1550)
    glVertex3f(x+11,0,1500)
    glVertex3f(x+7,0,1500)
    glVertex3f(x+7,0,1546)
    glVertex3f(x-7,0,1546)
    glVertex3f(x-7,0,1500)
    glVertex3f(x-11,0,1500)
    glEnd()



def obstacles3(x): # -100 ,  500, 
    glColor3f(0,0,1) 
    glBegin(GL_QUADS)
    glVertex3f(x-2,0,1500)
    glVertex3f(x-2,0,1520)
    glVertex3f(x+2,0,1520)
    glVertex3f(x+2,0,1500)
    glEnd()
    glLineWidth(2)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x-2,0,1500)
    glVertex3f(x-2,0,1520)
    glVertex3f(x+2,0,1520)
    glVertex3f(x+2,0,1500)
    glVertex3f(x-2,0,1500)
    glEnd()

    glColor3f(0,0,1) 
    glBegin(GL_QUADS) # left front vertical
    glVertex3f(x-14,0,1520) 
    glVertex3f(x-14,0,1540) 
    glVertex3f(x-10,0,1540) 
    glVertex3f(x-10,0,1520) 
    glEnd()

    glBegin(GL_QUADS) # right front vertical
    glVertex3f(x+14,0,1520) 
    glVertex3f(x+14,0,1540) 
    glVertex3f(x+10,0,1540) 
    glVertex3f(x+10,0,1520) 
    glEnd()

    glBegin(GL_QUADS) # top back 
    glVertex3f(x-10,0,1540) 
    glVertex3f(x-10,0,1536) 
    glVertex3f(x+10,0,1536) 
    glVertex3f(x+10,0,1540) 
    glEnd()

    glBegin(GL_QUADS) # bottom 
    glVertex3f(x-10,0,1520) 
    glVertex3f(x-10,0,1524) 
    glVertex3f(x+10,0,1524) 
    glVertex3f(x+10,0,1520) 
    glEnd()

    glLineWidth(2)
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x-14,0,1520)
    glVertex3f(x-14,0,1540)
    glVertex3f(x+14,0,1540)
    glVertex3f(x+14,0,1520)
    glVertex3f(x-14,0,1520)
    glEnd()

    glLineWidth(2)
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x-10,0,1524)
    glVertex3f(x-10,0,1540)
    glVertex3f(x+10,0,1540)
    glVertex3f(x+10,0,1524)
    glVertex3f(x-10,0,1524)
    glEnd()



####### shooting #########
def target(x): # -100 ,  500, 

    # img = pygame.image.load('target123.bmp')
    # textureData = pygame.image.tostring(img, "RGBA", 1)
    # width = img.get_width()
    # height = img.get_height()
    # im = glGenTextures(1)
    # glBindTexture(GL_TEXTURE_2D, im)
    # glTexEnvf (GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)    
    # glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    # glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)


    glColor3f(1,0,1) 
    glBegin(GL_QUADS)

 #   glTexCoord3f (0,0,1500)
    glVertex3f(x-5,0,1500)
    
#    glTexCoord3f (0,1,1500)
    glVertex3f(x-5,0,1520)

#    glTexCoord3f (1,1,1500)
    glVertex3f(x+5,0,1520)

#    glTexCoord3f (1,0,1500)
    glVertex3f(x+5,0,1500)

    glEnd()



###################

grace_list = []    
for i in range(0,5):
    grace_list.append(random.randrange(-149,149))
grace_list1 = []    
for i in range(0,5):
    grace_list1.append(random.randrange(-149,149))
grace_list2 = []    
for i in range(0,5):
    grace_list2.append(random.randrange(-149,149))
grace_list3 = []    
for i in range(0,5):
    grace_list3.append(random.randrange(-149,149))
grace_list4 = []    
for i in range(0,5):
    grace_list4.append(random.randrange(-149,149))
grace_list5 = []    
for i in range(0,5):
    grace_list5.append(random.randrange(-149,149))
grace_list6 = []    
for i in range(0,5):
    grace_list6.append(random.randrange(-149,149))
grace_list7 = []    
for i in range(0,5):
    grace_list7.append(random.randrange(-149,149))
grace_list8 = []    
for i in range(0,5):
    grace_list8.append(random.randrange(-149,149))
grace_list9 = []    
for i in range(0,5):
    grace_list9.append(random.randrange(-149,149))
grace_list10 = []    
for i in range(0,5):
    grace_list10.append(random.randrange(-149,149))
grace_list11 = []    
for i in range(0,5):
    grace_list11.append(random.randrange(-149,149))
grace_list12 = []    
for i in range(0,5):
    grace_list12.append(random.randrange(-149,149))
grace_list13 = []    
for i in range(0,5):
    grace_list13.append(random.randrange(-149,149))
grace_list14 = []    
for i in range(0,5):
    grace_list14.append(random.randrange(-149,149))




def mygracelist(z):
    if z == 0:
        y = -13
        for i in range(0,5):
            grace(grace_list[i],y)
            y += 5
    if z == 1:
        y = -13
        for i in range(0,5):
            grace(grace_list1[i],y)
            y += 5
    if z == 2:
        y = -13
        for i in range(0,5):
            grace(grace_list2[i],y)
            y += 5
    if z == 3:
        y = -13
        for i in range(0,5):
            grace(grace_list3[i],y)
            y += 5
    if z == 4:
        y = -13
        for i in range(0,5):
            grace(grace_list4[i],y)
            y += 5
    if z == 5:
        y = -13
        for i in range(0,5):
            grace(grace_list5[i],y)
            y += 5
    if z == 6:
        y = -13
        for i in range(0,5):
            grace(grace_list6[i],y)
            y += 5
    if z == 7:
        y = -13
        for i in range(0,5):
            grace(grace_list7[i],y)
            y += 5
    if z == 8:
        y = -13
        for i in range(0,5):
            grace(grace_list8[i],y)
            y += 5
    if z == 9:
        y = -13
        for i in range(0,5):
            grace(grace_list9[i],y)
            y += 5
    if z == 10:
        y = -13
        for i in range(0,5):
            grace(grace_list10[i],y)
            y += 5
    if z == 11:
        y = -13
        for i in range(0,5):
            grace(grace_list11[i],y)
            y += 5
    if z == 12:
        y = -13
        for i in range(0,5):
            grace(grace_list12[i],y)
            y += 5
    if z == 13:
        y = -13
        for i in range(0,5):
            grace(grace_list13[i],y)
            y += 5
    if z == 14:
        y = -13
        for i in range(0,5):
            grace(grace_list14[i],y)
            y += 5

######################

tree_angle_dict = {}

def treelist(z):
    if (z % 3) == 0:
        z1 = z
        if not z in tree_angle_dict:
            tree_angle_dict[z] = random.randrange(-140,140)
            try:
                del tree_angle_dict[z1 - 15]
            except:
                pass
    try:
        treekk(tree_angle_dict[z],12,1)
    except:
        pass

    #print (tree_angle_dict)

######################
obstacles_angle_dict = {}


def obslist(q):
    if (q % 5) == 0:
        q1 = q
        if not q in obstacles_angle_dict:
            obstacles_angle_dict[q] = random.randrange(-135,135)
            try:
                del obstacles_angle_dict[q1 - 15]
            except:
                pass

    try:
        obstacles1(obstacles_angle_dict[q])
    except:
        pass

def getobslist():
    tmpdict = obstacles_angle_dict.copy()
    return tmpdict



obstacles_angle_dict2 = {}

def obslist2(q2):
    if (q2 % 11) == 0:
        q1_2 = q2
        if not q2 in obstacles_angle_dict2:
            obstacles_angle_dict2[q2] = random.randrange(-135,135)
            try:
                del obstacles_angle_dict2[q1_2 - 22]
            except:
                pass

    try:
        obstacles2(obstacles_angle_dict2[q2])
    except:
        pass

def getobslist2():
    tmpdict2 = obstacles_angle_dict2.copy()
    return tmpdict2




obstacles_angle_dict3 = {}

def obslist3(q3):
    if (q3 % 13) == 0:
        q1_3 = q3
        if not q3 in obstacles_angle_dict3:
            obstacles_angle_dict3[q3] = random.randrange(-135,135)
            try:
                del obstacles_angle_dict3[q1_3 - 26]
            except:
                pass

    try:
        obstacles3(obstacles_angle_dict3[q3])
    except:
        pass

def getobslist3():
    tmpdict3 = obstacles_angle_dict3.copy()
    return tmpdict3

################ target #####################

target_dict = {}
target_list = []

def targetlist(t):
    if (t % 7) == 0:
        t1 = t

        if not t in target_list:
            target_list.append(t)
        #if not t in target_dict:
            target_dict[t] = random.randrange(-140,140)
            try:
                del target_dict[t1 - 21]
            except:
                pass

    try:
        target(target_dict[t])
    except:
        pass

    # print("list:",target_list)
    # print("dict:",target_dict)


def gettargetdict():
    tmpdicttarget = target_dict.copy()
    return tmpdicttarget

def deltargetdict(key):
    try:
        del target_dict[key]
    except:
        pass
