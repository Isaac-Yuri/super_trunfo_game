from bibliotecas.bib_cartas import *
from bibliotecas.bib_funcionalidades import *

personagens = ["Naruto", "Sakura", "Sasuke", "Itachi", "Madara", "Obito ", "Hidan ", "Sasori", "Pain  ", "Konan ", "Jiraya", "Yamato", "Gaara ", "Kiba  ", "Hinata", "Choji ", "Neji  ", "Temari", "Asuma ", "Kakuzu"]

baralho_principal = gera_baralho(personagens)

jogador1 = cria_jogador(baralho_principal)
jogador2 = cria_jogador(baralho_principal)


