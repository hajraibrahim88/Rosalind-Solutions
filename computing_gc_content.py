#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:10:32 2025

@author: hajraibrahim
"""

from Bio import SeqIO

max_sequence_id = None
max_gc_content = 0
for seq_record in SeqIO.parse("rosalind_gc (2).txt", "fasta"):
    sequence = str(seq_record.seq)
    sequence_id = seq_record.id
    gc_content = (sequence.count("C") + sequence.count("G")) / len(sequence) * 100
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_sequence_id = sequence_id 

print(max_sequence_id)
print(max_gc_content)