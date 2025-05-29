import pandas as pd 
from scipy import stats

d_nuevo_mexico = pd.read_csv(r'C:\Users\fdogs\OneDrive\Desktop\ING de Datos\u2\data.csv')

d_nuevo_mexico.columns = ['Fecha','Temperatura']

d_nuevo_mexico.Fecha = d_nuevo_mexico.Fecha.floordiv(100)

print("\nDataset\n",d_nuevo_mexico)

print("\nValores estadisticos\n",d_nuevo_mexico.Temperatura.describe())

regresion_lineal = stats.linregress(x = d_nuevo_mexico.Fecha, y = d_nuevo_mexico.Temperatura)
m = regresion_lineal.slope
x = 2025
b = regresion_lineal.intercept
estimacion = m * x + b
print("\n La estimacion de temperatura de nuevo mexico para mayo 2025 es: ",estimacion, "\n")pip