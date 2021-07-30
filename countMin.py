# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:26:47 2021

@author: M Shoaib
"""

def countMin(string):
    l=len(string)
    #performing a dynamic approach
    app = [[0]*l for i in range(l)]
    #will check for the toatl rift
    for dif in range(1,l):
        i=0
        for j in range(dif,l):
                
            if dif==1:
                
                
                if string[i]==string[j]:
                    app[i][j]=0
                else:
                    app[i][j]=1

            else:
                if string[i]==string[j]:
                    app[i][j]=app[i+1][j-1]
                else:
                    #app[i][j]=1+min(app[i][j+1],app[i-11][j])
                    app[i][j]=1+min(app[i][j-1],app[i+1][j])

            i+=1
        
    return app[0][-1]
#print(countMin('abcd'))
