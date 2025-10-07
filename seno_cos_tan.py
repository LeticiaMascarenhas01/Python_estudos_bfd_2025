#programa que lê um numero qualquer
#e mostre na tela o valor de seno, cosseno,     tangente desse angulo
import math

#math.sin: função usada para calcular o seno de um número
#radiano: é a razão entre o comprimento de um arco e o seu raio

angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
print("O angulo {} tem o SENO igual a: {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo {} tem o COSSENO igual a: {:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O angulo {} tem o TANGENTE igual a: {:.2f}".format(angulo, tangente))