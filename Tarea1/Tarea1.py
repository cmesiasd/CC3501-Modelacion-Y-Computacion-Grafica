#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import math

RRR = 0.261 #Últimos digitos del RUT


class Cordillera:
    def __init__(self, ancho,largo,dh,tol):
        """
        Constructor
        :param ancho: Ancho en metros
        :param largo: Largo en metros
        :param dh: Tamaño cada celda en metros.
        """
        self._ancho = ancho
        self._largo = largo
        self._dh = dh
        self._tol = tol


        #Dimensiones de la matriz
        self._h = int(float(ancho) / dh) #Altura
        self._w = int(float(largo) / dh)

        #Dimensiones de objetos
        self._marx = int(float(1200+400*RRR)/dh)
        self._refineria = int(120/dh)
        self._tramox1 = int(280/dh)
        self._tramox2 = int(800/dh)
        self._tramox3 = int(300/dh)
        self._tramox4 = int(500/dh)
        self._tramox5 = int((self._w-(self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3+self._tramox4)))

        self._nieve = int((ancho - 1800) / dh)
        self._tramoy1 = int(93/dh)
        self._tramoy2 = int((1500+200*RRR)/dh)
        self._tramoy3 = int((1300+200*RRR)/dh)
        self._tramoy4 = int((1850+100*RRR)/dh)
        self._mary = int(100/dh)
        self._nivelmar = self._h - self._mary

        self._matrix = np.ones((self._h, self._w))
        self._lista = []

    def plot(self, t, **kwargs):
        # Si se define el color de fondo como negro
        if kwargs.get("black"):
            mpl.rcParams['axes.facecolor'] = '000000'

        # Se imprime el grafico
        fig = pl.figure()
        ax = fig.add_subplot(111)
        cax = ax.imshow(self._matrix,interpolation='none', cmap='gnuplot',vmin=-20,vmax=600)
        cfg = pl.gcf()
        fig.colorbar(cax)

        # Experimental: se modifican las etiquetas de los ejes
        xnum = len(ax.get_xticks()) -1
        ynum = len(ax.get_yticks()) -1
        xlabel = []
        ylabel = []

        for i in range(xnum): xlabel.append(str(int(float(self._largo) * i / (xnum))))
        for j in range(ynum): ylabel.append(str(int(float(self._ancho) * j / (ynum - 1))))
        ylabel.reverse()
        if kwargs.get("xlabel"):
            ax.set_xticklabels([''])
            pl.xlabel("Ancho [m]")
        else:
            ax.set_xticklabels([''])
        if kwargs.get("ylabel"):
            ax.set_yticklabels([''] + ylabel)
            pl.ylabel("Altura [m]")
        else:
            ax.set_yticklabels([''])

        # Se establece el titulo de la ventana
        pl.title("Temperatura en t=" + str(int(t)) + "\n")
        cfg.canvas.set_window_title("Temperatura en t=" + str(int(t)))
        plt.show()

    def cond_borde(self,t):
        ##MONTAÑAS
        #Peq inclinación
        for i in range((self._marx+self._refineria),self._marx+self._refineria+self._tramox1):
            for j in range((self._nivelmar-self._tramoy1), self._nivelmar):
                if j+1 > (-self._tramoy1/self._tramox1)*(i - (self._marx+self._refineria))+self._nivelmar:
                    self._matrix[j][i] = 20
                    self._lista.append([i,j])


        #Subida primera montaña
        for i in range(self._marx+self._refineria+self._tramox1, self._marx+self._refineria+self._tramox1+self._tramox2):
            for j in range(self._nivelmar-self._tramoy2, self._nivelmar+1):
                if j+1 > (((-self._tramoy2+self._tramoy1)/self._tramox2)*(i-(self._marx+self._refineria+self._tramox1))+(self._nivelmar-self._tramoy1)):
                    self._matrix[j][i] = 20
                    self._lista.append([i,j])

        #Bajada primera montaña
        for i in range(self._marx+self._refineria+self._tramox1+self._tramox2, self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3):
            for j in range(self._nivelmar-self._tramoy2, self._nivelmar+1):
                if j+1 > (((-self._tramoy3+self._tramoy2)/self._tramox3)*(i-(self._marx+self._refineria+self._tramox1+self._tramox2))+(self._nivelmar-self._tramoy2)):
                    self._matrix[j][i] = 20
                    self._lista.append([i,j])


        #Subida segunda montaña
        for i in range(self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3, self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3+self._tramox4):
            for j in range(self._nivelmar-self._tramoy4, self._nivelmar+1):
                if j+1 > (((-self._tramoy4+self._tramoy3)/self._tramox4)*(i-(self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3))+(self._nivelmar-self._tramoy3)):
                    self._matrix[j][i] = 20
                    self._lista.append([i,j])
                    if (self._h - j) * self._dh > 1800:
                        self._matrix[j][i] = 0


        #Bajada segunda montaña
        for i in range(self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3+self._tramox4, self._w):
            for j in range(self._nivelmar-self._tramoy4, self._nivelmar+1):
                if j+1 > (((self._tramoy4-self._tramoy3)/self._tramox4)*(i-(self._marx+self._refineria+self._tramox1+self._tramox2+self._tramox3+self._tramox4))+(self._nivelmar-self._tramoy4)):
                    self._matrix[j][i] = 20
                    self._lista.append([i,j])
                    if (self._h - j) * self._dh > 1800:
                        self._matrix[j][i] = 0


        #BAJO NIVEL DEL MAR
        for j in range(self._nivelmar, self._h):
            # Parte de abajo de las montañas
            for i in range(self._marx, self._w):
                self._matrix[j][i] = -20
                self._lista.append([i,j])
            # Mar
            for i in range(self._marx):
                if j > self._nivelmar:
                    self._matrix[j][i] = -20
                    self._lista.append([i, j])
                #Superficie del mar
                else:
                    if t>= 0 and t <= 8:
                        self._matrix[j][i] = 4
                    elif t > 8 and t <= 16:
                        self._matrix[j][i] = 4 + 2*(t-8)
                    elif t > 16 and t <= 24:
                        self._matrix[j][i] = 20 - 2*(t-16)
        #ATMÓSFERA
        for j in range(0, self._nivelmar+1):
            for i in range(self._marx):
                if [i,j] in self._lista:
                    continue
                else:
                    self._matrix[j][i] = self._matrix[self._nivelmar][i] - float(6 / 1000 * self._dh) * (
                                        self._nivelmar - j)
            for i1 in range(self._marx, self._w):
                if [i1,j] in self._lista:
                    continue
                else:
                    self._matrix[j][i1] = self._matrix[self._nivelmar][i] - float(6 / 1000 * self._dh) * (
                                        self._nivelmar - j)
        #REFINERÍA
        for i in range(self._marx, self._marx + self._refineria):
            self._matrix[self._nivelmar][i] = 450 * (math.cos(math.pi * t / 12) + 2)

        #Adentro Montañanas
        for i in range(self._marx+self._refineria,self._w):
            for j in range(self._nivelmar):
                if [i,j+1] in self._lista:
                    self._matrix[j+3][i] = -20

    def _single_iteration(self, matrix_new, matrix_old, omega):
        """
        Inicia calculo sólo 1 iteración
        :return:
        """

        for x in range(1, self._w - 1):
            for y in range(1, self._nivelmar+1):
                prom = 0
                if [x, y] in self._lista:
                    if x < self._w - 2:
                        y = 1
                        x = x + 1
                else:
                    #Borde derecho
                    if [x + 1, y] in self._lista:
                        # Borde derecho-inferior
                        if [x + 1, y + 1] in self._lista:
                            prom = 0.25 * (2 * matrix_old[y - 1][x] + 2 * matrix_old[y][x - 1] - 4 * matrix_old[y][x])
                        else:
                            prom = 0.25 * (matrix_old[y - 1][x] + matrix_old[y + 1][x] + 2 * matrix_old[y][x - 1] - 4 * matrix_old[y][x])
                    #Borde inferior
                    elif [x, y + 1] in self._lista:
                        prom = 0.25 * (2 * matrix_old[y - 1][x] + matrix_old[y][x - 1] + matrix_old[y][x + 1] - 4 * matrix_old[y][x])
                    #Borde izquierdo
                    if [x - 1, y] in self._lista:
                        # Borde izquierdo-inferior
                        if [x - 1, y + 1] in self._lista:
                            prom = 0.25 * (2 * matrix_old[y - 1][x] + 2 * matrix_old[y][x + 1] - 4 * matrix_old[y][x])
                        else:
                            prom = 0.25 * (matrix_old[y - 1][x] + matrix_old[y + 1][x] + 2 * matrix_old[y][x + 1] - 4 * matrix_old[y][x])

                    #General
                    else:
                        prom = 0.25 * (matrix_old[y - 1][x] + matrix_old[y + 1][x] + matrix_old[y][x - 1] + matrix_old[y][x + 1] - 4 * matrix_old[y][x])
                # Calcula nuevo valor
                matrix_new[y][x] = matrix_old[y][x] + prom * omega

    @staticmethod
    def _convergio(mat_old, mat_new, tol):
        """
        Retorna un booleano indicando si el problema convergió o no.

        :param mat_old: Vector de soluciones previo
        :param mat_new: Vector de soluciones posterior
        :param tol: Error máximo admisible
        :return:
        """
        not_zero = (mat_new != 0)
        diff_relativa = (mat_old - mat_new)[not_zero]
        max_diff = np.max(np.fabs(diff_relativa))
        return [max_diff < tol, max_diff]

    def start(self, omega):
        """
        Soluciona el sistema
        :return:
        """
        # Clonamos las matrices
        mat_new = np.copy(self._matrix)
        # Inicia variables
        niters = 0
        run = True
        converg = []
        omega = omega - 1
        if not 0 <= omega <= 1:
            raise Exception('Omega tiene un valor incorrecto')

        while run:
            mat_old = np.copy(mat_new)
            self._single_iteration(mat_new, mat_old, omega)
            #self._unaIteracion(mat_new,mat_old,omega)
            niters += 1
            print("llevo " + str(niters) + " iteraciones")
            converg = self._convergio(mat_old, mat_new, self._tol)
            run = not converg[0]

        print('El programa terminó en {0} iteraciones, con error {1}'.format(niters, converg[1]))
        self._matrix = np.copy(mat_new)
        return niters

    def w_op(self):
       return (4 / (2 + (math.sqrt(4 - (math.cos(math.pi / (self._w - 1)) + math.cos(math.pi / (self._h - 1)))**2))))


cord = Cordillera(2100,4000,32,1)
cord.cond_borde(0) #Crea las matrices con cond de borde iniciales

# Se prueban varios w
#omegas = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
#iters = []
#errors = []
#for w in omegas:
#    iters.append(cord.start(w))
cord.start(cord.w_op()) #Ejecuta el método iterativo, con omega optimo
cord.plot(0,ylabel=True) #Plotea la nueva matriz


# Graficamos variación de iteraciones
#plt.plot(omegas, iters)
#plt.xlabel('Omega')
#plt.ylabel('Numero de iteraciones')
#plt.show()