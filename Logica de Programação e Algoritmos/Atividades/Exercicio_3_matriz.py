matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Matriz[{i}][{j}]= ")))
    matriz.append(linha)

x = int(input("Digite im número para ser procurado: "))
contador = 0
for i in range(4):
    for j in range(4):
        if(matriz[i][j]==x):
            print("x está na matriz")
            print("Posição i: ", i)
            print("Posição j: ", j)
            contador+=1

if(contador == 0):
    print("x não está na matriz")
