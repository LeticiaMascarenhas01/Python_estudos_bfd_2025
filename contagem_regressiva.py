# UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA
# PARA O ESTOURO DE FOGOS DE ARTIFÍCIO
# INDO DE 10 ATÉ 0, COM PAUSA DE 1 SEGUNDO ENTRE ELES

from time import sleep   #sleep serve para que entre um print e outro haja uma pausa programada
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print("BUM! CABUM! POW!")