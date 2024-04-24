from navio-pode-ser-alocado
import random
def aloca_navios(m,x):
    n = len(m) 
    for i in x:#3,2
        o = random.choice(['h', 'v'])
        l = random.randint(0, n-1) 
        c = random.randint(0, n-1)
        if o == 'v':
            for a in range(i): #0,1,2
                if l+a >= len(m):
                    l = random.randint(0, n-1)
                elif m[l+i][c] == 'N':
                    l = random.randint(0, n-1) 
                else:
                    m[l+i][c] = 'N'
        elif o == 'h':
            for b in range(i):
                if c+b >= len(m):
                    c = random.randint(0, n-1)
                elif m[l][c+b] == 'N':
                    c = random.randint(0, n-1)    
                else:
                    m[l][c+b] = 'N'
    return m

m = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]
x = [3, 2]

print(aloca_navios(m,x))
