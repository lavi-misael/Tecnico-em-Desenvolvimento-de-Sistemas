numeros = []
soma = 0
media = 0

for i in range(6):
    num = int(input("Digite um numero: "))
    numeros.append(num)


for numero in numeros:
   soma = numero + soma 
media = soma / 6
print("A media dos numeros é ", media)

