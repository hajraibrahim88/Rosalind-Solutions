#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:08:46 2025

@author: hajraibrahim
"""

# Function to count the nucleotides
def count_nucleotides(file_path):
    # Open the file and read the sequence (ignoring the header)
    with open(file_path, "r") as file:
        # Read the content (skip the first line if it's a header)
        sequence = file.read().strip().splitlines()[-1]
        
    # Count occurrences of each nucleotide
    a_count = sequence.count('A')
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    t_count = sequence.count('T')
    
    # Print the result in the required format
    print(a_count, c_count, g_count, t_count)

# Main part of the program
file_path = 'rosalind_ini (11).txt'  # Change to the correct file path if needed
count_nucleotides(file_path)
