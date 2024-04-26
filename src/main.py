#BIBLIOTECAS
import random
import threading
from playsound import playsound #pip install playsound ##para baixar
import time #efeito no terminal
#funcoes
from utils import *
##cores
from constantes import *
time.sleep(1)
# Função para tocar o som
def musica_fundo():
    playsound("docs/march-of-the-templars-globus-preliator.mp3")

# Iniciar a thread de música
music_thread = threading.Thread(target=musica_fundo)
music_thread.start()

delay = 0.4

print(f"{CORES['red']} ===============xxx================={CORES['reset']}")
print(f"{CORES['red']}|{CORES['reset']} {CORES['green']}Bem-vindos a Batalha Naval INSPER{CORES['reset']} {CORES['red']}|{CORES['reset']}")
print(f"{CORES['red']} ===============xxx================={CORES['reset']}")
time.sleep(delay)

tempo = input('Quer pular a animação ?[S/N]')
if tempo == "S":
    delay = 0.1
else:
    delay = 2

print("Iniciando o Jogo!")
time.sleep(delay)

pc= random.choice(['Brasil', 'França', 'Austrália', 'Rússia', 'Japão'])

print(f"Computador está alocando os navios de guerra do país {pc}")
time.sleep(delay)

print("Computador já está em posição de batalha!")
time.sleep(delay)

mj=( cria_mapa (10)) #mapa do jogador
mc=( cria_mapa (10)) #mapa do computador
    
lbc = lis_blocos (PAISES, CONFIGURACAO, pc) #lista do numero de blocos do computador

mi = aloca_navios(mc,lbc) #mapa inicial computador

#print(lbc) #lista que sera usada pela funcao aloca_navios

# for i in mi: #imprime de forma legivel
#     print(i)

###Imprime os paises para a escolha
print("1: Brasil")
print("                                        1 cruzador")
print("                                        2 torpedeiro")
print("                                        1 destroyer")
print("                                        1 couracado")
print("                                        1 porta-avioes")
time.sleep(delay)
print("2: França")
print("                                        3 cruzador")
print("                                        1 porta-avioes")
print("                                        1 destroyer")
print("                                        1 submarino")
print("                                        1 couracado")
time.sleep(delay)
print("3: Austrália")
print("                                        1 couracado")
print("                                        3 cruzador")
print("                                        1 submarino")
print("                                        1 porta-avioes")
print("                                        1 torpedeiro")
time.sleep(delay)
print("4: Rússia")
print("                                        1 cruzador")
print("                                        1 porta-avioes")
print("                                        2 couracado")
print("                                        1 destroyer")
print("                                        1 submarino")
time.sleep(delay)
print("5: Japão")
print("                                        2 torpedeiro")
print("                                        1 cruzador")
print("                                        2 destroyer")
print("                                        1 couracado")
print("                                        1 submarino")
time.sleep(delay)

pj= int(input('Qual o número da sua frota? ')) #pais do jogador

fp=[] #frota do pais 
lbj=[] #lista numero de blocos do jogador
disc_paises = {1:'Brasil',2:'França',3:'Austrália',4:'Rússia',5:'Japão'}

for a in disc_paises.keys():
    if pj == a:
        
        fp.append(PAISES[disc_paises[a.items()])

print(fp)

# for a in PAISES[pj]:
#     for b in range(PAISES[pj][a]):
#         fp.append(a)
#         lbj.append(CONFIGURACAO[a])

#print(fp)

# for a in range (len(fp)):
#     print (f'alocar a frota {fp[0]}({CONFIGURACAO[fp[0]]} blocos)')
#     l=input('escolhaa letra:') #letra escolhida (coluna)
#     lln={'A':0, 'B':1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9} #lista de letra pra numero
#     c=lln[l] #letra escolhida em numero(indice da coluna)
#     li=int(input ('escolha o numero:'))-1  #numero escolhido pelo jogador(indice da linha)
#     o= input('escolha orientação[v/h]: ') #orientação escolhida