from bibliotecas import bib_funcionalidades
from bibliotecas import bib_menus
from time import sleep
#interface inicial
condicao = True
while(condicao):
    bib_menus.menu_inicial()
    menu_opcao = str(input(">")).strip().lower()[0]

    bib_funcionalidades.limpa_tela()

    if(menu_opcao == "2"):#para ver as regras
        bib_menus.menu_regras()
        x = input(">")#só para parar o o fluxo do código

        bib_funcionalidades.limpa_tela()

    else:#para sair da interface inicial
        condicao = False

baralho = [["SAMUEL", 99, 99, 99], ["SAMUEL", 99, 99, 99], ["SAMUEL", 99, 99, 99], ["SAMUEL", 99, 99, 99]]
bib_menus.menu_combate_jogador_1(baralho,100,100)
input("Oque vc deseja fazer?: ")
sleep(10)
#inicio do jogo


cont_partida = 0
vez = 1
while(cont_partida <= 4):
    
    if(vez % 2 != 0):#vez do jogador um
        bib_menus.menu_vez_jogador_1()
        bib_funcionalidades.limpa_tela()


    else:#vez do jogador dois
        bib_menus.menu_vez_jogador_2()
        bib_funcionalidades.limpa_tela()


    vez += 1
