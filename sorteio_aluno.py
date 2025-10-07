#um professor quer sortear um dos seus 4 alunos para apagar o quadro
#faça um programa que ajude ele, lendo o nome dos 4 alunos
#e dando o nome escolhido
import random

#random: gerador de numeros aleatorios
#random.choice: serve para escolher aleatoriamente um item de uma sequência (como lista, tupla ou string)

a1 = str(input("Digite o nome do aluno numero 1: "))
a2 = str(input("Digite o nome do aluno numero 2: "))
a3 = str(input("Digite o nome do aluno numero 3: "))
a4 = str(input("Digite o nome do aluno numero 4: "))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print("O aluno escolhido é: {}".format(escolhido))