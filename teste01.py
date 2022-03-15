import urllib.request
import urllib.parse
import urllib.error
import re
from bs4 import BeautifulSoup
import ssl

global lista

contagem = int(input("Contagem - "))
posicao = int(input("Posição - "))

def busca_link(url):
    lista: list = []
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lista.append(tag.get('href', None))
    return lista


def pegar_url(lista):
    count: int = 1
    for x in lista:
        if count == posicao:
            return x
        count = count + 1


urlRetorno = pegar_url(busca_link("http://py4e-data.dr-chuck.net/known_by_Cael.html"))
while contagem >= 2:
    lista = []
    lista = busca_link(urlRetorno)
    urlRetorno = pegar_url(lista)
    print(f"{urlRetorno} {contagem}")
    if contagem == 2:
        nome = re.split("_+", urlRetorno)[2]
        print(re.split("\.", nome)[0])

    contagem = contagem - 1
