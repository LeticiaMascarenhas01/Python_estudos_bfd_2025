#faça um programa que leia altura e largura de uma parede em metros
#calcule a quantidade de tinta necessária para pinta-la
#sabendo que cada litro de tinta pinta uma área de 2m quadrados

largura = float(input("Digite a largura da sua parede: "))
altura = float(input("Digite a altura da sua parede: "))
area = largura * altura
print("A sua parede tem dimensão {} X {}, e a dimessão total é igual a {}".format(largura, altura,area))
quantidade_tinta = area / 2
print("Para fazer a pintura dessa parede você precisa-rá de {}l de tinta".format(quantidade_tinta))