numeros = []
soma = 0
media = 0

for i in range(4):
    num = int(input("Digite um numero: "))
    numeros.append(num)


for numero in numeros:
   soma = numero + soma 
media = soma / 4
print("A media dos numeros é ", media)

if(media < 4):
    print("Reprovado")
elif(media >= 4 and media <=7):
    print("Recuperação")
else:
    print("aprovado")

