import re
name = "two.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lista = []
for x in handle:
    lista.append(re.findall("[0-9]+", x))
# y = re.findall("\S+?@\S+", x)
# print(y)
y: int = 0
listaa = []
for x in lista:
    if len(x) == 0: continue
    listaa.extend(x)

for x in listaa:
    y = y + int(x)
print(y)
