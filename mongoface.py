import requests 
import pymongo 
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient()
db = client.test 

# Token de acceso y ID de la página
access_token = "EAAHyQQ1mOygBO8BkDpMY8NrcKM5QFQOa3DcVs6VCAkDyENxbrFKSIlEysPBSprMHkJKfM4TqCG6fpR490M67uHwXZACLrI9w9ZBeYaRxcDiEIvJi8Fs4DBPfIWdfaPZCEE0E9ChWJjWkFlqL8ZC54n9XsoUf3e3XRweKPp5LLbZBj4PZCIy2N6PYlj5ANrb3bb"
page_id = '494162977124143'

# Obtener publicaciones
url = f'https://graph.facebook.com/{page_id}/posts?access_token={access_token}'
response = requests.get(url)
data = response.json()

print("-------POST-------")

# Validar si 'data' está presente en la respuesta
if 'data' in data:
    for post in data['data']:
        post_id = post.get('id', 'ID desconocido')
        mensaje = post.get('message', 'No hay mensaje')

        # Obtener cantidad de likes
        url2 = f'https://graph.facebook.com/{post_id}?fields=likes.summary(true)&access_token={access_token}'
        response2 = requests.get(url2)
        data2 = response2.json()

        # Obtener cantidad de comentarios
        url3 = f'https://graph.facebook.com/{post_id}/comments?summary=true&access_token={access_token}'
        response3 = requests.get(url3)
        data3 = response3.json()

        # Obtener comentarios
        url4 = f'https://graph.facebook.com/{post_id}/comments?access_token={access_token}'
        response4 = requests.get(url4)
        data4 = response4.json()

        # Extraer valores con seguridad para evitar KeyError
        likes = data2.get('likes', {}).get('summary', {}).get('total_count', 0)
        cantidad_comentarios = data3.get('summary', {}).get('total_count', 0)
        comentarios = data4.get('data', [])

        # Almacenar en MongoDB
        collection = db['post']
        documento = {
            "Mensaje": mensaje,
            "ID": post_id,
            "Likes": likes,
            "Cantidad de comentarios": cantidad_comentarios,
            "Comentarios": comentarios
        }
        collection.insert_one(documento)

        # Imprimir la información desde MongoDB
        cursor = db.post.find()
        for document in cursor:
            print(document)

    print("\nListo!!")
else:
    print("❌ No se encontraron publicaciones en la página.")