populacao_a = int(input("Insira a população dao país A: "))
populacao_b = int(input("Insira a população da país B: "))

if populacao_a < populacao_b:
    populacao_a, populacao_b = populacao_b, populacao_a

taxa_a = 0.02
taxa_b = 0.03
anos = 0

while populacao_b <= populacao_a:
    populacao_a *= 1 + taxa_a
    populacao_b *= 1 + taxa_b
    anos += 1

print(f"Levará {anos} anos para a população do país B ultrapassar a do país A")
