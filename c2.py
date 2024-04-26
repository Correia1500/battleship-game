import random

print ('batalha naval')
pc = random.choice(['Brasil', 'França', 'Austrália', 'Rússia', 'Japão'])


print (f'computador esta alocando seus navios da frota do pais {pc}')
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

def cria_mapa (n):
    mq=[]
    l1=[]
    for a in range (n):
        l1.append(' ')

    for a in range (n):
        mq.append(l1)

    return mq

mj=( cria_mapa (10))
mc=( cria_mapa (10))

lnb=[]

def lis_blocos (PAISES, CONFIGURACAO, p):
    for a in PAISES[p]:
        lnb.append(PAISES[p][a]*CONFIGURACAO[a])

    return lnb
lbc=lis_blocos (PAISES, CONFIGURACAO, pc)

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


mi= aloca_navios(mc,lbc)

print(mi)


print(f'escolha um pais para jogar: {PAISES}')
pj= input('pais escolhido? ')
lbj=[]
fp=[]
for a in PAISES[pj]:
    for b in range(PAISES[pj][a]):
        fp.append(a)
        lbj.append(CONFIGURACAO[a])
    

print(fp)

for a in range (len(fp)):
    print (f'alocar a frota {fp[0]}({CONFIGURACAO[fp[0]]} blocos)')
    l=input('escolhaa letra:')
    lln={'A':0, 'B':1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
    ln=lln[l]
    n=input ('escolha o numero:')-1
    o= input('escolha orientação[v/h]: ')