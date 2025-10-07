salario = float(input("Qual seu salário? "))
print("Seu salário atual é {}".format(salario))

if salario >= 1250:
    salario_reajuste = salario + (salario * 10 / 100)
    print("Seu salario com 15%  de aumento fica R${}".format(salario_reajuste))
else:
    salario_reajuste = salario + (salario * 15 / 100)
    print("Seu salario com 10%  de aumento fica R${}".format(salario_reajuste))
print("Seu salário era de R${:.2f}, e agora você passou a ganhar R${:.2f}".format(salario, salario_reajuste))