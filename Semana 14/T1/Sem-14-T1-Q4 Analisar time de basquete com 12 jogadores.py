jogadores = []
total_altura = 0

for r in range(12):
    nome = input()
    altura = float(input('Digite a altura do jogador: '))
    jogadores.append((nome, altura))
    total_altura += altura

maior_altura = 0
superiores_media = []

for jogador in jogadores:
    if jogador[1] > maior_altura:
        maior_altura = jogador[1]

media_altura = total_altura / 12

for jogador in jogadores:
    if jogador[1] > media_altura:
        superiores_media.append(jogador)

print("JOGADOR MAIS ALTO DO TIME")
for jogador in jogadores:
    if jogador[1] == maior_altura:
        print(jogador[0])
        print("{:.2f}".format(jogador[1]))
        break

print("ALTURA MÉDIA DO TIME")
print("{:.2f}".format(media_altura))
print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
for jogador in superiores_media:
    print(jogador[0])
    print("{:.2f}".format(jogador[1]))
