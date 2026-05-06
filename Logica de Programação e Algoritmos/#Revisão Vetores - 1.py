#Revisão Vetores - 1
#Solicitar ao usuário a quantidade de números
#Preencher o vetor
#Percorrer o vetor e calcular a soma dos números
#Exibir a soma 
#_______________________________________________

#Passo 1) Criar variaveis 
qtd = int(input("Digite a quantidade de números: "))
vetor = []
soma = 0 

#Passo 2) Preencher o vetor
for i in range(qtd):
    vetor.append(int(input("Digite um número: ")))

#Passo 3) Percorrer o vertor 
for num in vetor:
    soma = soma + num

print("A soma é: ", soma)
