import os
import random

from CC3501Utils import *
from vista import *
from pelota import *
from aros_sup import *
from aros_inf import *
from fondo import *
from nubes import *
from ala import *
from crearObjetos import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "Flappy Dunk - Versión Fruna")
    vista = Vista()

    pjs = crearObjetos()
    fondo = pjs[0]
    aro_sup1 = pjs[4]
    aro_sup2 = pjs[5]
    ala = pjs[6]
    pelota = pjs[7]
    aro_inf1 = pjs[8]
    aro_inf2 = pjs[9]
    dt=0.1
    run = True
    puntaje = 0

    while run:
        paso = False
        if strike(aro_inf1,pelota) or strike(aro_inf2,pelota):
            if not paso:
                paso = True
                puntaje = puntaje + 2

        if spare(aro_inf1, pelota) or spare(aro_inf2,pelota):
            if not paso:
                paso = True
                puntaje = puntaje + 1
        y1 = random.randint(350,500)
        y2 = random.randint(350,500)
        x1 = random.randint(100, 500)
        x2 = random.randint(100, 500)
        aro_sup1.mover(x1,y1)
        aro_inf1.mover(x1,y1)
        aro_sup2.mover(x2,y2)
        aro_inf2.mover(x2,y2)
        fondo.mover()
        pelota.mover(dt, pelota.flotando)
        ala.mover(dt, ala.flotando)

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pelota.flotando = True
                    ala.flotando = True
                    dt = 0
        if pelota.piso() or pelota.cielo():
            run = False

        vista.dibujar(pjs)
        pygame.display.flip()  # actualizar pantalla


        dt=dt+0.2
        pygame.time.wait(int(1000 / 60))  # ajusta a 60 fps

    pygame.quit()
    print("Puntaje total: ")
    print(puntaje)

main()