print("O programa irá comparar elementos iguais de dois conjuntos.")

conj_a = []
conj_b = []

pos = 0

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

print("A matriz que indica os elementos iguais é:")
print(conj_a)

result = '__|_' + conj_b[0]
for j in range(1, len(conj_b)):
    result += '_|_' + conj_b[j]

result += "_|"

for i in range(len(conj_a)):
    result += "\n" + conj_a[i] + " | "
    for j in range(len(conj_b)):
        if conj_a[i] == conj_b[j]:
            result += "1 | "
        else:
            result += "0 | "

print(result)
