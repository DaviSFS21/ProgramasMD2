print("O programa irá mostrar a matriz de igualdade de dois conjuntos.")

conj_a = []
conj_b = []

pos = 0

print("Digite os valores do conjunto A (digite '/' para encerrar a leitura): ")
while True:
    valor = input('> ')
    if valor == '/':
        break
    pos += 1
    conj_a[pos] = valor

pos = 0

print("Digite os valores do conjunto B (digite '/' para encerrar a leitura): ")
while True:
    valor = input('> ')
    if valor == '/':
        break
    conj_b[pos] = valor

print("A matriz de AxB é:")

produto = '__|_' + conj_b[0]
for j in range(1, len(conj_b)):
    produto += '_|_' + conj_b[j]

produto += "_|"

for i in range(len(conj_a)):
    produto += "\n" + conj_a[i] + " | "
    for j in range(len(conj_b)):
        if conj_a[i] == conj_b[j]:
            produto += "1 | "
        else:
            produto += "0 | "

print(produto)
