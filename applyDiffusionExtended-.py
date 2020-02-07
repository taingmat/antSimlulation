import numpy as N

def applySenseExtended(grid): 
    length = len(grid) + 2 
    width =  len(grid[0]) + 2
    border = -2
     
    extendedGrid = N.zeros(length, width)
    
    #Sets top and bottom to be the boundary values
    extendedGrid[0] = border
    extendedGrid[-1] = border
    
    #Sets the sides to be the boundary values
    extendedGrid[:][0] = border
    extendedGrid[:][-1] = border
    
    #Copies the original grid
    extendedGrid[1:-1][1:-1] = grid
    
    