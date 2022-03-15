import json

import urllib.request
import urllib.parse
import urllib.error
import ssl


url = "http://py4e-data.dr-chuck.net/comments_1479586.json"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
dados = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(dados)

soma: int = 0
for item in info["comments"]:
    soma = soma + int(item["count"])


print(soma)