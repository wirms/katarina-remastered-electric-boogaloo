import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import numpy as np


def dibujartrayectoria(archivo):
    f = open(archivo, "r")
    puntos = np.array([[0, 0, 0, 0, 0, 0]])
    for linea in f:

        linea = linea.split()
        for i in range(0, len(linea)):
            linea[i] = float(linea[i])

        punto = np.array(
            [[linea[1], linea[2], linea[3], linea[5], linea[6], linea[3]]])
        puntos = np.append(puntos, punto, 0)

    figura = plt.figure()
    ejes = figura.add_subplot(111, projection="3d")

    ejes.scatter(puntos[:, 0], puntos[:, 1], zs=puntos[:, 2], color="b")
    ejes.scatter(puntos[:, 3], puntos[:, 4], zs=puntos[:, 5], color="r")
    figura.show()


def test():

    asdasd = 2
    return asdasd


def dibujartrayectoria3D(rutabase):
    f = open(rutabase + "/pos.txt", "r")
    puntos = np.array([[0, 0, 0]])
    for linea in f:

        linea = linea.split()
        for i in range(0, len(linea)):
            linea[i] = float(linea[i])

        punto = np.array([[linea[1], linea[2], linea[3]]])
        puntos = np.append(puntos, punto, 0)

    g = open(rutabase + "/pos.txt", "r")
    vectores = np.array([[0, 0, 0]])
    for linea in g:

        linea = linea.split()
        for i in range(0, len(linea)):
            linea[i] = float(linea[i])

        punto = np.array([[linea[1], linea[2], linea[3]]])
        vectores = np.append(vectores, punto, 0)

    figura = plt.figure()
    ejes = figura.add_subplot(111, projection="3d")

    ejes.scatter(puntos[:, 0], -puntos[:, 1], zs=puntos[:, 2])
    for i in range(0, np.shape(vectores)[0]):
        ejes.quiver(puntos[i, 0], -puntos[i, 1], puntos[i, 2], np.math.cos(
            vectores[i, 0]), -np.math.sin(vectores[i, 1]), 0, length=-0.1)
    figura.show()
