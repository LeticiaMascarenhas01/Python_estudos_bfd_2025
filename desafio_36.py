# programa que aprova o empréstimo bancário para compra de uma casa
# o programa vai perguntar o valor da casa, salario do comprador e em quantos anos ele vai pagar
# calcule o valor da prestação mensal, sabendo que não excede 30% do salário
# ou então o empréstimo será negado

casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o valor do salário? R$ "))
anos = float(input("Quantos anos deseja quitar a casa? R$ "))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print("Para pagar uma casa de R$ {:.2f} em {} anos, terá uma prestação de R$ {}".format(casa, anos, prestacao))
if prestacao <= minimo:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")