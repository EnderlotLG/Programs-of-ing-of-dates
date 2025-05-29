import pandas as pd 
from scipy import stats

Hawai = pd.read_csv(r'C:\Users\fdogs\OneDrive\Desktop\ING de Datos\u2\data2.csv')

Hawai.columns = ['Fecha','Temperatura']

Hawai.Fecha = Hawai.Fecha.floordiv(100)

print("\nDataset\n",Hawai)

print("\nValores estadisticos\n",Hawai.Temperatura.describe())

regresion_lineal = stats.linregress(x = Hawai.Fecha, y = Hawai.Temperatura)
m = regresion_lineal.slope
x = 2025
b = regresion_lineal.intercept
estimacion = m * x + b
print("\n La estimacion de temperatura de Hawai para mayo 2025 es: ",estimacion, "\n")