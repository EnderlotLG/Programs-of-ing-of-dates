import json

# JSON en formato de cadena (con triple comilla para mejor manejo)
json_str = """
{
  "nombre": "Juan", 
  "edad": 30, 
  "ciudad": "Madrid"
}
"""

# Deserialización: convertir JSON a diccionario de Python
datos = json.loads(json_str)

# Imprimir el diccionario
print(datos)  # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Acceder a los valores usando las claves del diccionario
print(datos["nombre"])  # Juan
print(datos["edad"])  # 30

#Json con listas 

json_str = """
{
  "nombre": "Carlos",
  "edad": 40,
  "habilidades": ["Python", "Machine Learning", "Big Data"]
}
"""

datos = json.loads(json_str)

print(datos["habilidades"])       # ['Python', 'Machine Learning', 'Big Data']
print(datos["habilidades"][0])    # Python

json_str = """
{
  "usuario": {
    "nombre": "David",
    "edad": 35,
    "direccion": {
      "calle": "Avenida Siempre Viva",
      "ciudad": "Madrid",
      "pais": "España"
    }
  }
}
"""

datos = json.loads(json_str)

print(datos["usuario"]["nombre"])  # David
print(datos["usuario"]["direccion"]["ciudad"])  # Madrid

#Ejeercicio 4

json_str_mal = '("nombre": "Lucas", "edad":28, "ciudad":Madrid,)'

try:
    datos = json.loads(json_str_mal)
    print(datos)
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {e}")


#ejercico 5

    datos = {"nombre":"juan","edad":30,"ciudad":'Madrid'}

    #serializar el diccionario a una cadena JSON
    json_str = json.dumps(datos)
    print(json_str) #{"nombre":"juan","edad":30,"ciudad":'Madrid'}

    #Ejemplo 6

    datos ={
        "nombre":"Ana",
        "edad": 25,
        "ciudad":"Barcelona"
    }

    json_str = json.dumps(datos, indent=4)
    print(json_str)


    #ejemplo 7

    datos = {
        "nombre":"Carlos",
        "edad":40,
        "Habilidades":["Python", "Machine Learning", "Big data"]
    }
    json_str = json.dumps(datos, indent=4)
    print(json_str)

#Ejemplo 8

datos = {
  "Usuario":{
      "nombre":"Davida",
      "edad":35,
      "Direccion":{
          "Calle": "Avenida Simpre Viva",
          "Ciudad":"Madrid",
          "Pais":"España"
      }
  }
  
}
json_str = json.dumps(datos, indent=4)
print(json_str)


#Ejemplo 9 
##Definir una Clase

class Persona:
    def __init__(self,nombre, edad,ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad 
#Creara un objeto
Persona = Persona ("sergio",33,"Sevilla")

#Funcion para Convertir el Objeto en un Diccionario
def convertir_a_diccionario(obj):
    return obj.__dict__

#Serealiar el Objeto 

json_str = json.dumps(Persona, default=convertir_a_diccionario, indent=4)
print(json_str)

#Ejercicio 10
class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def convertir_a_diccionario(obj):
    return obj.__dict__

persona = Persona("Luis", 40)

try:
    json_str = json.dumps(persona, default=convertir_a_diccionario, indent=4)
    print(json_str)
except TypeError as e:
    print(f"Error: {e}")