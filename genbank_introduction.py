#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:13:24 2025

@author: hajraibrahim
"""

from Bio import Entrez

def get_Nucleotide_GenBank_entries(genus_name, date1, date2):
    # Use a generic email if you don't want to use your own
    Entrez.email = "no-reply@example.com"
    
    # Create the search term to query Nucleotide GenBank entries
    term = f'"{genus_name}"[Organism] AND "{date1}"[Publication Date] : "{date2}"[Publication Date]'
    
    # Perform the search query on GenBank's Nucleotide database
    handle = Entrez.esearch(db="nucleotide", term=term)
    
    # Read the results as a dictionary
    records = Entrez.read(handle)
    
    # Close the handle after reading
    handle.close()
    
    # The count of entries is in the 'Count' field of the result
    return records["Count"]

if __name__ == "__main__":
    # Read input data (genus name and two dates)
    with open("rosalind_gbk.txt", "r") as f:
        genus_name = f.readline().strip()  # Genus name
        date1 = f.readline().strip()  # Start date
        date2 = f.readline().strip()  # End date
    
    # Get the number of Nucleotide GenBank entries for the genus published within the date range
    count = get_Nucleotide_GenBank_entries(genus_name, date1, date2)
    
    # Print the result
    print(count)