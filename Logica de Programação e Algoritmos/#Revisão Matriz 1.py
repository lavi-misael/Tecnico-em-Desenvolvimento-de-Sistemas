#Revisão Matriz 1
#Solicitar a quantidade de linhas 
#Solicitar a quantidade de colunas 
#Preencher a matriz
#Calcular a soma de todos os números 
#____________________________________ 

#Criar as variaveis 
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a a quantidade de colunas: "))
matriz = []
soma = 0 

#Sempre repetir quando for preencher a matriz
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)

#Sempre repetir quando for percorrer a matriz
for i in range(linhas):
    for j in range(colunas):
        soma = soma + matriz [i][j]
        print("A soma é: ", soma)