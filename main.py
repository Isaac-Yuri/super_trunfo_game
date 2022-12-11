from bibliotecas.bib_cartas import *
from bibliotecas.bib_funcionalidades import *
from bibliotecas.bib_menus import *

personagens = ["Naruto", "Sakura", "Sasuke", "Itachi", "Madara", "Obito ", "Hidan ", "Sasori", "Pain  ", "Konan ", "Jiraya", "Yamato", "Gaara ", "Kiba  ", "Hinata", "Choji ", "Neji  ", "Temari", "Asuma ", "Kakuzu"]

baralho_principal = gera_baralho(personagens)

jogador1 = cria_jogador(baralho_principal)
jogador2 = cria_jogador(baralho_principal)

numero_de_rodadas = 2

menu_inicial()

jogar_ou_ver_regras = int(input(">>> "))
while jogar_ou_ver_regras not in [1, 2]:
    jogar_ou_ver_regras = int(input(">>> "))

limpa_tela()

if jogar_ou_ver_regras == 1:
    menu_vez_jogador_1()
    limpa_tela()
    menu_combate(baralho_principal, jogador1[-1], jogador2[-1])
else:
    menu_regras()
    input()