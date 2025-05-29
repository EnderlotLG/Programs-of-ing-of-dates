import json
import os

# Ruta del archivo
archivo = "datos_facebook.txt"

# Verificar si el archivo existe y no está vacío
if not os.path.exists(archivo) or os.stat(archivo).st_size == 0:
    print("⚠ Error: El archivo está vacío o no existe.")
else:
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extraer y analizar datos
        posts = data.get("data", [])

        # Filtrar solo publicaciones con mensaje
        messages = [post for post in posts if "message" in post]

        # Contar publicaciones
        cantidad_posts = len(posts)
        cantidad_mensajes = len(messages)

        print(f"Total de publicaciones: {cantidad_posts}")
        print(f"Publicaciones con mensaje: {cantidad_mensajes}")

        # Mostrar mensajes extraídos
        for i, post in enumerate(messages, start=1):
            print(f"Post {i}: {post['message']}")

    except json.JSONDecodeError:
        print("⚠ Error: El archivo no contiene un JSON válido.")
    except Exception as e:
        print(f"⚠ Se produjo un error inesperado: {e}")
