#escreva em python um programa que lê um valor
#em metros e converta em centimetros e milimetros

metros = float(input("Digite os metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print("O metro informado foi {}".format(metros))
print("O metro em centimetros fica {}".format(centimetros))
print("O metro em milimetros fica {}".format(milimetros))
