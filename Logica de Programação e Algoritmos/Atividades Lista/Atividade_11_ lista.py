vetor = []
soma = 0 

for i in range(7):
    vetor.append(int(input("Digite um numero: ")))

for i in vetor:
    soma = soma + i
    print("A soma é: ", soma)