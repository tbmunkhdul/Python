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



score = 0
collision = 4


tempdict = {}
tempdict2 = {}
tempdict3 = {}
tempdicttarget = {}

def detect(x):
    global collision
    global score
   
    pitchshrink = 0
    pitchshrink_hori = 0

    if pitch == 10 or pitch == -10:
        pitchshrink = 0
        pitchshrink_hori = 1.5
    if pitch == 20 or pitch == -20:
        pitchshrink = 0
        pitchshrink_hori = 2
    if pitch == 30 or pitch == -30:
        pitchshrink = 1
        pitchshrink_hori = 2.5
    if pitch == 40 or pitch == -40:
        pitchshrink = 1.5
        pitchshrink_hori = 3
    if pitch == 50 or pitch == -50:
        pitchshrink = 2
        pitchshrink_hori = 3.5
    if pitch == 60 or pitch == -60:
        pitchshrink = 2.5
        pitchshrink_hori = 4
    if pitch == 70 or pitch == -70:
        pitchshrink = 3
        pitchshrink_hori = 4.5
    if pitch == 80 or pitch == -80:
        pitchshrink = 3.5
        pitchshrink_hori = 5
    if pitch == 90 or pitch == -90:
        pitchshrink = 4
        pitchshrink_hori = 6


    if not x == 0:
        x1 = x
        x1 = float('%.2f' % x1)
        x2 = x
        x2 = float('%.2f' % x2)
        x3 = x
        x3 = float('%.2f' % x3)
        xt = x
        xt = float('%.2f' % xt)
        if (x1 % 5) == 0:
            tempdict = my_obs.getobslist()
            print("obs_cordinate:", tempdict[int(x1)])
            if (tempdict[int(x1)] - 3.5 - pitchshrink < -1*translatex < tempdict[int(x1)] + 3.5 + pitchshrink) and ( 1500 + pitchshrink_hori< -1*translatez < 1519.5 - pitchshrink_hori):
                score += 5      
            elif ((tempdict[int(x1)] - 20.5 + pitchshrink < -1*translatex < tempdict[int(x1)] - 3.5 - pitchshrink) and (-1*translatez < 1524 + pitchshrink_hori)) or ((tempdict[int(x1)] + 3.5 + pitchshrink < -1*translatex < tempdict[int(x1)] + 20.5 - pitchshrink) and (-1*translatez < 1524 + pitchshrink_hori)):
                collision -= 1
            elif (tempdict[int(x1)] - 3.5 - pitchshrink < -1*translatex < tempdict[int(x1)] + 3.5 + pitchshrink) and ( 1519.5 - pitchshrink_hori < -1*translatez < 1524 + pitchshrink_hori ):
                collision -= 1      

        if (x2 % 11) == 0:
            tempdict2 = my_obs.getobslist2()
            print("obs_cordinate:", tempdict2[int(x2)])
            if (tempdict2[int(x2)] - 0.5 - pitchshrink < -1*translatex < tempdict2[int(x2)] + 0.5 + pitchshrink) and ( 1500 + pitchshrink_hori< -1*translatez < 1545.5 - pitchshrink_hori ):
                score += 8      
            elif ((tempdict2[int(x2)] - 17.5 + pitchshrink < -1*translatex < tempdict2[int(x2)] - 0.5 - pitchshrink) and (-1*translatez < 1550 + pitchshrink_hori)) or ((tempdict2[int(x2)] + 0.5 + pitchshrink < -1*translatex < tempdict2[int(x2)] + 17.5 - pitchshrink) and (-1*translatez < 1550 + pitchshrink_hori)):
                collision -= 1
            elif (tempdict2[int(x2)] - 0.5 - pitchshrink < -1*translatex < tempdict2[int(x2)] + 0.5 + pitchshrink) and ( 1545.5 - pitchshrink_hori < -1*translatez < 1550 + pitchshrink_hori):
                collision -= 1      


        if (x3 % 13) == 0:
