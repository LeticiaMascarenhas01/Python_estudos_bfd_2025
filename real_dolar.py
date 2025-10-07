#programa que leia um salario em real e tranforme ele em dolar

salario_real = float(input("Informe seu salário: R$ "))
dolar = salario_real / 5.33
print("Seu salário em real é R${:.2f}. E esse é seu "
"salario em dolar US$ {:.2f}".format(salario_real, dolar))

# R${:.2f} serve para formatar e deixar a moeda como valor
# flutuante