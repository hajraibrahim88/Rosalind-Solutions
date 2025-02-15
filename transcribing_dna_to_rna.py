#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:12:08 2025

@author: hajraibrahim
"""

def transcribe_dna_to_rna(file_path):
    
    with open(file_path, "r") as file:
        
        sequence = file.read().strip().splitlines()[-1]
        
    
    rna_sequence = sequence.replace('T', 'U')
    
   
    print(rna_sequence)


file_path = 'rosalind_rna.txt'  
transcribe_dna_to_rna(file_path)