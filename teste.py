name = "sample.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    if "From:" in line:
        t = line.split()
        t = line.strip("From: ")
        t = t.strip()
        count[t] = count.get(t, 0) + 1

maiorNumero = None
maiorPalvra = None
for palavra, numero in count.items():
    if maiorNumero is None or numero > maiorNumero:
        maiorPalvra = palavra
        maiorNumero = numero
print(maiorPalvra, maiorNumero)