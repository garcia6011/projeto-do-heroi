while True:
    # Solicitar ao usuário o nome e a quantidade de experiência (XP) do herói
    nome = input("Digite o nome do Herói: ")
    xp = int(input("Digite a quantidade de experiência (XP) do Herói: "))

    # Utilizar estruturas de decisão para determinar o nível do herói
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 6001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # Exibir a mensagem com o nome e o nível do herói
    print(f"O Herói de nome {nome} está no nível de {nivel}")

    # Perguntar ao usuário se deseja classificar outro herói
    resposta = input("Deseja classificar outro herói? (S para Sim, qualquer outra tecla para sair): ")
    if resposta.upper() != "S":
        break