qtd_Positivos = 0
qtd_Negativos = 0

for i in range(10):
    numero = int(input("Dgite um numero: "))
    if (numero > 0): 
        qtd_Positivos = qtd_Positivos + 1
    elif(numero < 0):
        qtd_Negativos = qtd_Negativos + 1
print("A qtd de positivos é: ", qtd_Positivos)
print("A qtd de negativos é: ", qtd_Negativos)