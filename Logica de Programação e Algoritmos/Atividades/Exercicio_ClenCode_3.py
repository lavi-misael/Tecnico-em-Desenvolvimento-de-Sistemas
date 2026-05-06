numeros = []


for i in range(4):
    numeros.append(float(input(f"Digite a {i+1}º numero: ")))

Soma = sum(numeros)/len(numeros)

print("Sua soma é: ", Soma)