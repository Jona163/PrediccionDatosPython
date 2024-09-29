# Predicción de datos Mejorada

# Importación de librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
x = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
y = np.array([106.46, 123.08, 132.12, 152.27, 180.67, 205.05, 227.23, 249.46])

def fx(x1, coef):
    """Calcula el valor de la función polinómica dada en coeficientes."""
    return np.polyval(coef, x1)

# Anno para la predicción
anno = 2000

# Gráfica de predicciones
for i in range(1, 11):  # Grados del polinomio desde 1 hasta 10
    coef = np.polyfit(x, y, i)  # Ajuste del polinomio
    p = np.polyval(coef, anno)   # Predicción para el año 2000

    print(f"Para grado {i} la predicción es {p}")
    
    x1 = np.linspace(1920, anno + 1, 1000)  # Valores de x para graficar
    y1 = fx(x1, coef)                       # Valores de y correspondientes


    # Configuración de la gráfica
    plt.figure(figsize=[20, 10])
    plt.title(f"Cantidad de litros vs año. Para grado: {i}")
    plt.scatter(x, y, s=120, c='blueviolet', label='Datos reales')
    plt.plot(x1, y1, "--", linewidth=3, color='orange', label='Ajuste polinómico')
    plt.scatter(anno, p, s=200, c='red', label='Predicción 2000')
    plt.yticks(range(100, 320, 20))
    plt.grid("on")

  # Etiquetas de los ejes
    plt.xlabel("Años")
    plt.ylabel("Cantidad litros")
    plt.legend()
    plt.show()

# Cálculo de MSE para cada grado del polinomio
grado = np.arange(0, 31)  # Grados de 0 a 30
aproxi = []  # Lista para almacenar las aproximaciones
mse_values = []  # Lista para almacenar los valores de MSE
