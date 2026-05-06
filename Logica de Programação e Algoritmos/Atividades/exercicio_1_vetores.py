numeros = []
Cont_Pares = 0

for i in range(10):
    num = int(input("Digite um numero: "))
    numeros.append(num)

for numero in numeros:
    if(numero % 2 == 0):
        Cont_Pares = Cont_Pares + 1
print("O qtd de par é: ", Cont_Pares)


