# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:51:33 2021

@author: M Shoaib
"""

def spirallytraverse(matrix,R,C):
    
    total_int=R*C
    point=0 
    spiral=[] 
    while len(spiral)<total_int:
        #this loops casues the pointer to move right
        for i in range(point,C-point):
            spiral.append(matrix[point][i])
        #a simple check to see if we already done
        if len(spiral)==total_int:
            return spiral
        #else move down
        for row in range(point+1,len(matrix)-point):
            integer = matrix[row][C-1-point]
            spiral.append(integer)
        # again check if we are done
            if len(spiral)==total_int:
                return spiral
        #now after moving down following the shape of spiral
        # we should move left
        for num in range(C-point-1,point,-1):
            row_num=matrix[R-1-point]
            spiral.append(row_num[num-1])
        #check
        if len(spiral)==total_int:
            return spiral
        # lastly we move up
        for i in range(R-2-point,point,-1):
            row_num=matrix[i]
            integer=matrix[i][point]
            spiral.append(integer)
        if len(spiral)==total_int:
            return spiral
        point+=1
    return spiral
# m=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# r=3
# c=4
# print(spirallytraverse(m,r,c))