# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

with open('rosalind_dna.txt', 'r') as file:
    dna = file.read().rstrip()

nucleotides = {}

for nucleotide in dna:
    if nucleotide in nucleotides:
        nucleotides[nucleotide] = nucleotides[nucleotide] + 1
    else:
        nucleotides[nucleotide] = 1

print(nucleotides['A'], ' ', nucleotides['C'], ' ', nucleotides['G'], ' ', nucleotides['T'])