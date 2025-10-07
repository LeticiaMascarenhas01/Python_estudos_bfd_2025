#programa que leia o nome completo de uma pessoa
#e em seguida mostre seu primeiro e ultimo nome de forma separada

nome = str(input("Digite seu nome completo: ")).strip()
n = nome.split() #split "fatia" a frase, põe em uma lista
print("Seu primeiro nome é {}".format(n[0]))
print("Seu último nome é {}".format(n[len(n)-1]))
