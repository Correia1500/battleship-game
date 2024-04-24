#BIBLIOTECAS
import random
import threading
from playsound import playsound #pip install playsound ##para baixar
import time #efeito no terminal

##cores
cores = {'limpa': '\033[m',
    'azul': '\033[34m',
    'verde': '\033[32m',
       'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebraco': '\033[7;30m',
         }
time.sleep(1)
# Função para tocar o som
def musica_fundo():
    playsound("docs/march-of-the-templars-globus-preliator.mp3")

# Iniciar a thread de música
music_thread = threading.Thread(target=musica_fundo)
music_thread.start()

delay = 0.4

print(f"{cores['vermelho']} ==================================={cores['limpa']}")
print(f"{cores['vermelho']}|{cores['limpa']} {cores['verde']}Bem-vindos a Batalha Naval INSPER{cores['limpa']} {cores['vermelho']}|{cores['limpa']}")
print(f"{cores['vermelho']} ==================================={cores['limpa']}")
time.sleep(1)

print("Iniciando o Jogo!")
time.sleep(1)

print("Computador está alocando os navios de guerra do país Japão...")
time.sleep(2)

print("Computador já está em posição de batalha!")
time.sleep(2)



print("1: Brasil")
print("                                        1 cruzador")
print("                                        2 torpedeiro")
print("                                        1 destroyer")
print("                                        1 couracado")
print("                                        1 porta-avioes")
time.sleep(1)
print("2: França")
print("                                        3 cruzador")
print("                                        1 porta-avioes")
print("                                        1 destroyer")
print("                                        1 submarino")
print("                                        1 couracado")
print("                                        1 couracado")
time.sleep(1)
print("3: Austrália")
print("                                        3 cruzador")
print("                                        1 submarino")
print("                                        1 porta-avioes")
print("                                        1 torpedeiro")
time.sleep(1)
print("4: Rússia")
print("                                        1 cruzador")
print("                                        1 porta-avioes")
print("                                        2 couracado")
print("                                        1 destroyer")
print("                                        1 submarino")
time.sleep(1)
print("5: Japão")
print("                                        2 torpedeiro")
print("                                        1 cruzador")
print("                                        2 destroyer")
print("                                        1 couracado")
print("                                        1 submarino")
time.sleep(1)
print("Qual o número da nação da sua frota? |")
