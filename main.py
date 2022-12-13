from bibliotecas.bib_cartas import *
from bibliotecas.bib_funcionalidades import *
from bibliotecas.bib_menus import *
from time import sleep

def jogada():
    menu_combate(baralho_principal, jogador1[-1], jogador2[-1])
    atributo_escolhido = int(input(">>> "))
    print(f"O nome do personagem do jogador 1 é {jogador1[0][0][0]} e o valor do atributo escolhido dele(a) é: {jogador1[0][0][atributo_escolhido]}")
    print(f"O nome do personagem do jogador 2 é {jogador2[0][0][0]} e o valor do atributo escolhido dele(a) é: {jogador2[0][0][atributo_escolhido]}")

    sleep(1)

    # Se o jogador 1 ganhar entra nesse if
    if jogador1[0][0][atributo_escolhido] > jogador2[0][0][atributo_escolhido]:
        print(f"{jogador1[0][0][0]} ganha de {jogador2[0][0][0]}.")
        sleep(1)

        jogador2[1] = calcula_pontos_jogador(jogador1[1], jogador1[0][0][atributo_escolhido], jogador2[0][0][atributo_escolhido], resultado=False)

        jogador1[1] = calcula_pontos_jogador(jogador1[1], jogador1[0][0][atributo_escolhido], jogador2[0][0][atributo_escolhido])

        print(f"Valor do atributo vencedor {jogador1[0][0][atributo_escolhido]} somado aos pontos do jogador 1, e diferença entre os atributos {jogador1[0][0][atributo_escolhido] - jogador2[0][0][atributo_escolhido]} subtraídos dos pontos do jogador 2.")

    # Se o jogador 2 ganhar entra nesse elif
    elif jogador2[0][0][atributo_escolhido] > jogador1[0][0][atributo_escolhido]:
        print(f"{jogador2[0][0][0]} ganha de {jogador1[0][0][0]}.")
        sleep(1)

        jogador1[1] = calcula_pontos_jogador(jogador2[1], jogador2[0][0][atributo_escolhido], jogador1[0][0][atributo_escolhido], resultado=False)

        jogador2[1] = calcula_pontos_jogador(jogador2[1], jogador2[0][0][atributo_escolhido], jogador1[0][0][atributo_escolhido])

        print(f"Valor do atributo vencedor {jogador2[0][0][atributo_escolhido]} somado aos pontos do jogador 1, e diferença entre os atributos {jogador2[0][0][atributo_escolhido] - jogador1[0][0][atributo_escolhido]} subtraídos dos pontos do jogador 2.")

    # Se der empate entra no else
    else:
        print(f"{jogador1[0][0][0]} empata com {jogador2[0][0][0]}")
        sleep(1)

personagens = ["Naruto", "Sakura", "Sasuke", "Itachi", "Madara", "Obito ", "Hidan ", "Sasori", "Pain  ", "Konan ", "Jiraya", "Yamato", "Gaara ", "Kiba  ", "Hinata", "Choji ", "Neji  ", "Temari", "Asuma ", "Kakuzu"]

baralho_principal = gera_baralho(personagens)

jogador1 = cria_jogador(baralho_principal)
jogador2 = cria_jogador(baralho_principal)


menu_inicial()

jogar_ou_ver_regras = int(input(">>> "))
while jogar_ou_ver_regras not in [1, 2]:
    jogar_ou_ver_regras = int(input(">>> "))

limpa_tela()

numero_de_rodadas = 3
if jogar_ou_ver_regras == 1:

    for i in range(numero_de_rodadas):
        menu_vez_jogador_1()
        sleep(1)
        jogada()
        sleep(1.5)
        menu_vez_jogador_2()
        sleep(1)
        jogada()
        sleep(1.5)
        
else:
    menu_regras()
    input()