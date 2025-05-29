import requests

acces_token = "EAAHyQQ1mOygBO8BkDpMY8NrcKM5QFQOa3DcVs6VCAkDyENxbrFKSIlEysPBSprMHkJKfM4TqCG6fpR490M67uHwXZACLrI9w9ZBeYaRxcDiEIvJi8Fs4DBPfIWdfaPZCEE0E9ChWJjWkFlqL8ZC54n9XsoUf3e3XRweKPp5LLbZBj4PZCIy2N6PYlj5ANrb3bb"
page_id = "494162977124143"

url = f'https://graph.facebook.com/{page_id}/posts?access_token={acces_token}'

response = requests.get(url)
data = response.json()
print (data)


for post in data['data']:
    # Imprimir los posts de texto
    print("------- POST ------- ")
    post_id = post.get('id', 'ID no disponible')

    # Obtener cantidad de likes de cada post de texto
    url2 = f'https://graph.facebook.com/{post_id}?fields=likes.summary(true)&access_token={acces_token}'
    response2 = requests.get(url2)
    data2 = response2.json()

    # Obtener cantidad de comentarios de cada post de texto
    url3 = f'https://graph.facebook.com/{post_id}/comments?summary=true&access_token={acces_token}'
    response3 = requests.get(url3)
    data3 = response3.json()

    # Obtener comentarios de cada post de texto
    url4 = f'https://graph.facebook.com/{post_id}/comments?access_token={acces_token}'
    response4 = requests.get(url4)
    data4 = response4.json()

    print(
        "Mensaje = ", post.get('message', 'Mensaje no disponible'),
        " ID =", post_id,
        " Likes =", data2.get('likes', {}).get('summary', {}).get('total_count', 0),
        " Cantidad de comentarios =", data3.get('summary', {}).get('total_count', 0)
    )

    print("--COMENTARIOS--")
    for c in data4.get('data', []):
        print("El usuario ", c.get('from', {}).get('name', 'Desconocido'), " comenta: ", c.get('message', 'Sin mensaje'))
    print(" ")
    print("Listo Terminamos este tema!!")