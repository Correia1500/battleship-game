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

print("Computador está alocando os navios de guerra do país Japão...")
time.sleep(delay)

print("Computador já está em posição de batalha!")
time.sleep(delay)



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

cria_mapa(n)

mj=( cria_mapa (10))
mc=( cria_mapa (10))

lnb=[] #lista de numero de blocos

lis_blocos (PAISES, CONFIGURACAO, p)
    
lbc = lis_blocos (PAISES, CONFIGURACAO, pc)

aloca_navios (m, lnb)

mi = aloca_navios(mc,lbc)

print(mi)

print(f'escolha um pais para jogar: {PAISES}')
pj= input('pais escolhido? ')

fp=[]
fp =[]
for a in PAISES[pj]:
    for b in range(PAISES[pj][a]):
        fp.append(a)

print(fp)

for a in range(len(fp)):
    print (f'alocar a frota {fp[0]}({CONFIGURACAO[fp[0]]} blocos)')
    l=input('escolhaa letra:')
    lln={'A':0, 'B':1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
    ln=lln[l]
    n=input ('escolha o numero:')-1
    o= input('escolha orientação[v/h]: ')