'''
KEY:
0   EMPTY   Empty ground containing no ant
1   NORTH   Ant about to move to or just moved from the north
2   EAST    Ant about to move to or just moved from the east
3   SOUTH   Ant about to move to or just moved from the south
4   WEST    Ant about to move to or just moved from the west
5   STAY    Ant about to stay in or did not move from the current site
6   BORDER  Border


RULES:
7. For a cell that remains empty, the amount of chemical decrements by a constant amount, EVAPORATE, but does not fall below 0. Thus, the new amount is the maximum of 0 and the current amount minus EVAPORATE.
8. An ant facing in a certain direction will move into that neighboring cell as long as no other ant has already moved there.
9. Otherwise, the ant will stay in its current cell.
10. If an ant leaves a cell that has pheromone above a certain threshold,
THRESHOLD, the amount of chemical increments by a set amount, DE-
POSIT, to reinforce the trail.
11. If an ant stays in a cell, the amount of chemical remains the same.
12. After moving to a new location, the ant faces towards the cell from which
the animal just came.
'''

import math

#Pheromone levels will range between 0(lowest) and 1 (highest)
EVAPORATE = 0.1
EMPTY = 0  
NORTH = 1  
EAST = 2 
SOUTH = 3
WEST = 4    
STAY = 5    
BORDER = 6
THRESHOLD = 0.3
DEPOSIT = 0.1

def walk(antGrid, pherGrid):
    n = len(antGrid) - 2
    newAntGrid = antGrid
    newPherGrid = pherGrid
    for i in range(n):  # i = rows
        for j in range(n):  # j = columns
            if(antGrid[i][j] == EMPTY):
                newPherGrid[i][j] = max(0, (newPherGrid[i][j] - EVAPORATE))
            
            #NORTH
            if (antGrid[i][j] = NORTH):
                if(newAntGrid[i - 1][j] == EMPTY):
                    if(newPherGrid[i][j] > THRESHOLD):
                        newPherGrid[i][j] = newPherGrid[i][j] + DEPOSIT
                    newAntGrid[i][j] = EMPTY
                    newAntGrid[i - 1][j] = SOUTH
                else:
                    newAntGrid(i, j) ← STAY

            #SOUTH
            if (antGrid[i][j] = NORTH):
                if(newAntGrid[i - 1][j] == EMPTY):
                    if(newPherGrid[i][j] > THRESHOLD):
                        newPherGrid[i][j] = newPherGrid[i][j] + DEPOSIT
                    newAntGrid[i][j] = EMPTY
                    newAntGrid[i - 1][j] = SOUTH
                else:
                    newAntGrid(i, j) ← STAY



# n ← number of rows/columns in ant/pheromone grid minus 2 
# newAntGrid ← antGrid
# newPherGrid ← pherGrid
# for i going through each internal row index, do the following:
#     for j going through each internal column index, do the following: 
#         if antGrid(i, j) is EMPTY // Rule 7
#             newPherGrid(i, j) ← maximum of 0 and 
#                 (newPherGrid(i, j) – EVAPORATE)
# // Corresponding segments to the following occur for each direction: 
# if antGrid(i, j) is NORTH
#     if newAntGrid(i – 1, j) is EMPTY
#         if newPherGrid(i, j) > THRESHOLD // Rule 10
#             newPherGrid(i, j) ← newPherGrid(i, j) + DEPOSIT
#         newAntGrid(i, j) ← EMPTY // Rule 8

#         newAntGrid(i - 1, j) ← SOUTH // Rule 12 
#     else
# newAntGrid(i, j) ← STAY // Rules 9 and 11 
# // Corresponding segments for directions EAST, SOUTH, WEST go 
# // here
# return newAntGrid and newPherGrid