#            print("angle:", int(x3))
            tempdict3 = my_obs.getobslist3()
            if (tempdict3[int(x3)] - 3.5 - pitchshrink < -1*translatex < tempdict3[int(x3)] + 3.5 + pitchshrink) and ( 1523.5 + pitchshrink_hori < -1*translatez < 1535.5 - pitchshrink_hori):
                score += 10      
            elif ((tempdict3[int(x3)] - 20.5 + pitchshrink < -1*translatex < tempdict3[int(x3)] - 3.5 - pitchshrink) and ( 1519.5 - pitchshrink_hori <-1*translatez < 1540 + pitchshrink_hori)) or ((tempdict3[int(x3)] + 3.5 + pitchshrink < -1*translatex < tempdict3[int(x3)] + 20.5 - pitchshrink) and ( 1519.5 - pitchshrink_hori<-1*translatez < 1540 + pitchshrink_hori)):
                collision -= 1
            elif (tempdict3[int(x3)] - 3.5 - pitchshrink < -1*translatex < tempdict3[int(x3)] + 3.5 + pitchshrink) and (( 1519.5 - pitchshrink_hori < -1*translatez < 1523.5 + pitchshrink_hori) or ( 1535.5 - pitchshrink_hori < -1*translatez < 1540 + pitchshrink_hori)):
                collision -= 1      
            elif (( tempdict3[int(x3)] - 8.5 + pitchshrink < -1*translatex < tempdict3[int(x3)] + 8.5 - pitchshrink) and (-1*translatez < 1520 + pitchshrink_hori)):
                collision -= 1      


        try:
            if (xt % 7) == 0:
                tempdicttarget = my_obs.gettargetdict()
                # print ("main :",tempdicttarget)
                if ((tempdicttarget[int(xt)] - 11.5 + pitchshrink < -1*translatex < tempdicttarget[int(xt)] + 11.5 - pitchshrink) and (-1*translatez < 1520.5 + pitchshrink_hori)): 
                    collision -= 1      
        except:
            pass

    # print("_______________detect___________________")
    # print("plane level : ",-1*translatez)
    # print(-1*translatex - 6.5,"\____",-1*translatex,"____/",-1*translatex + 6.5)
    # print("pitch",pitch)
    # print("pitchshrink",pitchshrink)
    # print("__________________________________________")


shootedlist = [] 

def detectfire():
    global score
    tempdicttarget = my_obs.gettargetdict()
    # print ("main detectfire :",tempdicttarget)

    for key , value in tempdicttarget.items():
        if ((value - 5 < -1*translatex < value + 5) and (-1*translatez < 1520)):
            # print("key:", key,"value:", value )
            shootedlist.append(key)
           
            if shootedlist.count(key) > 3:
                score += 10
                my_obs.deltargetdict(key) 
    

    # print("translatex",-1*translatex)
    # print("translatez",-1*translatez)




def drawground1(from_,to_):
    for angle in range(from_,to_,-1):
        glPushMatrix()

        glRotatef(angle,1,0,0)
        ground()
        my_obs.mygracelist((-1*angle) % 14)
    
        my_obs.treelist(-1*angle)        

        my_obs.obslist(-1*angle)
        my_obs.obslist2(-1*angle)
        my_obs.obslist3(-1*angle)
        my_obs.targetlist(-1*angle)

   
        glPopMatrix()




def ground():
    glColor3f(0.5, 0.35, 0.05)
#    glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.5, 0.35, 0.05,1))
    glBegin(GL_QUADS)
    glVertex3f(-150,-13.5,1500)
    glVertex3f(-150,13.5,1500)
    glVertex3f(150,13.5,1500)
    glVertex3f(150,-13.5,1500)
    glEnd()

def bullet():
    glLineWidth(2)
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex3f(0,15,1500)
    glVertex3f(0,0,1500)
    glEnd()

smokecolor = (
    (0,0,0),
    (0,0,0),
    (0.5,0.5,0.5),
    (1,0,0),
    (1,0,0),
    (1,1,1)
     )

def smokedot(x,y,z,color):
    glLineWidth(1)
    glColor3fv(smokecolor[color])
    glBegin(GL_POINTS)
    glVertex3f(x,y,z) 
    glEnd()

def drawsmoke1():
    for i in range(0,100):
        smokedot(random.randrange(0,200)/100,random.randrange(-500,-700,-1)/100,random.randrange(0,200)/100,random.randrange(0,6))
def drawsmoke2():
    for i in range(0,100):
        smokedot(random.randrange(0,200)/100,random.randrange(-700,-900,-1)/100,random.randrange(0,200)/100,random.randrange(0,6))
