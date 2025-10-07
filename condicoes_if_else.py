tempo = int(input("Quantos anos tem seu carro? "))
if tempo <= 5:
    print("Seu carro é novo!")
else:
    print("Não é um carro tão novo assim!")

#de forma resumida
tempo_carro = int(input("Quantos anos tem seu carro? "))
print("Carro novo" if tempo_carro<=3 else("Carro velho"))

#na identação do código, o que vem colado no lado esquerdo
#será sempre executado (if/else)
#e o que vem com tab de distancia pode ou não,
#dependendo do código, ser executado (o print por exemplo)

nome = str(input("Qual seu nome? "))
if nome == "Samara":
    print("Seja bem-vinda!!")
else:
    print("Não é quem eu esperava")
print("Olá, {}".format(nome))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Parabéns {}, você passou no concurso com média {}!".format(nome,media))
else:
    print("Sua média ficou {}, e infelizmente você está na lista de espera".format(media))