import numpy as N

def sense(site, na, ea, sa, wa, np, ep, sp, wp):
    north = 1
    east = 2 
    south = 3
    west = 4
    stay = 5 
    
    ants = [na, ea, sa, wa]
    pheremone = [np, ep, sp, wp]
    
    #Rule 2
    if site != stay: 
        pheremone[site - 1] = -2
    
    #Rule 4
    for i in range(4): 
        if ants[i] != 0:
            pheremone[i] = -2
    
    mx = max(pheremone)
    print(pheremone)
    print(mx)
    
    #Rule 6
    if mx < 0: 
        return stay 
    
    #Rule 5
    else: 
        direction = -1
        while direction == -1:
            rand = N.random.randint(4)
            if (pheremone[rand] == mx):
                direction = rand + 1
    return direction

print(sense(3, 0, 0, 1, 1, 1, 1, 1, -2))
    