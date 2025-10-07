a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

#verificando o menor número
if a < b and a < c:
    print("O menor valor é o {}".format(a))
if b < a and b < c:
    print("O menor valor é o {}".format(b))
if c < b and c < a:
    print("O menor valor é o {}".format(c))

#verificando o maior número
#fazendo de forma que economiza linha
maior = a  #já defino quem é e depois "quebro" isso testando as outras linhas
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print("O maior número é o {}".format(maior))
