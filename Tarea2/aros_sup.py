import os
import random
from CC3501Utils import *

####################################################
# Clase Aro Superior
####################################################

global velx
velx=Vector(-3,0)

class Aros_sup(Figura):
    def __init__(self, dh,vel = Vector(-3,0),pos=Vector(400, 300), rgb=(1.0, 1.0, 1.0)):
        self.vel = vel
        self.dh = dh
        super().__init__(pos, rgb)

    def figura(self):
        
        # Se dibuja la pelota
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.27, 0)
        a = 18 * self.dh
        b = 8 * self.dh
        r = 0
        g = 0.42
        bl = 0.18
        for j in range(25):
            bl = bl - 0.001 * j
            g = g - 0.001 * j
            glColor3f(r, g, bl)
            i = 0.0
            a = a - 0.05 * j
            b = b - 0.05 * j
            while (i < 10):
                alax = a * cos(i)
                alay = b * sin(i)
                if (alay > 0):
                    glVertex(alax, alay)
                i = i + 0.001
        glEnd()

    def mover(self,posx,posy):
        self.pos = sumar(self.pos, ponderar(2, self.vel))
        if self.pos.x < -200:
            self.pos = Vector(posx + 800, posy)