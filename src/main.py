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

###########posiciona o computador###########

m = 10 #tamanho do mapa

#sorteia um pais para o comp

pais_comp = random.choice(['Brasil', 'França', 'Austrália', 'Rússia', 'Japão'])

#lista do tamanho das embarcações
x =  []
cria_mapa(m) ##retorna matriz 10x10
aloca_navios(m,x) #recebe uma matriz e uma lista, posicionando os navios.

dic_pais = {1: 'Brasil', 2: 'França', 3: 'Austrália', 4: 'Rússia', 5: 'Japão'}
############################################










from constantes import paises

dic_pais = {1: 'Brasil', 2: 'França', 3: 'Austrália', 4: 'Rússia', 5: 'Japão'}
nacao = int(input("Qual o número da nação da sua frota? ")) 
dic_pais[nacao]
print(f'Você escolheu a nação {dic_pais[nacao]}')
print("Aloque seus Navios e Prepare-se para a Guerra!")
print(paises[dic_pais[nacao]])


m = 10
print(cria_mapa(m))

aloca_navios(m,paises[dic_pais[nacao[0]]])






music_thread.join()