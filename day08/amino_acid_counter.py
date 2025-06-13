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
    """
    Parses a FASTA file and returns the full sequence and a trimmed version that is a multiple of 3 in length.
    fasta_file: Path to the FASTA file.
    returns: Tuple containing the full sequence and the trimmed sequence.
    """
    with open(fasta_file, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequence = str(record.seq).upper()
            trimmed = sequence[:len(sequence) - len(sequence) % 3]
            return sequence, trimmed

def translate_sequence(sequence):
    """
    Translates a nucleotide sequence into a list of amino acids.
    sequence: Nucleotide sequence as a string.
    returns: List of amino acids represented by their three-letter codes.
    """
    amino_acids = [
        codon_to_aa.get(sequence[i:i+3])
        for i in range(0, len(sequence), 3)
        if codon_to_aa.get(sequence[i:i+3])
    ]
    return amino_acids

def count_amino_acids(amino_acids):
    """
    Counts the occurrences of each amino acid in a list.
    amino_acids: List of amino acids represented by their three-letter codes.
    returns: Counter object with amino acid counts.
    """
    return Counter(amino_acids)
