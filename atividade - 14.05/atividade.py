nomes = []
usuários = []

while True:
    usuário = {}

    nome = input("Digite seu nome: ")
    usuário['nome'] = nome
    nomes.append(nome)

    cidade = input("Digite sua cidade: ")
    usuário['cidade'] = cidade

    tem_transporte = input("Você possui algum transporte? (sim/não): ").strip().lower()

    if tem_transporte == 'sim':
        tipo = input("Qual o tipo do transporte? ")
        modelo = input("Qual a marca do transporte? ")
        placa = input("Qual a placa do transporte? ")

        usuário['Transporte'] = {
            'Tipo': tipo,
            'Modelo': modelo,
            'Placa': placa
        }
    else:
        usuário['Transporte'] = None

    usuários.append(usuário)

    continuar = input("Deseja cadastrar outro usuário? (sim/não): ").strip().lower()
    if continuar == 'não':
        break

print("\nUsuários:")
for usuário in usuários:
    print([usuário]) 