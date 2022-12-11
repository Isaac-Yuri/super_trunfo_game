from time import sleep
import os


def menu_inicial():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}
    
                     _______. __    __   __  .______   .______    __    __   _______   _______ .__   __.      
                    /       ||  |  |  | |  | |   _  \  |   _  \  |  |  |  | |       \ |   ____||  \ |  |     
                   |   (----`|  |__|  | |  | |  |_)  | |  |_)  | |  |  |  | |  .--.  ||  |__   |   \|  |
                    \   \    |   __   | |  | |   ___/  |   ___/  |  |  |  | |  |  |  ||   __|  |  . `  |
                .----)   |   |  |  |  | |  | |  |      |  |      |  `--'  | |  '--'  ||  |____ |  |\   |
                |_______/    |__|  |__| |__| | _|      | _|       \______/  |_______/ |_______||__| \__| 
                                                
                            .___________..______   __    __  .__   __.  _______   ______
                            |           ||   _  \ |  |  |  | |  \ |  | |   ____| /  __  \                                  
                            `---|  |----`|  |_)  ||  |  |  | |   \|  | |  |__   |  |  |  | 
                                |  |     |      / |  |  |  | |  . `  | |   __|  |  |  |  |
                                |  |     |  |\  \ |  `--'  | |  |\   | |  |     |  `--'  |
                                |__|     | _| `.__|\______/  |__| \__| |__|      \______/ 



                                        Aperte [1] para jogar 
                                        Aperte [2] para ver as regras

{"=" * largura_terminal}""")


def menu_regras():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * 180}


        Os jogadores começam a partida com 1000 pontos.
        Cada jogador receberá 4 cartas de 20 do baralho.
        Ao todo, serão 4 rodadas e, em caso de empate, uma quinta rodada será realizada como desempate.
        O jogador que tiver a vez deverá escolher um dos 3 atributos (ninjutsu, genjutsu e taijutsu) para desafiar o adversário.
        O vencedor terá a diferença entre os valores das habilidades desafiadas acrescidas em seu contador de pontos.
        O perdedor, por sua vez, terá debitada a diferença entre as habilidades desafiadas do seu contador de pontos.
        Em caso de empate, a rodada é anulada e uma próxima é realizada.
        Vence o jogador com maior quantidade de pontos.
        Divirta-se e boa sorte no nosso Trunfo-Shippuden!
            
                            Pressione Enter para voltar


{"=" * 180}""")


def menu_vez_jogador_1():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}
                
                                   ____    ____  _______  ________  
                                   \   \  /   / |   ____||       /  
                                    \   \/   /  |  |__   `---/  /   
                                     \      /   |   __|     /  /    
                                      \    /    |  |____   /  /____. 
                                       \__/     |_______| /________|

 _______   ______             __    ______     _______      ___       _______   ______   .______        __  
|       \ /  __  \           |  |  /  __  \   /  _____|    /   \     |       \ /  __  \  |   _  \      /_ | 
|  .--.  |  |  |  |          |  | |  |  |  | |  |  __     /  ^  \    |  .--.  |  |  |  | |  |_)  |      | | 
|  |  |  |  |  |  |    .--.  |  | |  |  |  | |  | |_ |   /  /_\  \   |  |  |  |  |  |  | |      /       | | 
|  '--'  |  `--'  |    |  `--'  | |  `--'  | |  |__| |  /  _____  \  |  '--'  |  `--'  | |  |\  \.      | | 
|_______/ \______/      \______/   \______/   \______| /__/     \__\ |_______/ \______/  | _| `._|      |_| 
                                    

{"=" * largura_terminal}""")
    sleep(0.8)

def menu_vez_jogador_2():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}
                
                                   ____    ____  _______  ________  
                                   \   \  /   / |   ____||       /  
                                    \   \/   /  |  |__   `---/  /   
                                     \      /   |   __|     /  /    
                                      \    /    |  |____   /  /____. 
                                       \__/     |_______| /________|
                                                                                                       
 _______   ______             __    ______     _______      ___       _______   ______   .______      ___  
|       \ /  __  \           |  |  /  __  \   /  _____|    /   \     |       \ /  __  \  |   _  \    |__ \   
|  .--.  |  |  |  |          |  | |  |  |  | |  |  __     /  ^  \    |  .--.  |  |  |  | |  |_)  |      ) |
|  |  |  |  |  |  |    .--.  |  | |  |  |  | |  | |_ |   /  /_\  \   |  |  |  |  |  |  | |      /      / /
|  '--'  |  `--'  |    |  `--'  | |  `--'  | |  |__| |  /  _____  \  |  '--'  |  `--'  | |  |\  \.    / /_
|_______/ \______/      \______/   \______/   \______| /__/     \__\ |_______/ \______/  | _| `._|   |____|
                                    

{"=" * largura_terminal}""")
    sleep(0.8)


