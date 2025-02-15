#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:10:59 2025

@author: hajraibrahim
"""


from Bio import SeqIO

def count_matching_reverse_complements(file_path):
    count = 0
    
    for record in SeqIO.parse("rosalind_rvco.txt", "fasta"):
        
        seq = record.seq
        rev_complement = seq.reverse_complement()
        
        
        if seq == rev_complement:
            count += 1
            
    return count


file_path = 'rosalind_rvco.txt'  # Change to the path of your file
result = count_matching_reverse_complements(file_path)

# Output the result
print(result)