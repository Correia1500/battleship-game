def cria_mapa(x):
    l = []
    for i in range(x):
        l.append([])
        
    for j in range(x):
            for k in range(x):
                l[j].append(' ')
    print(l)
x = 3
print(cria_mapa(x))

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

# m = [
#     [' ', ' ', ' ', 'N'],
#     [' ', ' ', ' ', 'N'],
#     ['N', 'N', ' ', 'N'],
#     [' ', ' ', ' ', ' ']
# ]

# b = 2

# l = 1

# c = 0

# o = 'v'

# print(posicao_suporta(m,b,l,c,o))
