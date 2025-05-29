from urllib.request import urlopen
from bs4 import BeautifulSoup
print("\nExtraer el titulo de una pagina web")
pagina = "https://ocotlan.tecnm.mx/"
html = urlopen(pagina)
bs = BeautifulSoup(html.read(),'html.parser')
titulo = str(bs.title)
print("\nPágina: ",pagina)
print("\nTítulo: ",titulo, " \n")
