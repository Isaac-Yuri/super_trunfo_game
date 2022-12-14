from bibliotecas.bib_cartas import *
from bibliotecas.bib_funcionalidades import *
from bibliotecas.bib_menus import *
from time import sleep

def jogada(vez_do_jogador):
    if vez_do_jogador == 1:
        menu_combate(baralho_principal, jogador1[-1], jogador2[-1])
        print("Qual opção o jogador 1 escolhe? ")
    else: 
        menu_combate(baralho_principal, jogador1[-1], jogador2[-1])
        print("Qual opção o jogador 2 escolhe? ")
    atributo_escolhido = int(input(">>> "))
    limpa_tela()
    print(f"O nome do personagem do jogador 1 é {jogador1[0][0][0]} e o valor do atributo escolhido dele(a) é: {jogador1[0][0][atributo_escolhido]}")
    print(f"O nome do personagem do jogador 2 é {jogador2[0][0][0]} e o valor do atributo escolhido dele(a) é: {jogador2[0][0][atributo_escolhido]}")

    sleep(1)

    # Se o jogador 1 ganhar entra nesse if
    if jogador1[0][0][atributo_escolhido] > jogador2[0][0][atributo_escolhido]:
        print(f"{jogador1[0][0][0]} ganha de {jogador2[0][0][0]}. Jogador 1 venceu.")
        sleep(1)

        jogador1[-1] = calcula_pontos_jogador(jogador1[-1], jogador1[0][0][atributo_escolhido], jogador2[0][0][atributo_escolhido]) # Soma o atributo vencedor ao vencedor da rodada
        jogador2[-1] = calcula_pontos_jogador(jogador2[-1], jogador1[0][0][atributo_escolhido], jogador2[0][0][atributo_escolhido], resultado=False) # Subtrai a diferença entre os atributos vencedor e perdedor dos pontos do jogador que perdeu

        carta_usada(jogador1[0])
        adicionar_carta_de_outro_baralho(jogador2[0], jogador1[0])


    # Se o jogador 2 ganhar entra nesse elif
    elif jogador2[0][0][atributo_escolhido] > jogador1[0][0][atributo_escolhido]:
        print(f"{jogador2[0][0][0]} ganha de {jogador1[0][0][0]}. Jogador 2 venceu.")
        sleep(1)

        jogador2[-1] = calcula_pontos_jogador(jogador2[-1], jogador2[0][0][atributo_escolhido], jogador1[0][0][atributo_escolhido]) # Soma o atributo vencedor ao vencedor da rodada
        jogador1[-1] = calcula_pontos_jogador(jogador1[-1], jogador2[0][0][atributo_escolhido], jogador1[0][0][atributo_escolhido], resultado=False) # Subtrai a diferença entre os atributos vencedor e perdedor dos pontos do jogador que perdeu

        carta_usada(jogador2[0])
        adicionar_carta_de_outro_baralho(jogador1[0], jogador2[0])

    # Se der empate entra no else
    else:
        print(f"{jogador1[0][0][0]} empata com {jogador2[0][0][0]}")
        sleep(1)
    
    print(len(jogador1[0]), len(jogador2[0]))

while True:
    personagens = ["Naruto", "Sakura", "Sasuke", "Itachi", "Madara", "Obito ", "Hidan ", "Sasori", "Pain  ", "Konan ", "Jiraya", "Yamato", "Gaara ", "Kiba  ", "Hinata", "Choji ", "Neji  ", "Temari", "Asuma ", "Kakuzu"]

    baralho_principal = gera_baralho(personagens)

    jogador1 = cria_jogador(baralho_principal)
    jogador2 = cria_jogador(baralho_principal)


    menu_inicial()

    jogar_ou_ver_regras = int(input(">>> "))
    while jogar_ou_ver_regras not in [1, 2, 3]:
        jogar_ou_ver_regras = int(input(">>> "))

    limpa_tela()

    numero_de_rodadas = 2

    if jogar_ou_ver_regras == 1:

        for i in range(numero_de_rodadas):
            menu_vez_jogador_1()
            sleep(1)
            limpa_tela()
            jogada(1)

            sleep(1.5)
            limpa_tela()

            menu_vez_jogador_2()
            sleep(1)
            jogada(2)
            sleep(1.5)

            limpa_tela()
        
        if jogador1[-1] > jogador2[-1]:
            menu_jogador_1_venceu()
            input()
            limpa_tela()
        elif jogador2[-1] > jogador1[-1]:
            menu_jogador_2_venceu()
            input()
            limpa_tela()
        else:
            menu_empate()
            input()
            limpa_tela()

    elif jogar_ou_ver_regras == 2:
        menu_regras()
        input()
        limpa_tela()

    else:
        break