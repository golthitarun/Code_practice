#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:15:35 2018

@author: tharunngolthi
"""
import random
def simulateDrop(p,board):
    c = p
    r = 0
    while(r<len(board)-1):
        if (random.getrandbits(1)):
            if (c-1 < 0):
                c = c+1
                r = r+1
            else:
                c = c-1
                r = r+1
        else:
            if (c+1 > len(board[0])):
                c = c-1
                r = r+1
            else:
                c = c+1
                r = r+1
    return c
if __name__ == '__main__':
    board = [[0]*13 for _ in range(0,7)]
    
    for i in range(0,7):
        for j in range(0,13):
            if i%2 != 0:
                if j%2 != 0:
                    board[i][j] = "X"
            if i%2 == 0:
                if j%2 == 0:
                    board[i][j] = "X"
    

    values = (250,500,0,2000,0,500,250)
    for i in range(0,4):
        InitialColumn = random.randint(0,6)
        
        index = simulateDrop(InitialColumn*2, board)
        print ("Trial",i+1,"with Initial Columns :",InitialColumn,", Ends in bucket with value : ",values[index//2])

    