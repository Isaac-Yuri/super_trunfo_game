from random import choice
from time import sleep
import os

def carregando():
    print("Carregando...")
    sleep(1)


def limpa_tela():
    clear = lambda: os.system('cls')
    clear()


def distribui_cartas(baralho):
    baralho_jogador = []
    for indice in range(4):
        carta = choice(baralho)#escolhe uma carta
        baralho_jogador.append(carta)
        del baralho[baralho.index(carta)]#deleta a carta escolhida
    
    return baralho_jogador


def empilha_cartas(baralho):
    #inverte a ordem das cartas
    for indice in range(len(baralho)):
        #reposiciona a carta
        baralho.insert(indice,baralho[-1])
        #retira o carta reposicionada de onde estava anteriormente
        del baralho[-1]


def caso_empate(baralho,baralho_jogador):
    #para descartar a carta usada
    del baralho_jogador[0]
    #para pegar uma nova carta da pilha
    baralho_jogador.append(baralho[0])
    del baralho[0]

def carta_usada(baralho):
    #para colar a carta usada no fim do baralho
    baralho.append(baralho[0])#coloca na ultima posição
    del baralho[0]#apaga oque ficou na primeira
