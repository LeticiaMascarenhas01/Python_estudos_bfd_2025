from random import randint
computador = randint(0, 10)

print('''Olá, sou seu computador e acabei de pensar em um número. 
Será que você consegue adivinhar em qual estou pensando? ''')

acertou = False
palpites = 0
while not acertou:
    adivinha = int(input("Digite um número entre 0 e 10: "))
    palpites += 1
    if adivinha == computador:
        acertou = True
    else:
        if adivinha < computador:
            print("Mais...tente mais uma vez")
        elif adivinha > computador:
            print("Menos...tente mais uma vez")
print("Acertou com {} tentativas. Parabéns!".format(palpites))