numeros = []


for i in range(5):
    numeros.append(float(input(f"Digite a {i+1}º numero: ")))

Soma = sum(numeros)

print("Sua soma é: ", Soma)
