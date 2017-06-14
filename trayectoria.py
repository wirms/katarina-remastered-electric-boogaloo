# define a trayectory
import numpy as np
import cuaternios as cua
import copy as copy


cua = reload(cua)


def recta():
    trayectoria = np.array([
        [0, 0, 1],
        [2, 0, 1],
        [4, 0, 1]
    ])
    return trayectoria


def trayectoria():
    trayectoria = np.array([
        [0, 0, 1],
        [2, 0, 1],
        [4, 0, 1]
    ])
    return trayectoria


def cuadrado():
    trayectoria = np.array([
        [0, 0, 1],
        [2, 0, 1],
        [2, 2, 1],
        [0, 2, 1],
        [0, 0, 1]
    ])
    return trayectoria


def test(trayectoria):
    for i in range(1, trayectoria.shape[0]):
        print trayectoria[i, :] - trayectoria[i - 1, :]


def process(trayectoria, director, escala):
    vector = copy.deepcopy(trayectoria)

    for i in range(1, trayectoria.shape[0]):

        vector[i, :] = trayectoria[i, :] - trayectoria[i - 1, :]

        
        u = [1, 0, 0]
        giro = cua.giro2cua(director, u)
        orden = cua.girar(vector[i, :], giro)
        # print orden
        vector[i, :] = orden
        vector[i, :] = [vector[i, 0] * escala,
                        vector[i, 1] * escala, vector[i, 2] * escala]
        vector[i, 1] = vector[i, 1] * (-1)

    # trayectoria[i,:]=vector[i,:]
    vector[0,:]=[0,0,0]
    return vector


def importFromFile(filename='/home/david/Documents/drone/matlab/FM2/trayectory.data'):
    trayectoria = np.loadtxt(filename)
    return trayectoria


def trayectoriapatio1():
    trayectoria = np.array([
        [254, 422, 1],
        [256.7860381, 373.5076548, 1],
        [250.4728564, 323.5076548, 1],
        [249.7467797, 273.5076548, 1],
        [208.1880039, 250.3730746, 1],
        [128, 243.5691145, 1]




    ])
    return trayectoria


def trayectoriapatio2():
    trayectoria = np.array([
        [183.5254,  252.7903, 1],
        [252.7256,  300.3996, 1],
        [293.9629,  275.1505, 1],
        [340.0000,  253.0000, 1]



    ])
    return trayectoria
