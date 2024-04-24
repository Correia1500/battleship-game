#BIBLIOTECAS
import random
import threading
from playsound import playsound #pip install playsound ##para baixar

##cores
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebraco': '\033[7;30m',
         }

# Função para tocar o som
def musica_fundo():
    playsound("docs/march-of-the-templars-globus-preliator.mp3")

# Iniciar a thread de música
music_thread = threading.Thread(target=musica_fundo)
music_thread.start()


print(f"{cores['vermelho']} ==================================={cores['limpa']}")
print(f"{cores['vermelho']}|{cores['limpa']} {cores['verde']}Bem-vindos a Batalha Naval INSPER{cores['limpa']} {cores['vermelho']}|{cores['limpa']}")
print(f"{cores['vermelho']} ==================================={cores['limpa']}")

