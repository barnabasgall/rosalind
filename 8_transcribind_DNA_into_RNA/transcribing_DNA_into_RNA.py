
#dna = 'TACTGTGGCTATCGTAGCT'
with open('rosalind_rna.txt', 'r') as file:
   dna = file.read().rstrip()

rna = ''
for nucleotide in dna:
    if nucleotide == 'G':
        rna += 'G'
    if nucleotide == 'A':
        rna += 'A'
    if nucleotide == 'C':
        rna += 'C'
    if nucleotide == 'T':
        rna += 'U'

print(rna)