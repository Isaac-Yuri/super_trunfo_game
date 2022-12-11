from random import randint

def gera_valores(): 
    """
    Retorna os valores das características das cartas
    """
    ninjutsu = randint(1, 20) * 5 
    genjutsu = randint(1, 20) * 5
    taijutsu = randint(1, 20) * 5
    atributos = [ninjutsu, genjutsu, taijutsu] #Os valores dos atributos das cartas são adicionados nesta lista
    return atributos


def gera_baralho(personagens): 
    """
    Retorna o baralho
    parâmetro:
        a lista dos personagens:
            Para que suas cartas sejam formadas
    """
    baralho = []
    for cartas in range(len(personagens)):
        atributos_carta = gera_valores() #Usamos a função anterior para gerar os atributos
        carta = [personagens[cartas],atributos_carta[0], atributos_carta[1], atributos_carta[2]] #Faz com que o personagem receba seus atributos, gerando uma carta
        baralho.append(carta) #Na lista do baralho é adicionado a carta que é uma sub-lista
    return baralho


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
    