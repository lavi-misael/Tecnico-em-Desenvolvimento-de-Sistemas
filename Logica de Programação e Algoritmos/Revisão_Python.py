#Criando uma varialvel numerica
numero = 10 

#Criando uma variavel textual 
nome = "Gabriel"

#Usuário inserir um texto 
nome_completo = input("Digite seu nome: ")

#Usuário inserir um numero inteiro 
idade = int(input("Digite sua idade: "))

#Usuário inserir um numero decimal 
salário = float(input9("Digite seu salário: "))

#Estruturas condicionais - if
if(salário >1500 and idade >18):
    print("Você pode tirar carta!")
elif(salário <1500 or idade <18):
    print("Você não pode tirar carta")
else:
    print("inválido")

#Estruturas condicionais exemplo 2
turno = input("Digite seu turno(m/v/n:")

if(turno == "M"): #Utilize dois iguais para comparar
    print("Bom dia!")
elif(turno == "V"):
    print("Boa Tarde!")
elif(turno == "N"):
    print("Boa Noite!")
else: #else não tem parenteses
    print("Inválido")

#Estrutura de repetição
#0 -> 10
for i in range(11): #Sempre coloque +1
    print(i)

#1 -> 15 
for i in range(1,16): #Sai do 1 até o 15
    print(i)

#5 -> 65 (aumentando de 5 em 5)
for i in range(5,66, +5):
    print(i)

#122 -> 0 (tirando de 2 em 2)
for i in range(122,-1,-2):
    print(i)

#Usuario escolhe o inicio e fim 
#Inicio -> fim
inicio = int(input("Inicio")):
fim = int(input("Fim"))

for i in range (inicio, fim+1): #Sempre colocar 1
    print(i)

#Vetores
nomes = []

#Sempre utilizar para preencher o vetor 
for i in range(5):
    nomes.appende(input("Digite um nome:"))

#Sempre utilizar para exibir o vetor
for nome in nomes:
    print(nome)
