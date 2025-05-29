import re                                   #Manejo de expresiones regulares
import nltk                                  #Procesa lenguaje natural
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize     #Tokenizar un texto
from nltk.corpus import stopwords           #Cargar las stopwords del español

#Cargar archivo de texto a memoria
with open(r'C:\Users\fdogs\OneDrive\Desktop\ING de Datos\u2\discurso_sentimientos_14_septiembre_1813.txt','r',encoding='utf-8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

#Convertir el texto a minusculas
texto_minusculas = texto.lower()

#Eliminar simbolos y caracteres especiales usando expresiones regulares
texto_sin_simbolos = re.sub(r'[^\w\s]','',texto_minusculas)

#Convertimos a tokens todo el texto y lo imprimimos en pantalla
tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
print('\nTokens totales = ',len(tokens_de_mi_texto))

#Cargamos las "stopwords" del español (palabras que no nos aportan informacion)
palabras_vacias = set(stopwords.words('spanish'))

#Filtramos los tokens eliminando las stopwords
lista_final = []
for palabra in tokens_de_mi_texto:
    if palabra not in palabras_vacias:
        lista_final.append(palabra)

#Imprimimos la cantidad de tokens ya sin stopwords
print('Total de tokens sin stopwords = ',len(lista_final))

#Analisis de sentimientos
#Cargar lista de palabras positivas y negativas en español
with open (r'C:\Users\fdogs\OneDrive\Desktop\ING de Datos\u2\texto_002_palabras_positivas.txt','r',encoding='utf-8') as archivo_positivas:
    palabras_positivas = [linea.strip() for linea in archivo_positivas]
with open (r'C:\Users\fdogs\OneDrive\Desktop\ING de Datos\u2\texto_003_palabras_negativas.txt','r',encoding='utf-8') as archivo_negativas:
    palabras_negativas = [linea.strip() for linea in archivo_negativas]

#Inicializar contadores de palabras positivas y negativas
numero_positivas = numero_negativas = 0

#Buscamos las palabras positivas y negativas dentro del texto
for elemento in lista_final:
    if elemento in palabras_positivas:
        numero_positivas += 1
    elif elemento in palabras_negativas:
        numero_negativas += 1

#Imprimir resultados
print("\nPalabras positivas encontradas = ", numero_positivas)
print("\nPalabras negativas encontradas = ", numero_negativas)
print("Polaridad del texto = ")
polaridad = numero_positivas - numero_negativas
if polaridad>0: print('Positiva\n')
elif polaridad<0: print("Negativa\n")
else: print("Polaridad del texto Neutral\n")