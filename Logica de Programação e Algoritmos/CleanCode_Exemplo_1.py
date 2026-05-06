#Codigo Ruim
a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = (a + b + c + d) /4

if x >= 7:
    print("OK")
elif x >= 5:
    print("REC")
else: 
    print("NO")
    
#Clean Code 1
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = float(nota1 + nota2 + nota3 + nota4) /4
 
print("Sua média é: ", media)

if (media >= 7):
    print("Aprovado😁")
elif (media >= 5):
    print("Recuperação🫤")
elif (media < 5):
    print("Reprovado😖")
else: 
    print("Dados inválidos❌")

#Clean Code 2 
notas = []

for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª notas: ")))

media = sum(notas)/len(notas)

print("Sua média é: ", media)

if (media >= 7):
    print("Aprovado😁")
elif (media >= 5):
    print("Recuperação🫤")
elif (media < 5):
    print("Reprovado😖")
else: 
    print("Dados inválidos❌")