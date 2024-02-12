from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

W_Width,W_Height = 500, 500

x=-250
y=-250
rain=250  
rain_down=245  
rain_speed=4
day_night=""
typed="n"

class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

def draw_points(x,y,size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def keyboardListener(key,x,y):
    global typed
    if key==b'd':
        typed="d"
        print("Day")
    if key==b'n':
        typed="n"
        print("Night")
    glutPostRedisplay()

def specialKeyListener(key,j,k):
    global x,y,rain,rain_down
    if key==GLUT_KEY_RIGHT:
        rain=250  
        rain_down=245
        if y<=-246:
            y+=1   
        print("Rain Moving Right")
        
    if key==GLUT_KEY_LEFT:
        rain=250  
        rain_down=245
        if y>=-259:
            y-=1   
        print("Rain Moving Left")

    glutPostRedisplay()

def display():
    global day_night
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if day_night=="night":
        glClearColor(0, 0, 0, 0)
    else:
        glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200,	0, 0, 0,	0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    glLineWidth(3)
    if day_night=="night":
        glColor3f(1.0,1.0,1.0)
    else:
        glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    
    # wall
    glVertex2d(150,0)
    glVertex2d(150,-180)
    glVertex2d(150,-180)
    glVertex2d(-150,-180)
    glVertex2d(-150,-180)
    glVertex2d(-150,0)
    glVertex2d(-150,0)
    glVertex2d(150,-0)
    
    # window 
    glVertex2d(30,-40)
    glVertex2d(130,-40)
    glVertex2d(130,-40)
    glVertex2d(130,-100)
    glVertex2d(130,-100)
    glVertex2d(30,-100)
    glVertex2d(30,-100)
    glVertex2d(30,-40)
    
    # door
    glVertex2d(-30,-180)
    glVertex2d(-30,-60)
    glVertex2d(-30,-60)
    glVertex2d(-90,-60)
    glVertex2d(-90,-60)
    glVertex2d(-90,-180)
    
    #floor
    glVertex2d(150,-180)
    glVertex2d(170,-200)
    glVertex2d(170,-200)
    glVertex2d(-170,-200)
    glVertex2d(-170,-200)
    glVertex2d(-150,-180)
    
    
    glEnd()
    
    # window grill
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2d(50,-40)
    glVertex2d(50,-100)
    glVertex2d(70,-40)
    glVertex2d(70,-100)
    glVertex2d(90,-40)
    glVertex2d(90,-100)
    glVertex2d(110,-40)
    glVertex2d(110,-100)
    glEnd()

    # door lock
    glColor3f(1.0,0.0,0.0)
    draw_points(-40,-120,5)

    # triangle roof
    if day_night=="night":
        glColor3f(1.0,1.0,1.0)
    else:
        glColor3f(0.0,0.0,0.0)
        
    glBegin(GL_TRIANGLES)
    glVertex2d(200,0)
    glVertex2d(0,140)
    glVertex2d(-200,0)
    glEnd()

    # rain
    glLineWidth(1)
    glBegin(GL_LINES)


    global x,y,rain,rain_down
    value=y
    for i in range(0,220):
        if y==-250:
            if i%2==0:
                if x<=250:
                    glVertex2d(x,rain)
                    glVertex2d(x,rain_down)
                    x+=25
                else:
                    x=-225
                    rain-=50
                    rain_down-=50
                    glVertex2d(-250,rain)
                    glVertex2d(-250,rain_down)

            else:
                if x<=250:
                    glVertex2d(x,rain-25)
                    glVertex2d(x,rain_down-25)
                    x+=25
                else:
                    x=-250
                    rain-=50
                    rain_down-=50
        else:
            if i%2==0:
                if x<=250:
                    glVertex2d(x,rain)
                    glVertex2d(y,rain_down)
                    x+=25
                    y+=25
                else:
                    x=225
                    y=value-25
                    rain-=50
                    rain_down-=50
                    glVertex2d(-250,rain)
                    glVertex2d(-270,rain_down)
            else:
                if x<=250:
                    glVertex2d(x,rain-25)
                    glVertex2d(y,rain_down-25)
                    x+=25
                    y+=25
                else:
                    x=-250
                    y=value
                    rain-=50
                    rain_down-=50
    glEnd()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    global day_night,x,y,rain,rain_down,rain_speed,typed
    if typed=="n":
        day_night="night"
    else:
        day_night="day"
    rain=(rain-rain_speed+250)%500-250
    rain_down=(rain_down-rain_speed+250)%500-250

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0,0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Building a House in Rainfall")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop() 
