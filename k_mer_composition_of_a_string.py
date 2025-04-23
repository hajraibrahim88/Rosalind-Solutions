#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:12:32 2025

@author: hajraibrahim
"""

def reconstruct_string(pairs, d):
    # Start with the first k-mer (ai part of the first pair)
    result = pairs[0][0]
    
    # Loop through each subsequent pair
    for i in range(1, len(pairs)):
        ai, bi = pairs[i]  # Get the current (k, d)-mer (ai | bi)
        
        # Append the suffix of ai (last d characters) to the result string
        result += ai[-d:]  # Take the last d characters from ai
    
    # Add the suffix of the last bi (last d characters) to the result string
    result += pairs[-1][1][-d:]  # Only take the last d characters from the last bi
    
    return result


# Example dataset (pairs of (ai | bi))
pairs = [
    ("GACC", "GCGC"),
    ("ACCG", "CGCC"),
    ("CCGA", "GCCG"),
    ("CGAG", "CCGG"),
    ("GAGC", "CGGA")
]

# Set d (overlap length)
d = 2

# Call the function to reconstruct the string
reconstructed_string = reconstruct_string(pairs, d)

# Output the result
print(reconstructed_string)
