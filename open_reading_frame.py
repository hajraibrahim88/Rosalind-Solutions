#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:12:53 2025

@author: hajraibrahim
"""

# Codon to Protein Translation Table
DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

# Translate codon to protein
def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE:
        protein = DNA_CODON_TABLE[codon]
    return protein

# Reverse complement the DNA string
def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

# Find all possible protein strings from the DNA sequence
def possible_protein_strings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translate_codon(s[i:i+3])
        if protein and protein == 'M':  # Start codon 'M'
            indices.append(i)

    for i in indices:
        found_stop = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = translate_codon(s[j:j+3])

            if not protein:
                break

            if protein == 'Stop':
                found_stop = True
                break

            protein_string += protein

        if found_stop:
            results.append(protein_string)

    return results

# Main function to handle file input and processing
def main(file_path):
    # Read the FASTA file and extract the DNA sequence
    try:
        with open(file_path, 'r') as file:
            dna_sequence = ''.join(line.strip() for line in file.readlines()[1:])  # Skip header
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return

    # Find possible protein strings from the original sequence
    possible_a = possible_protein_strings(dna_sequence)
    
    # Find possible protein strings from the reverse complement
    possible_b = possible_protein_strings(reverse_complement(dna_sequence))
    
    # Combine both results and print unique protein strings
    unique_proteins = set(possible_a + possible_b)
    print("\n".join(sorted(unique_proteins)))

if __name__ == "__main__":
    # Specify the path to the FASTA file
    fasta_file_path = 'rosalind_orf (2).txt'  # Replace with your actual file path

    # Call the main function
    main(fasta_file_path)