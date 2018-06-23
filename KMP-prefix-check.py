#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:05:48 2018

@author: tharunngolthi
"""

s = input()
dp = [0]*len(s)
j = 0
i = 1
while(i<len(s)):
    if(s[j]==s[i]):
        dp[i] = j+1
        j+=1
        i+=1
    else:
        if(j!=0):
            j = dp[j-1]
        else:
            dp[i]=0
            i+=1
    
print(dp)