def drawsmoke3():
    for i in range(0,100):
        smokedot(random.randrange(0,200)/100,random.randrange(-900,-1100,-1)/100,random.randrange(0,200)/100,random.randrange(0,6))
def drawsmoke4():
    for i in range(0,100):
        smokedot(random.randrange(0,200)/100,random.randrange(-1100,-1300,-1)/100,random.randrange(0,200)/100,random.randrange(0,6))


blacksmokecolor = (
    (0,0,0),
    (1,1,1),
    (0.5,0.5,0.5)
     )

def blacksmokedot(x,y,z,color):
    glLineWidth(1)
    glColor3fv(blacksmokecolor[color])
    glBegin(GL_POINTS)
    glVertex3f(x,y,z) 
    glEnd()

def blackdrawsmoke():
    for i in range(0,400):
        blacksmokedot(random.randrange(-200,200)/100,random.randrange(-200,-400,-1)/100,random.randrange(0,600)/100,random.randrange(0,3))




def crosshair():
    glLineWidth(1)
    glColor3f(0,0,0)

    glBegin(GL_LINES)
    glVertex3f(0,10,5)
    glVertex3f(0,10,5.8)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0,10,6.2)
    glVertex3f(0,10,7)
    glEnd()


    glBegin(GL_LINES)
    glVertex3f(-1,10,6)
    glVertex3f(-0.2,10,6)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(0.2,10,6)
    glVertex3f(1,10,6)
    glEnd()

