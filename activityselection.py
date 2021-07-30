# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:58:48 2021

@author: M Shoaib
"""
def activityselection(start,end,N):
    
    for i in range(1,N):
        s1=start[i]
        s2=end[i]
        j=i-1
        while j>=0 and s2<end[j]:
            end[j+1]=end[j]
            start[j+1]=start[j]
            j-=1
            end[j+1]=s2
            start[j+1]=s1
        total_act=0
        total_count=1
        for i in range(1,N):
            if start[i]>=end[total_act]:
                total_count=total_count+1
                total_act=i
        return total_count
        
Start=[2,1]
End=[2,2]
n=2
print(activityselection(Start,End,n))





