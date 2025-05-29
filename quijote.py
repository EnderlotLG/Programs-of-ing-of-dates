import re
import nltk

# Descargar las dependencias necesarias
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Cargar archivo de texto a memoria
with open(r'C:\Users\fdogs\OneDrive\Desktop\ING de Datos\u2\texto_001_don_quijote.txt', 'r', encoding='utf-8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

# Convertir el texto a minúsculas
texto_minusculas = texto.lower()

# Eliminar símbolos y caracteres especiales usando expresiones regulares
texto_sin_simbolos = re.sub(r'[^\w\s]', '', texto_minusculas)

# Convertir el texto en tokens
tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
print('\nTokens totales =', len(tokens_de_mi_texto))

# Cargar stopwords del español
palabras_vacias = set(stopwords.words('spanish'))

# Filtrar los tokens eliminando las stopwords
lista_final = []
for palabra in tokens_de_mi_texto:
    if palabra not in palabras_vacias:
        lista_final.append(palabra)

# Imprimimos la cantidad de tokens ya sin stopwords
print("Total de tokens sin stopwords =", len(lista_final))

# Análisis de Sentimientos
# Lista de palabras positivas y negativas en español
palabras_positivas = ['bueno', 'encantado', 'bonito', 'increíble', 'superior']
palabras_negativas = ['malo', 'decepcionado', 'feo', 'terrible', 'inferior']

# Inicializar contadores de palabras positivas y negativas
numero_positivas = numero_negativas = 0

# Buscar palabras positivas y negativas dentro del texto
for elemento in lista_final:
    if elemento in palabras_positivas:
        numero_positivas += 1
    if elemento in palabras_negativas:
        numero_negativas += 1

# Imprimir resultados
print('\nPalabras positivas encontradas =', numero_positivas)
print('Palabras negativas encontradas =', numero_negativas)

# Calcular y mostrar polaridad del texto
print('\nPolaridad del texto =')
polaridad = numero_positivas - numero_negativas
if polaridad > 0:
    print('Positiva\n')
elif polaridad < 0:
    print('Negativa\n')
else:
    print('Neutral\n')
