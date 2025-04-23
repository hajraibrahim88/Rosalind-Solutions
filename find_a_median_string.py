#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:56:23 2025

@author: hajraibrahim
"""

def MinHammingDistance(pattern, string):
    min_distance = len(pattern)
    for i in range(len(string) - len(pattern) + 1):
        distance = sum([1 for j in range(len(pattern)) if pattern[j] != string[i:i+len(pattern)][j]])
        if distance < min_distance:
            min_distance = distance
    return min_distance

def GenerateArray(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def FindMedianString(k, dna):
    pattern = GenerateArray(k)
    distance_of_pattern_dna = {}
    min_string = len(dna) * len(pattern)
    for i in pattern:
        sum_distance = 0
        for j in range(len(dna)):
            sum_distance += MinHammingDistance(i, dna[j])
        distance_of_pattern_dna[i] = sum_distance
        if sum_distance < min_string:
            min_string = sum_distance
    for t in distance_of_pattern_dna.keys():
        if distance_of_pattern_dna[t] == min_string:
            print(t)

if __name__ == "__main__":
    with open("rosalind_ba2b.txt", "r") as f:
        k = int(f.readline().strip())
        dna = [line.strip() for line in f]
    FindMedianString(k, dna)
