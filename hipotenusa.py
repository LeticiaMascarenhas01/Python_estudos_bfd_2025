#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa

# ** significa "elevado", 2**2 = dois elevado a dois
# :.2f para apresentar apenas duas casas decimais

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenuza = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print("A hipotenusa mede: {:.2f}".format(hipotenuza))