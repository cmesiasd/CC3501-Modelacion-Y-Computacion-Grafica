from CC3501Utils import *

global gver
gver = Vector(0, -1)

####################################################
# Clase Ala
####################################################
class Ala(Figura):
    def __init__(self, vel=Vector(0,0),  pos=Vector(0, 0), flotando=False, rgb=(1.0, 1.0, 1.0)):
        self.vel = vel
        self.flotando = flotando
        super().__init__(pos, rgb)

    def figura(self):

        glBegin(GL_QUADS)
        glColor3f(0.9, 1, 1)
        glVertex2f(0, 110)
        glVertex2f(50, 110)
        glVertex2f(50, 90)
        glVertex2f(0, 90)
        glEnd()

        glColor3f(0.9, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0, 100)
        radio = 10
        ang = 2 * pi / 10
        for i in range(11):
            ang_i = ang * i
            glVertex(cos(ang_i) * radio, 100 + sin(ang_i) * radio)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.9, 1, 1)
        glVertex2f(15, 90)
        glVertex2f(50, 90)
        glVertex2f(50, 70)
        glVertex2f(15, 70)
        glEnd()

        glColor3f(0.9, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(15, 80)
        radio = 10
        ang = 2 * pi / 10
        for i in range(11):
            ang_i = ang * i
            glVertex(15 + cos(ang_i) * radio, 80 + sin(ang_i) * radio)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.9, 1, 1)
        glVertex2f(30, 70)
        glVertex2f(50, 70)
        glVertex2f(50, 50)
        glVertex2f(30, 50)
        glEnd()

        glColor3f(0.9, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(30, 60)
        radio = 10
        ang = 2 * pi / 10
        for i in range(11):
            ang_i = ang * i
            glVertex(30 + cos(ang_i) * radio, 60 + sin(ang_i) * radio)
        glEnd()

    def mover(self,dt, flotando):
        if (not flotando):
            #self.pos = sumar(sumar(self.pos, sumar(ponderar(dt, ponderar(dt, gver)), ponderar(dt * dt / 2.0, gver))),ponderar(2, velx))
            self.pos = Vector(230,125)
        else:
            self.pos = sumar(self.pos, sumar(self.vel, ponderar(dt * dt / 2, gver)))

    def rotarArriba(self):
        self.pos = rotar(self.pos,1)
    def rotarAbajo(self):
        self.pos = rotar(self.pos,-1)
