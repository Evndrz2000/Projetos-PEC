def populacao(populacao_inicial):
    populacao_atual = populacao_inicial
    ano = 1600

    while populacao_atual >= 0.1 * populacao_inicial:
        nascidos = populacao_atual * 0.01
        mortes = populacao_atual * 0.06
        populacao_atual = populacao_atual - mortes + nascidos
        print(f"{ano},{nascidos:.0f},{mortes:.0f},{populacao_atual:.0f}")
        ano += 1

populacao_inicial = int(input())
populacao(populacao_inicial)

print("A população total de dodos caiu para menos de 10% da população original.")
