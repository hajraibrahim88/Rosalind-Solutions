#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:09:17 2024

@author: hajraibrahim
"""

def resteriction(DNA):
    Result = []
    for nuc in range(len(DNA)-4):
        length = 3
        while length != 14:
            length += 1
            if (length + nuc) > len(DNA):
                continue
            reverse = DNA[nuc:nuc+length].replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
            reverse = reverse.upper()
            relist = list(reverse)
            relist.reverse()
            reverse = ''.join(relist)
            if DNA[nuc:nuc+length] == reverse:
                Result.append([nuc+1,length])
    for i in range(len(Result)):
        seq = str(Result[i][0]) + ' ' + str(Result[i][1])
        print(seq)

with open('rosalind_revp.txt','r') as file:
    content = file.read()
DNA = ''
for i in range(1,len(content.splitlines())):
    DNA += content.splitlines()[i]
resteriction(DNA)