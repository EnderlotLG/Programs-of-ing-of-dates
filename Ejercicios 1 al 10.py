import json

# JSON en formato de cadena
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
print(datos)
print(datos["nombre"])  
print(datos["edad"])  

# JSON con listas 
json_str = """
{
  "nombre": "Carlos",
  "edad": 40,
  "habilidades": ["Python", "Machine Learning", "Big Data"]
}
"""

datos = json.loads(json_str)
print(datos["habilidades"])       
print(datos["habilidades"][0])    

# JSON con anidación 
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
print(datos["usuario"]["nombre"])  
print(datos["usuario"]["direccion"]["ciudad"])  

# **Ejercicio 4: JSON mal formado corregido**
json_str_mal = '{"nombre": "Lucas", "edad": 28, "ciudad": "Madrid"}'

try:
    datos = json.loads(json_str_mal)
    print(datos)
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {e}")

# **Ejercicio 5: Serializar un diccionario a JSON**
datos = {"nombre": "juan", "edad": 30, "ciudad": "Madrid"}
json_str = json.dumps(datos)
print(json_str)

# **Ejemplo 6: Serializar con formato bonito**
datos = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Barcelona"
}
json_str = json.dumps(datos, indent=4)
print(json_str)

# **Ejemplo 7: JSON con listas**
datos = {
    "nombre": "Carlos",
    "edad": 40,
    "Habilidades": ["Python", "Machine Learning", "Big Data"]
}
json_str = json.dumps(datos, indent=4)
print(json_str)

# **Ejemplo 8: JSON anidado**
datos = {
  "Usuario": {
      "nombre": "David",
      "edad": 35,
      "Direccion": {
          "Calle": "Avenida Siempre Viva",
          "Ciudad": "Madrid",
          "Pais": "España"
      }
  }
}
json_str = json.dumps(datos, indent=4)
print(json_str)

# **Ejemplo 9: Serializar un objeto**
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad 

# Crear un objeto de la clase Persona
persona_objeto = Persona("Sergio", 33, "Sevilla")

# Función para convertir el objeto en un diccionario
def convertir_a_diccionario(obj):
    return obj.__dict__

# Serializar el objeto 
json_str = json.dumps(persona_objeto, default=convertir_a_diccionario, indent=4)
print(json_str)

# **Ejercicio 10: Serialización con manejo de error**
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
