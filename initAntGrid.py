def initAntGrid(n, probAnt):
    import numpy as np
    site = np.empty((n+2,n+2))
    direction = [1,2,3,4] # N, E, S, W
    
    site[:,0] = 6 #- Border
    site[:,-1] = 6 #- Border
    site[0, :] = 6 #- Border
    site[-1,:] = 6 #- Border
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            chance = np.random.rand()
            if chance > probAnt:
                site[i,j] = direction[np.random.randint(0,4)]
    
    return site