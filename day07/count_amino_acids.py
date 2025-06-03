import sys
from Bio import SeqIO
from collections import Counter

fasta_file = sys.argv[1]  

# Define the codon table for translation
codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}

# Reverse the codon table to map codons to amino acids
codon_table_reversed = {codon: amino_acid for amino_acid, codons in codon_table.items() for codon in codons}

def count_amino_acids(fasta_file):
   '''Reads a FASTA file, counts the amino acids in the file,
   and prints the reuslt.'''

   with open(fasta_file, "r") as file:
        
        # Parse the FASTA file and convert the sequence to a string
        for record in SeqIO.parse(file, "fasta"):
            sequence = str(record.seq).upper()
            
            # Trim the sequence to get the length that is a multiple of 3
            trimmed_sequence = sequence[:len(sequence) - (len(sequence) % 3)]

            # Print the length of the old & trimmed sequences
            print(f'Old sequence length: {len(sequence)}\nTrimmed sequence length: {len(trimmed_sequence)}')
            
            # Translate the sequence into amino acids
            translated_sequence = []

            for i in range(0, len(trimmed_sequence), 3):
                codon = trimmed_sequence[i:i+3]
                if codon in codon_table_reversed:
                    translated_sequence.append(codon_table_reversed[codon])
            
            # Count the amino acids in the translated sequence & print the results
            counts = Counter(translated_sequence)
            print("----\nAmino Acid Counts:")
            for amino_acid, count in counts.most_common():
                print(f"{amino_acid}: {count}")


count_amino_acids(fasta_file)

