km_corridos = 10.5 #float
km_corridos_concorrente = 12 # int
nome_da_corrida = "Corrida IWTraining" # str
duracao_da_corrida = [3.5, 3] # list
ganhei_a_corrida = False # bool
paradas = {"praça": 5, "em frente a igreja": 3.5} # Chave:Valor (dict)

# Condicionais (If, Elif, Else)
for item in range(1,10):
    if item == 5:
        print(f'meu numero é {item}')
    elif item / 2 == 4:
        print(f'resultado da divsao por 2 é 4: item - {item}')
    else:
        print(f'é o que sobrou {item}')