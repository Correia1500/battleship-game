
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

def aloca_navios(m,x):
    n = len(m) 
    posicao_suporta(m,b,l,c,o)  
        
    def colocar_navio(b,l,c,o):
        if o == 'h':
            for i in range(b):
                m[l][c+i] = 'N'
        else:
            for i in range(b):
                m[l+i][c] = 'N'    
    for b in x:
        alocado = False
        while not alocado:
            l = random.randint(0, n-1)
            c = random.randint(0, n-1)
            o = random.choice(['h', 'v'])
            if posicao_suporta(m,b,l,c,o):
                colocar_navio(b,l,c,o)
                alocado = True
    return m

def foi_derrotado(m):
    for i in m:
        for j in i:
            if j == 'N':
                return False
    return True























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