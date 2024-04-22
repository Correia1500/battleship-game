# Lógica central do jogo
def cria_mapa (n):
    mq=[]
    l1=[]
    for a in range (n):
        l1.append(' ')

    for a in range (n):
        mq.append(l1)

    return mq