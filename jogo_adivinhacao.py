from random import randint
#randint(a, b) → é uma função que retorna um número
#inteiro aleatório entre a e b

computador = randint(0,100) #faz o computador "pensar" em um número
print("Vou pensar em um número, tente adivinhar...")
jogador = int(input("Em que número pensei? "))
if jogador == computador:
    print("Na mosca muleque!!")
else:
    print("Eu pensei no número {}".format(computador))