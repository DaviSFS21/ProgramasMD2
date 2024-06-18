print("O programa irá mostrar o produto cartesiano de dois conjuntos.")

conj_a = []
conj_b = []

print("Digite os valores do conjunto A (digite '/' para encerrar a leitura): ")
while True:
    valor = input('> ')
    if valor == '/':
        break
    conj_a.append(valor)

print("Digite os valores do conjunto B (digite '/' para encerrar a leitura): ")
while True:
    valor = input('> ')
    if valor == '/':
        break
    conj_b.append(valor)

produto = ''

for j in range(len(conj_b)):
    produto += '___|___' + str(conj_b[j])

produto += "__|"

# Assuming arr1 is a list
for i in range(len(conj_a)):
    produto += "\n" + str(conj_a[i]) + " | "
    for j in range(len(conj_b)):
        produto += "<" + str(conj_a[i]) + ";" + str(conj_b[j]) + "> | "

print(produto)
