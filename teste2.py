name = "sample.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
lista = []
for line in handle:
    if "From " in line:
        t = line.split()
        t = line.strip("From ")
        t = t.strip()
        t = line.split()
        t = t[5].split(":")
        count[t[0]] = count.get(t[0], 0) + 1



for k, i in count.items():
    novaTuple = k, i
    lista.append(novaTuple)

lista = sorted(lista)
for v, k in lista:
    print(v, k)