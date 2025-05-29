from urllib.request import urlopen
from bs4 import BeautifulSoup

print("\n🔍 Extraer información de una página web")

# URL de la página web
pagina = "https://www.ferchogs.facpages.com.mx/NIMBUS-DEV2/"

try:
    # Abrir la página y parsear el HTML
    html = urlopen(pagina)
    bs = BeautifulSoup(html.read().decode("utf-8"), 'html.parser')

    # Extraer título
    titulo = bs.title.text.strip()
    print("\n🌐 Página:", pagina)
    print("\n📌 Título:", titulo)

    # 🔹 1. Obtener todos los enlaces de la página
    print("\n🔗 Enlaces encontrados:")
    for link in bs.find_all("a", href=True):  # Solo enlaces con "href"
        print("➡", link["href"])

    # 🔹 2. Extraer todas las imágenes
    print("\n🖼 Imágenes encontradas:")
    for img in bs.find_all("img"):
        print("🖼", img.get("src"))

    # 🔹 3. Obtener los encabezados principales
    print("\n📢 Encabezados encontrados:")
    for h in bs.find_all(["h1", "h2", "h3"]):  # Buscar H1, H2 y H3
        print(f"🔹 {h.name}: {h.text.strip()}")

    # 🔹 4. Extraer el contenido de los párrafos
    print("\n📄 Contenido de los párrafos:")
    for p in bs.find_all("p"):
        print("📄", p.text.strip())

    # 🔹 5. Extraer una sección específica (ejemplo: div con id="contenido")
    contenido_div = bs.find("div", id="contenido")
    if contenido_div:
        print("\n📦 Contenido del div 'contenido':")
        print(contenido_div.text.strip())
    else:
        print("\n⚠ No se encontró un div con id='contenido'.")

except Exception as e:
    print("\n❌ Error al acceder a la página:", str(e))
