# programa que pede o valor de um saalrio
# e me de o novo valor desse saalrio com +15% de reajuste

salario_atual = float(input("Digite seu salario atual: R$ "))
print("Atualmente você recebe: R$ {}".format(salario_atual))
salario_reajustado = salario_atual + (salario_atual * 15/100)
print("Seu novo salario novo é: R$ {}".format(salario_reajustado))