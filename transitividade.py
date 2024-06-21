import os

def verifica_transitividade(matriz):
    i = len(matriz)
    for x in range(i):
        for y in range(i):
            if matriz[x][y] == 1:
                for z in range(i):
                    if matriz[y][z] == 1 and matriz[x][z] != 1:
                        return False
    return True

matriz = [['_'] * 3 for _ in range(3)]

print("Digite uma matriz 3x3 para verificar se há transitividade: ")
for line in range(3):
    for col in range(3):
        while True:
            for count in range(3): print(matriz[count])
            valor = input("Digite um valor(0 ou 1): ")
            os.system('cls')
            if (valor == '0') or (valor == '1'):
                matriz[line][col] = valor
                break

for count in range(3): print(matriz[count])

if verifica_transitividade(matriz):
    print("A matriz é transitiva.")
else:
    print("A matriz não é transitiva.")

input("Pressione Enter para encerrar o programa")
