#programa que leia o comprimento de 3 retas
#e diga ao usuário se elas formam uma reta
print(" * " * 20) #baitolagem
print("ANALISANDO TRIANGULOS")
print(" * " * 20)

r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

#a regra é que para formar um triãngulo, um comprimento não pode ser maior que a soma dos outros dois
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos digitados formam um triângulo!")
else:
    print("Não é possível formar um triângulo")