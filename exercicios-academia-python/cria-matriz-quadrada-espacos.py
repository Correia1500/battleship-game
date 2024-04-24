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
