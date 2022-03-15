import string
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

import ssl

global lista

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1479585.xml", context=ctx).read()

arvore = ET.fromstring(html)
resultado = arvore.findall(".//count")
soma: int = 0
x: int = 0
for li in resultado:
    x = int(li.text)
    soma = soma + x

print(soma)


