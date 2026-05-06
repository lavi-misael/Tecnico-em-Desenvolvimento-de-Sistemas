m1 =[]
m2 = []
matriz_soma = []

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"M1[{i}][{j}]= ")))
    m1.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"M2[{i}][{j}]= ")))
    m2.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(m1[i][j]+m2[i][j])
    matriz_soma.append(linha)

#EXIBIR MATRIZ (REPETIR SEMPRE QUE EXIBIR MATRIZ)
print("Matriz Soma: ")
for linha in matriz_soma:
    print(linha)

