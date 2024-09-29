#Prediccion de datos

#Importacion de librerias a ocupar con python.
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1920,1930,1940,1950,1960,1970,1980,1990])
y=np.array([106.46,123.08,132.12,152.27,180.67,205.05,227.23,249.46])
def fx (x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx = fx + p*x1**n
        n = n - 1
    return fx
anno = 2000
for i in range(0,10):
    coef = np.polyfit(x,y,i)
    p = np.polyval(coef, anno)
