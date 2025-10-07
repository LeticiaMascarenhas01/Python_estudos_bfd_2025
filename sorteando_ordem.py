#programa que receba o nome de quatro alunos
#e sorteie a ordem para apresentação do trabalho
import random

#random.shuffle = serve para sortear um aleatorio da lista

a1 = str(input("Digite o nome do aluno numero 1: "))
a2 = str(input("Digite o nome do aluno numero 2: "))
a3 = str(input("Digite o nome do aluno numero 3: "))
a4 = str(input("Digite o nome do aluno numero 4: "))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print("A ordem de apresentação será ")
print(lista)