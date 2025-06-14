from Bio import Entrez, SeqIO

Entrez.email = "zafranulhaq06@gmail.com"

# Fetch MTHFR mRNA (not entire chromosome)
handle = Entrez.efetch(db="nucleotide", id="NM_005957.5", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

# Print part of the sequence and a codon
mthfr_seq = record.seq
print("Full sequence length:", len(mthfr_seq))

# Let's get codon around position 677 (1-based)
coding_pos = 677 - 1  # zero-indexed
print("Wild type codon:", mthfr_seq[coding_pos-1:coding_pos+2])  # Show codon
