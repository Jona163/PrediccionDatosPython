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

 print(f"para grado {i} la predicción es {p}")
    x1 = np.linspace(1920, anno + 1, 1000)
    y1 = fx(x1, coef) # funcion
    plt.figure(figsize=[20,10])
    plt.title("Cantidad de litros vs año. Para grado: " + str(i))
    
    plt.scatter(x,y,s=120,c='blueviolet')
    plt.plot(x1,y1,"--",linewidth=3,color='orange')
    plt.scatter(anno,p,s=200,c='red')
    plt.yticks(range(100,320,20))
    plt.grid("on")
    ax=plt.gca()
    ax.set_xlabel("$años$")
    ax.set_ylabel("$Cantidad litros$")
    #plt.savefig("img" + str(i)+".jpg", dpi=600)
    plt.show()
anno = 2000
grado = np.arange(0, 30 + 1, 1) #de 0 a 100 de 1 en 1
aproxi = np.array([])
y_pred_vec = np.array([])
for i in grado:
    coef = np.polyfit(x,y,i)
    p = np.polyval(coef, anno)
    aproxi = np.append(aproxi, p)
    
    # para la MSE
    y_pred_vec = np.array([])
    for j in x: # para la MSE
        y_pred = np.polyval(coef, j)
        y_pred_vec = np.append(y_pred_vec,y_pred)
    #print(f"los y: {y}")
    #print(f"los y_aprox: {y_pred_vec}")
    MSE = (sum( (y - y_pred_vec)**2 ))/len(y)
    print(f"Para grado {i} El MES es: {MSE}")
plt.figure(figsize=[20,10])
plt.title("Grado del polinomio vs predicción")
plt.plot(grado,aproxi,"--",linewidth=3,color='red')
plt.grid("on")
plt.show()