def crashbackgroud():
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex3f(10,0,0)
    glVertex3f(10,0,10)
    glVertex3f(30,0,10)
    glVertex3f(30,0,0)
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

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0) # on top nice viewing
              


    glEnable(GL_DEPTH_TEST)

    #################### Splash start
    my_splash.splash_running()
	################## Splash end
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt(0, 0, 100, 0, 0, 0, 0, 1, 0) # on top nice viewing
    gluLookAt(0, -30, 10, 0, 0, 0, 0, 1, 0) # nice viewing
              


    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    img = pygame.image.load('leaf.bmp')
    textureData = pygame.image.tostring(img, "RGBA", 1)
    width = img.get_width()
    height = img.get_height()
    im = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, im)
    glTexEnvf (GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)    
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    # #############################
    pygame.key.set_repeat(50, 50)


    keyboard1 = ""

    global speedangle
    speedangle = 0

    global translatex
    global translatez
    global pitch
    translatex = 0
    translatez = -1550
    pitch = 0
    cycle = 0
    warncycle = 0 
    goingdowncycle = 0

    tempcountground = 0

    tempspeedangle = 0
    tempspeedangle = speedangle

    from_s = 0
    to_s = -15

    bulletangle = 0
    bulletx = 0
    bullety = 0
    bulletz = 0        
    shoot = ""
    status = "normal"
    warningtime = 6
    global collision
    goingdown = "yes"
    goingdowntime = 5


    #ligth()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                    keyboard1 = "left"
              if event.key == pygame.K_RIGHT:
                    keyboard1 = "right"
              if event.key == pygame.K_UP:
                    keyboard1 = "up"
              if event.key == pygame.K_DOWN:
                    keyboard1 = "down"
              if event.key == pygame.K_q:
                    keyboard1 = "q"
              if event.key == pygame.K_w:
                    keyboard1 = "w"
              # if event.key == pygame.K_e:
              #       keyboard1 = "e"
              if event.key == pygame.K_r:
                    keyboard1 = "r"

      

        glClearColor (1.0, 1.0, 1.0, 1.0);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # # # #displaying texts


        all_func.printtext(-20,10,25,'DISTANCE :'+str(tempcountground*10)+' Meters')

        all_func.printtext(-20.5,10,23.5,'SCORE :'+str(score))
        
        collisiontext = ""
        collisiontext = str(collision)
        if collision < 0:
            collisiontext = "Plane Is Crashed"
        all_func.printtext(-20.5,10,22.0,'Damage :'+collisiontext)

        altitudetext = ""
        altitudetext = str((-1*translatez - 1500)/2)
        all_func.printtext(15,10,25,'ALTITUDE : '+altitudetext+' Meters')

        warning = (-1*translatez - 1500)/2
        warningtext = "Normal Air Pressure"

        if warning >= 100:
            warningtext = "Low Air Pressure"
            all_func.printtextwarning(5.5,10,23.5,'WARNING : '+warningtext)
            all_func.printtextwarning(30.5,10,23.5,': remaining '+str(warningtime)+' sec')
            if warncycle == 50:
                warningtime -= 1
                warncycle = 0
            warncycle += 1
        elif warning < 100:
            warningtext = "Normal Air Pressure"
            all_func.printtextwarningnormal(5.5,10,23.5,'WARNING : '+warningtext)
            warningtime = 6
            warncycle = 0    

        if warningtime < 0:
            collision = -1


        if status == "normal":
            if keyboard1 == "left":
                translatex += 2
            if keyboard1 == "right":
                translatex -= 2 
            if keyboard1 == "up":
                translatez -= 2 
            if keyboard1 == "down":
                translatez += 2 
            # if keyboard1 == "e": # delete it after tested
            #     speedangle += 0.05 
            if keyboard1 == "r":
                shoot = "fire"
            if keyboard1 == "q":
                if pitch == 90:
                    pitch = 90 
                elif pitch != 0:    
                    pitch += 10
                elif pitch == 0: 
                    pitch = 10
            if keyboard1 == "w":
                if pitch == -90:
                    pitch = -90 
                elif pitch != 0:    
                    pitch -= 10
                elif pitch == 0: 
                    pitch = -10

        keyboard1 = "" 
        if status == "normal":
            crosshair()
            my_plane.Myobj()
    

        if collision == 3:
            drawsmoke1()
        if collision == 2:
            drawsmoke1()
            drawsmoke2()
        if collision == 1:
            drawsmoke1()
            drawsmoke2()
            drawsmoke3()
        if collision == 0:
            drawsmoke1()
            drawsmoke2()
            drawsmoke3()
            drawsmoke4()
        if collision < 0:
            if goingdown == "yes":
                drawsmoke1()
                drawsmoke2()
                drawsmoke3()
                drawsmoke4()
                my_plane.Myobj()
                status = "freeze"
                translatez += 1


        if translatez > -1502:
            blackdrawsmoke()
            my_plane.Myobjcrashed()
            goingdown = "no"
            status = "freeze"
            collision = -1
        
        if goingdown == "no":
            crashbackgroud()
            all_func.printtextgoingdown(10,-1,8,'YOUR RESULT')
            all_func.printtextgoingdown(10,-1,6,'YOUR SCORE :'+str(score))
            all_func.printtextgoingdown(10,-1,4,'DISTANCE :'+str(tempcountground*10)+' Meters')
            all_func.printtextgoingdown(10,-1,2,'>>>>> '+str(goingdowntime)+' <<<<<')

            if goingdowncycle == 40:
                goingdowntime -= 1
                goingdowncycle = 0
            goingdowncycle += 1
            
            if goingdowntime == 0:
                pygame.quit()
                os.system('python game2g.py')



        if speedangle - tempspeedangle >= 0.998:
            tempspeedangle = speedangle
            from_s -= 1
            to_s -= 1
            tempcountground += 1

        glPushMatrix()  # rotaion pich 
        glRotatef(pitch,0,1,0)
        glPushMatrix()  # translation 1
        glTranslatef(translatex,0,translatez)
        glPushMatrix()  # rotation 1
        glRotatef(speedangle,1,0,0)       
        drawground1(from_s,to_s)
        glPopMatrix()  # rotation 1
        glPopMatrix()  # rotaion pich
        glPopMatrix()  # translation 1
        
        bulletz = 1500


        # fire
        if shoot == "fire":
            glPushMatrix()
            glTranslatef(bulletx,bullety,-bulletz)
            glPushMatrix()
            glRotatef(bulletangle,1,0,0)
            bullet()
            glPopMatrix()
            glPopMatrix()
            bulletangle -= 1
            if bulletangle == -11: 
                detectfire()

        if bulletangle < -10:
            shoot = ""
            bulletangle = 0   
 

       
        if status == "normal":
            speedangle += 0.05  # auto run

        
        detect(speedangle)
        # print("translatez",translatez)

        pygame.display.flip()
        pygame.time.wait(10)
        cycle += 1

main()