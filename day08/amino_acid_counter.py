from Bio import SeqIO
from collections import Counter

# Codon table mapping
codon_table = {
    'Phe': ['TTT', 'TTC'], 'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'], 'Met': ['ATG'], 'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'], 'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'], 'His': ['CAT', 'CAC'], 'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'], 'Lys': ['AAA', 'AAG'], 'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'], 'Cys': ['TGT', 'TGC'], 'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Reverse codons to amino acids
codon_to_aa = {codon: aa for aa, codons in codon_table.items() for codon in codons}

def parse_fasta_sequence(fasta_file):
    with open(fasta_file, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequence = str(record.seq).upper()
            trimmed = sequence[:len(sequence) - len(sequence) % 3]
            return sequence, trimmed

def translate_sequence(sequence):
    amino_acids = [
        codon_to_aa.get(sequence[i:i+3])
        for i in range(0, len(sequence), 3)
        if codon_to_aa.get(sequence[i:i+3])
    ]
    return amino_acids

def count_amino_acids(amino_acids):
    return Counter(amino_acids)
