import random

numeros = list(range(1, 61))  # cria uma lista de números de 1 a 60

while True:
    print("Loteria \n 1. Imprimir 6 números aleatórios \n 0. Sair: ")
    escolha = input("Escolha uma opção: ")
    if escolha == "0":
        break
    elif escolha == "1":
        numeros_aleatorios = random.sample(numeros, 6)  # seleciona 6 números aleatórios da lista
        print(" | ".join(map(str, numeros_aleatorios)))  # imprime os 6 números separados por " | "
    else:
        print("Opção inválida. Tente novamente.")