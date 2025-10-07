numero = int(input("Digite um número qualquer: "))
resultado = numero % 2 # retorna o resto da divisão inteira de dois números
print("O resultado foi {}".format(resultado))
if resultado == 0:
    print("O número {} é par!".format(numero))
else:
    print("O número {} é ímpar!".format(numero))

#resto da divisão é o que sobra: 7 ÷ 2 = 3
#Mas 3 × 2 = 6, e sobra 1.
#Esse 1 é o resto.