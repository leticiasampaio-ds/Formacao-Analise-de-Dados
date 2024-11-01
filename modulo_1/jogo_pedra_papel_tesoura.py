# Criar um jogo de Pedra-Papel-Tesoura
# Regras do jogo:
# Pedra ganha da Tesoura
# Tesoura ganha do Papel
# Papel ganha da Pedra

# O que meu programa vai fazer:
# 1. Usuário vai falar se é: pedra, papel ou tesoura (input)
entrada_usuario = input("Escolha sua arma: ")
# Verificar entrada
possibilidades = ["pedra", "papel", "tesoura"]
verificacao = entrada_usuario in possibilidades

if verificacao == True:
    # 2. Random.
    import random
    resultado_da_maquina = random.choice(possibilidades)
    # 3. Ver quem ganha (Condicional - If, Elif, Else)
    # 4. Mostra o resultado (print())
    if entrada_usuario == "pedra" and resultado_da_maquina == "tesoura":
        print(f"Usuário: {entrada_usuario}")
        print(f"Robo: {resultado_da_maquina}")
        print("Você ganhou!")
    elif entrada_usuario == "tesoura" and resultado_da_maquina == "papel":
        print(f"Usuário: {entrada_usuario}")
        print(f"Robo: {resultado_da_maquina}")
        print("Você ganhou!")
    elif entrada_usuario == "papel" and resultado_da_maquina == "pedra":
        print(f"Usuário: {entrada_usuario}")
        print(f"Robo: {resultado_da_maquina}")
        print("Você ganhou!")
    elif entrada_usuario == resultado_da_maquina:
        print(f"Usuário: {entrada_usuario}")
        print(f"Robo: {resultado_da_maquina}")
        print("Foi empate!")
    else:
        print(f"Usuário: {entrada_usuario}")
        print(f"Robo: {resultado_da_maquina}")
        print("Você perdeu!")

else:
    print("Sua entrada está incorreta.")