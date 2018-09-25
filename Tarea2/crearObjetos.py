import random
from CC3501Utils import *
from vista import *
from pelota import *
from aros_sup import *
from aros_inf import *
from fondo import *
from nubes import *
from ala import *
from OpenGL.GLUT import *

def crearObjetos():
    objetos = []
    fondo = Fondo(Vector(0, 0))

    v1 = random.randint(3,5)
    x1 = random.randint(50,700)
    y1 = random.randint(250,550)
    nube1 = Nube(v1,Vector(x1,y1))

    v2 = random.randint(3, 5)
    x2 = random.randint(50, 700)
    y2 = random.randint(250, 550)
    nube2 = Nube(v2, Vector(x2, y2))

    v3 = random.randint(3, 5)
    x3 = random.randint(50, 700)
    y3 = random.randint(250, 550)
    nube3 = Nube(v3, Vector(x3, y3))

    aro_x1 = random.randint(400,600)
    aro_x2 = random.randint(400,600)
    aro_y1 = random.randint(300,400)
    aro_y2 = random.randint(300,400)
    dh1 = random.randint(5,8)
    dh2 = random.randint(5,8)
    aro_sup1 = Aros_sup(dh1,Vector(-3, 0), Vector(200+aro_x1, aro_y1))
    aro_sup2 = Aros_sup(dh2,Vector(-3, 0), Vector(700+aro_x2, aro_y2))
    ala = Ala(Vector(0, 7), Vector(0, 0), False)
    pelota = Pelota(Vector(0, 7), Vector(150, 300), False)
    aro_inf1 = Aros_inf(dh1,Vector(-3, 0), Vector(200+aro_x1, aro_y1))
    aro_inf2 = Aros_inf(dh2,Vector(-3, 0), Vector(700+aro_x2, aro_y2))

    objetos.append(fondo)
    objetos.append(nube1)
    objetos.append(nube2)
    objetos.append(nube3)
    objetos.append(aro_sup1)
    objetos.append(aro_sup2)
    objetos.append(ala)
    objetos.append(pelota)
    objetos.append(aro_inf1)
    objetos.append(aro_inf2)

    return objetos

def strike(aro,pelota):
    if aro.pos.x - 18 * (aro.dh-1) < pelota.pos.x < aro.pos.x + 18 * (aro.dh-1) and aro.pos.y - 10 < pelota.pos.y < aro.pos.y + 10:
        return True

def spare(aro,pelota):
    if aro.pos.x - 18 * (aro.dh+1) < pelota.pos.x < aro.pos.x - 18 * (aro.dh-1) and aro.pos.y - 10 < pelota.pos.y < aro.pos.y + 10:
        return True
    if aro.pos.x + 18 * (aro.dh -1) < pelota.pos.x < aro.pos.x + 18 * (aro.dh+1)and aro.pos.y - 10 < pelota.pos.y < aro.pos.y + 10:
        return True



