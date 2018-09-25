import os

from CC3501Utils import *

####################################################
# Clase Fondo
####################################################
global velx
velx=Vector(-1,0)

class Fondo(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):

        glBegin(GL_QUADS)
        #glColor3f(103/255.0, 193/255.0, 182/255.0)
        glColor3f(235/255, 152/255, 78/255)
        glVertex2f(1600, 0)
        glVertex2f(0, 0)
        glVertex2f(0, 600)
        glVertex2f(1600, 600)
        glEnd()

        ##MONTAÑAS##

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(86/255, 46/255, 1/255)
        glVertex2f(0, 0)
        glVertex2f(0, 50)
        glVertex2f(200, 100)
        glVertex2f(400, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(86 / 255, 46 / 255, 1 / 255)
        glVertex2f(100, 0)
        glVertex2f(300, 150)
        glVertex2f(600, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(86 / 255, 46 / 255, 1 / 255)
        glVertex2f(400, 0)
        glVertex2f(690, 100)
        glVertex2f(800, 50)
        glVertex2f(800, 0)
        glEnd()

        ###
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(86 / 255, 46 / 255, 1 / 255)
        glVertex2f(800, 0)
        glVertex2f(800, 50)
        glVertex2f(1000, 100)
        glVertex2f(1200, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(86 / 255, 46 / 255, 1 / 255)
        glVertex2f(900, 0)
        glVertex2f(1100, 150)
        glVertex2f(1400, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(86 / 255, 46 / 255, 1 / 255)
        glVertex2f(1200, 0)
        glVertex2f(1490, 100)
        glVertex2f(1600, 50)
        glVertex2f(1600, 0)
        glEnd()

    def mover(self):
        self.pos = sumar(self.pos, ponderar(2, velx))
        if self.pos.x == -800:
            self.pos = Vector(0, 0)

