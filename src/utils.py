from constantes import *
def cria_mapa(x):
    m = []
    for i in range(x):
        m.append([])
        
    for j in range(x):
            for k in range(x):
                m[j].append(' ')
            
    return m

def posicao_suporta(m,b,l,c,o):    
    if o == 'v':
        for i in range(b): #0,1
            if l+i >= len(m):
                return False
            elif m[l+i][c] == 'N':
                return False
    elif o == 'h':
        for j in range(b):
            if c+j >= len(m):
                return False
            elif m[l][c+j] == 'N':
                return False    
    return True


import random


def lis_blocos (PAISES, CONFIGURACAO, p):
    lnb=[]
    for a in PAISES[p]:
        if PAISES[p]==1:
            lnb.append(CONFIGURACAO[a])
        else:
            for i in range (PAISES[p][a]):
                lnb.append(CONFIGURACAO[a])

    return lnb


def aloca_navios (m, lnb):
    n=len(m)
    l= random.randint(0, n-1)
    c= random.randint(0, n-1)
    o= random.choice(['h', 'v'])
    
    for nb in lnb:
        def posicao_suporta(m, nb, l, c, o):
            if m[l][c]!=' ':
                return False 
            if o== 'v':
                i=1
                while i<nb:
                    if (l+i)>= len(m) or m[l+i][c]!=' ':
                        return False
                    i+=1
            if o=='h':
                j=1
                while j<nb:
                    if (c+j)>= len(m[0]) or m[l][c+j]!=' ':
                        return False
                    j+=1
            return True
        if posicao_suporta(m, nb, l, c, o)== False:
            while posicao_suporta(m, nb, l, c, o)==False:
                l= random.randint(0, n-1)
                c= random.randint(0, n-1)
                o= random.choice(['h', 'v'])
                posicao_suporta(m, nb, l, c, o)
        if posicao_suporta(m, nb, l, c, o)== True:
            for a in range (nb):
                if o== 'v':
                    m[l+a][c]='N'
                elif o=='h':
                    m[l][c+a]='N'



    return m


def foi_derrotado(m):
    for i in m:
        for j in i:
            if j == 'N':
                return False
    return True



def aloca_navios_j (mj, lbj, fp):
    for i in mj:
        print(i)
    for nb in lbj:
        print (f'alocar a frota {fp[0]}({CONFIGURACAO[fp[0]]} blocos)')
        del fp[0]
        l1=input('escolha letra:') #letra escolhida (coluna)
        l=l1.upper()
        lln={'A':0, 'B':1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9} #lista de letra pra numero
        c=lln[l] #letra escolhida em numero(indice da coluna)
        li=int(input ('escolha o numero:'))-1  #numero escolhido pelo jogador(indice da linha)
        
        o = input('escolha orientação[v/h]: ') #orientação escolhida
        for k in range (nb):

            if o== 'v':
                mj[li+k][c]='N'
            elif o=='h':
                mj[li][c+k]='N'

        for i in mj:
            print(i)

    return 'tropas posicionadas'

def disparo_computador (mj):
    n=len(mj)
    l= random.randint(0, n-1)
    c= random.randint(0, n-1)
    lnl={0:'A', 1:'B', 2: 'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'} #lista de numero pra letra
    lm= (l+1) #linha para mostrar ao jogador 
    cm= lnl[c]#coluna para mostrar ao jogador
    
    while mj[l][c] == ' ' or 'N':
        if mj[l][c]== ' ':
            mj[l][c]='A'
            break
        elif mj[l][c]=='N':
            mj[l][c]='D'
            break
        elif mj[l][c]=='D':
            l= random.randint(0, n-1)
            c= random.randint(0, n-1)

    print (f'computador disparou em {cm}{lm}')
    return mj

def imprime_matriz(m):
    n=len(m)
    print()
    for l in range (n):
        texto=f'{l} '
        for c in range (n):
            texto+=m[l][c]
        print(texto)


def disparo_jogador(mc):
    print('Cordenadas de seu disparo: ')
    l1=input('escolha letra:') #letra escolhida (coluna)
    l=l1.upper()
    lln={'A':0, 'B':1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9} #lista de letra pra numero
    c=lln[l] #letra escolhida em numero(indice da coluna)
    li=int(input ('escolha o numero:'))-1  #numero escolhido pelo jogador(indice da linha)

    if mc[li][c]=='N':
        mc[li][c]='D'
    elif mc[li][c]==' ':
        mc[li][c]='A'

    return mc




















# import random
# def aloca_navios (m, lnb): #####para usar tem que importar o random
#     n=len(m)
#     l= random.randint(0, n-1)
#     c= random.randint(0, n-1)
#     o= random.choice(['h', 'v'])
    
#     for nb in lnb:
#         def posicao_suporta(m, nb, l, c, o):
#             if m[l][c]!=' ':
#                 return False 
#             if o== 'v':
#                 i=1
#                 while i<nb:
#                     if (l+i)>= len(m) or m[l+i][c]!=' ':
#                         return False
#                     i+=1
#             if o=='h':
#                 j=1
#                 while j<nb:
#                     if (c+j)>= len(m[0]) or m[l][c+j]!=' ':
#                         return False
#                     j+=1
#             return True
#         if posicao_suporta(m, nb, l, c, o)== False:
#             while posicao_suporta(m, nb, l, c, o)==False:
#                 l= random.randint(0, n-1)
#                 c= random.randint(0, n-1)
#                 o= random.choice(['h', 'v'])
#                 posicao_suporta(m, nb, l, c, o)
#         if posicao_suporta(m, nb, l, c, o)== True:
#             for a in range (nb):
#                 if o== 'v':
#                     m[l+a][c]='N'
#                 elif o=='h':
#                     m[l][c+a]='N'
#     return m


# def  foi_derrotado(m):
#     for a in range (len(m)):
#         if 'N' in m[a]:
#             return False    
#     return True