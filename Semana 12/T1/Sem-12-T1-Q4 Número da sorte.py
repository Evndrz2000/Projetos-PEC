data_nascimento = input("Digite sua data de nascimento, no formato ddmmaaaa: ")
soma_digitos = sum(int(digito) for digito in data_nascimento)
print("Seu número da sorte é:", soma_digitos)
