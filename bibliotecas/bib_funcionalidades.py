import os
from random import choice
from time import sleep


def limpa_tela():
    clear = lambda: os.system('cls')
    clear()


def distribui_cartas(baralho, quantidade_cartas):
    """
    baralho:
        Pilha que se deseja retirar a ou as cartas.
    quantidade_cartas:
        Quantidade de cartas que se deseja retornar do baralho passado como parâmetro.
    """
    cartas_selecionadas = []
    for i in range(quantidade_cartas):
        carta = choice(baralho)#escolhe uma carta
        cartas_selecionadas.append(carta)
        del baralho[baralho.index(carta)]#deleta a carta escolhida
    
    return cartas_selecionadas    


def empilha_cartas(baralho):
    #inverte a ordem das cartas
    for indice in range(len(baralho)):
        #reposiciona a carta
        baralho.insert(indice,baralho[-1])
        #retira o carta reposicionada de onde estava anteriormente
        del baralho[-1]


def caso_empate(baralho, baralho_jogador):
    #para descartar a carta usada
    del baralho_jogador[0]
    #para pegar uma nova carta da pilha
    baralho_jogador.append(baralho[0])
    del baralho[0]

def carta_usada(baralho):
    #para colar a carta usada no fim do baralho
    baralho.append(baralho[0])#coloca na ultima posição
    del baralho[0]#apaga oque ficou na primeira


def calcula_pontos_jogador(pontos_jogador, habilidade_vencedora, habilidade_perdedora, resultado=True): 
    """
    Calcula os pontos do jogador:
        pontos_jogador:
            Os pontos atual do jogador que se quer calcular
        habilidade_vencedora:
            Pontos da característica vencedora da rodada
        habilidade_perdedora:
            Pontos da característica perdedora da rodada
        resultado:
            Se o resultado for True:
                Calcula os pontos do vencedor:
                    Soma-se a diferença aos pontos do vencedor
            Se o resultador não for True:
                Calcula os pontos do perdedor:
                    Subtrai-se a diferença aos pontos do perdedor
    """
    diferenca_habilidade = habilidade_vencedora - habilidade_perdedora #Calcula a diferença entre as habilidades
    if (resultado):
        pontos_vencedor = pontos_jogador + diferenca_habilidade
        return pontos_vencedor
    else:
        pontos_perdedor = pontos_jogador - diferenca_habilidade
        return pontos_perdedor


def cria_jogador(baralho, quantidade_pontos=1000) -> [list(), int()]:
    """
    Parâmetros:
        baralho: Pilha que se deseja retirar as cartas.
        quantidade_pontos: Número de pontos que o jogador vai ter que por padrão é 1000.
    Retorno:
        Retorna uma lista com as cartas e com a quantidade de pontos do jogador 
    """
    cartas_do_jogador = distribui_cartas(baralho, 4)
    return [cartas_do_jogador, quantidade_pontos]
