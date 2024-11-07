# Criar um programa que converta um valor de KM para M. (N * 1000)
## Regras:
## 1. O usuário vai inserir um número.
## 2. Criar uma função que execute a conversão.
## 3. Apresentar para o usuário o valor convertido.

# Regra 1
input_em_km = input("Insira o valor em KM: ")
input_em_km_int = int(input_em_km)

# Regra 2
def conversao_km_m(n_km):
    resultado_conversao = n_km * 1000
    return resultado_conversao

resultado = conversao_km_m(n_km=input_em_km_int)

# Regra 3
print(f"Esse é seu número em metros: {resultado}")