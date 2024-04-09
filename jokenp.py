#Crie pelo menos uma função chamada “Jogar" e desenvolva as tarefas abaixo:
#1. Peça ao usuário para escolher entre "Pedra", "Papel" e "Tesoura".
#2. Você deve definir a escolha do computador de forma aleatória também entre "Pedra", "Papel" e "Tesoura". (criar um número aleatório no python)
#3. As escolhas do jogador e do computador devem ser exibidas na tela.
#4. Depois, as escolhas serão comparadas para ver quem ganhou.
#5. O programa deve determinar o vencedor com base nas escolhas feitas, seguindo estas regras:
#a. Pedra ganha de Tesoura, mas perde para Papel.
#b. Papel ganha de Pedra, mas perde para Tesoura.
#c. Tesoura ganha de Papel, mas perde para Pedra.
#d. O jogo vai dizer quem ganhou ou se foi empate.
#6. O programa deve imprimir na tela o vencedor ou se houve empate.
#7. Ao final pergunte se o jogador quer continuar jogando. Se disser "sim", o jogo continuará; se disser "não", o jogo acaba.


import random

def jogar():
    vitorias_jogador = 0
    vitorias_computador = 0
    quantidade_empates = 0

    print("Bem-vindo ao Jokenpo!")

    while True:
        print("Escolha uma opção:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")

        jogador = int(input("Digite sua escolha: "))
        computador = random.randint(1, 3)

        # Mostra a escolha do computador
        opcoes = ["Pedra", "Papel", "Tesoura"]
        print(f"Computador escolheu: {opcoes[computador - 1]}")

        print("JO  KEN  POH! ! !")

        if jogador == computador:
            print("Empate!")
            quantidade_empates += 1
        elif jogador == 1:
            if computador == 2:
                print("Você perdeu. Papel embrulha Pedra")
                vitorias_computador += 1
            else:
                print("Você ganhou. Pedra amassa Tesoura")
                vitorias_jogador += 1
        elif jogador == 2:
            if computador == 3:
                print("Você perdeu. Tesoura corta Papel")
                vitorias_computador += 1
            else:
                print("Você ganhou. Papel embrulha Pedra")
                vitorias_jogador += 1
        elif jogador == 3:
            if computador == 1:
                print("Você perdeu. Pedra quebra Tesoura")
                vitorias_computador += 1
            else:
                print("Você ganhou. Tesoura corta Papel")
                vitorias_jogador += 1
        else:
            print("Jogada inválida. Escolha uma opção válida.")

        continuar = input("Deseja jogar novamente? (s/n): ")
        if continuar.lower() != "s":
            break

    print("Total de vitórias do jogador:", vitorias_jogador)
    print("Total de vitórias do computador:", vitorias_computador)
    print("Total de empates:", quantidade_empates)

jogar()
