def initPherGrid(n, MAXPHER):
    import numpy as np
    site = np.empty((n+2,n+2))
    
    site[:,0]  = 0 #- Border
    site[:,-1] = 0 #- Border
    site[0, :] = 0 #- Border
    site[-1,:] = 0 #- Border
    
    middle_index = int(n / 2)
    for i in range(1,n+1):
        site[middle_index, i] = MAXPHER * i /n
        
    return site