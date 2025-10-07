# "Curso em vídeo Python" cada caracter, incluindo espaço, oculpa uma posição
# então lê-se 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

frase = "Curso em vídeo Python"
dividido = frase.split() # lista me mostra cada palavra em uma posição
print(dividido[3]) # me mostra a palavra na posição pedida
print(dividido[3] [2]) # me mostra a letra escolhida, dentro de uma palavra escolhida anteriormente

print(frase[3]) # me dá o que estiver na posição 3, nesse caso, o S
print(frase[3:13]) # me dá o que estiver na posição 3 até o 13
print(frase[3:13:2]) # me dá o que estiver na posição 3 até o 13 de 2 em 2
print(frase[3::2]) # me dá o que estiver na posição 3 até o final, de 2 em 2
print(frase[:15:2]) # me dá o que estiver no começo até a posição 15, de 2 em 2
print(frase.count('o')) #descobrir quantas letras, silabas ou numeros uma frase possui
print(len(frase)) # descobrir o tamanho da frase
print(frase.replace("Python", "Android")) # para trocar uma palavra por outra
print(frase.split()) # cria uma lista com as letras

frase.find("deo")