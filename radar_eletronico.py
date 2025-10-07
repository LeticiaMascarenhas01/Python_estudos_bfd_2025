velocidade_atual = int(input("Qual a velocidade atual do carro? "))
if velocidade_atual <= 60:
    print("Ótimo! Bom dia!")
elif velocidade_atual <= 80:
    print("Melhor prestar atenção!")
else:
    multa = (velocidade_atual - 80) * 7 # -8 pois só se deve calcuar a multa com os KMs excedido
    print("Muito veloz, pague a multa de {:.2f}!".format(multa))