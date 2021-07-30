# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:29:04 2021

@author: M Shoaib
"""


def candyStore(candies,n,k):
    if n>k>0:
        #sorting array is important
        candies.sort()
        #main formula
        c=int(n%(k+1)!=0)
        c+=n//(k+1)
        #calculating minimum
        mini=sum(candies[0:c:1])
        #calculating maximum
        maxi=sum(candies[-1:n-c-1:-1])
    return mini,maxi


# l=[3,2,1,4]
# n=4
# k=2
# print(candyStore(l,n,k))
