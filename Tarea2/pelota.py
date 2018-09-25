import os
from CC3501Utils import *


global gver

gver = Vector(0, -1)

####################################################
# Clase Pelota
####################################################
class Pelota(Figura):
    def __init__(self, vel=Vector(0,0),  pos=Vector(0, 0), flotando=False, rgb=(1.0, 1.0, 1.0)):
        self.vel = vel
        self.flotando = flotando
        self.radio = 20
        super().__init__(pos, rgb)

    def figura(self):
        dh = 2 #Factor de escala
        # Se dibuja la pelota
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0, 0)
        radio = self.radio*dh
        i = 0.0
        while(i<10):
            alax = radio * cos(i)
            alay = radio * sin(i)
            glVertex(alax,alay)
            i = i + 0.001
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0,0,0)
        radio2 = 15*dh
        i = 0.0
        while (i < 10):
            alax = radio2 * cos(i)
            alay = radio2 * sin(i)
            glVertex(alax, alay)
            i = i + 0.001
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1, 0, 0)
        radio = 14 * dh
        i = 0.0
        while (i < 10):
            alax = radio * cos(i)
            alay = radio * sin(i)
            glVertex(alax, alay)
            i = i + 0.001
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        radio = 5 * dh
        i = 0.0
        while (i < 10):
            alax = radio * cos(i)
            alay = radio * sin(i)
            glVertex(alax, alay)
            i = i + 0.001
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        radio = 3 * dh
        i = 0.0
        while (i < 10):
            alax = radio * cos(i)
            alay = radio * sin(i)
            glVertex(alax, 14 * dh + alay)
            i = i + 0.001
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        radio = 3 * dh
        i = 0.0
        while (i < 10):
            alax = radio * cos(i)
            alay = radio * sin(i)
            glVertex(sin(pi/3)*14*dh+alax, alay - cos(pi/3)*dh*14)
            i = i + 0.001
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        radio = 3 * dh
        i = 0.0
        while (i < 10):
            alax = radio * cos(i)
            alay = radio * sin(i)
            glVertex(alax - sin(pi / 3) * 14 * dh , alay - cos(pi / 3) * dh * 14)
            i = i + 0.001
        glEnd()

    def mover(self,dt, flotando):
        if (not flotando):
            self.pos = Vector(300,200) #posicón de partida.
        else:
            self.pos = sumar(self.pos, sumar(self.vel, ponderar(dt * dt / 2, gver)))

    def piso(self):
        return self.pos.y - self.radio < 0

    def cielo(self):
        return self.pos.y + self.radio > 650