def menu_combate(baralho,pontos_jogador_1,pontos_jogador_2):
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}                                                                                                     
             Pontos do jogador um: {pontos_jogador_1}       Pontos do jogador dois: {pontos_jogador_2}      
     ________________ ________________ ________________ ________________ 
    |                |                |                |                |
    |                |                |                |                |
    |                |                |                |                |                
    |                |                |                |                |
    |                |                |                |                |
    |                |                |                |                |
    |                |                |                |                |
    |                |                |                |                |
    |________________|________________|________________|                |
                                                       |                |
                                 _______               |________________|              
                                |       |         
                                |       |
                                |       |   
                                |_______|
                                |_______|                                                                                                                                                                                 
     ________________           
    |                |          
    |                |________________ ________________ ________________
    |    {baralho[0][0]}      |    {baralho[1][0]}      |    {baralho[2][0]}      |    {baralho[3][0]}      |
    |________________|________________|________________|________________|
    |ninjutsu: {baralho[0][1]}    |ninjutsu: {baralho[1][1]}    |ninjutsu: {baralho[2][1]}    |ninjutsu: {baralho[3][1]}    |                
    |                |                |                |                |
    |genjutsu: {baralho[0][2]}    |genjutsu: {baralho[1][2]}    |genjutsu: {baralho[2][2]}    |genjutsu: {baralho[3][2]}    |
    |                |                |                |                |
    |taijutsu: {baralho[0][3]}    |taijutsu: {baralho[1][3]}    |taijutsu: {baralho[2][3]}    |taijutsu: {baralho[3][3]}    |
    |________________|________________|________________|________________|
{"=" * largura_terminal}
[1]-Usar Ninjutsu
[2]-Usar Genjutsu
[3]-Usar Taijutsu""")    


def menu_jogador_1_venceu():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}
    
               __    ______     _______      ___       _______   ______   .______        
              |  |  /  __  \   /  _____|    /   \     |       \ /  __  \  |   _  \       
              |  | |  |  |  | |  |  __     /  ^  \    |  .--.  |  |  |  | |  |_)  |      
        .--.  |  | |  |  |  | |  | |_ |   /  /_\  \   |  |  |  |  |  |  | |      /       
        |  `--'  | |  `--'  | |  |__| |  /  _____  \  |  '--'  |  `--'  | |  |\  \.  
         \______/   \______/   \______| /__/     \__\ |_______/ \______/  | _| `._|  
    
          __       _______      ___      .__   __.  __    __    ______    __    __  
         /_ |     /  _____|    /   \     |  \ |  | |  |  |  |  /  __  \  |  |  |  | 
          | |    |  |  __     /  ^  \    |   \|  | |  |__|  | |  |  |  | |  |  |  | 
          | |    |  | |_ |   /  /_\  \   |  . `  | |   __   | |  |  |  | |  |  |  | 
          | |    |  |__| |  /  _____  \  |  |\   | |  |  |  | |  `--'  | |  `--'  | 
          |_|     \______| /__/     \__\ |__| \__| |__|  |__|  \______/   \______/                                                            
    
    
{"=" * largura_terminal}""")


def menu_jogador_2_venceu():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}

               __    ______     _______      ___       _______   ______   .______      
              |  |  /  __  \   /  _____|    /   \     |       \ /  __  \  |   _  \     
              |  | |  |  |  | |  |  __     /  ^  \    |  .--.  |  |  |  | |  |_)  |    
        .--.  |  | |  |  |  | |  | |_ |   /  /_\  \   |  |  |  |  |  |  | |      /     
        |  `--'  | |  `--'  | |  |__| |  /  _____  \  |  '--'  |  `--'  | |  |\  \.
         \______/   \______/   \______| /__/     \__\ |_______/ \______/  | _| `._|

          ___        _______      ___      .__   __.  __    __    ______    __    __  
         |__ \      /  _____|    /   \     |  \ |  | |  |  |  |  /  __  \  |  |  |  | 
            ) |    |  |  __     /  ^  \    |   \|  | |  |__|  | |  |  |  | |  |  |  | 
           / /     |  | |_ |   /  /_\  \   |  . `  | |   __   | |  |  |  | |  |  |  | 
          / /_     |  |__| |  /  _____  \  |  |\   | |  |  |  | |  `--'  | |  `--'  | 
         |____|     \______| /__/     \__\ |__| \__| |__|  |__|  \______/   \______/                                                                                                                                                                          

        
{"=" * largura_terminal}""")
    

def menu_empate():
    largura_terminal = os.get_terminal_size()[0]
    print(f"""{"=" * largura_terminal}

             _______ .___  ___. .______      ___   .___________. _______ 
            |   ____||   \/   | |   _  \    /   \  |           ||   ____|
            |  |__   |  \  /  | |  |_)  |  /  ^  \ `---|  |----`|  |__   
            |   __|  |  |\/|  | |   ___/  /  /_\  \    |  |     |   __|  
            |  |____ |  |  |  | |  |     /  _____  \   |  |     |  |____ 
            |_______||__|  |__| | _|    /__/     \__\  |__|     |_______|


{"=" * largura_terminal}""")
