"""
02_clean_fasta.py - Combine + QC your 6 accessions
Input: data/raw/*.fasta (6 files: KM251420.1 etc)
Output: data/processed/combined_pqqD.fasta + aligned_pqqD.fasta
"""

from Bio import SeqIO
import os
import glob

RAW_DIR = "data/raw"
COMBINED = "data/processed/combined_pqqD.fasta"
ALIGNED = "data/processed/aligned_pqqD.fasta"

os.makedirs("data/processed", exist_ok=True)

cleaned = []
# Read all 6 raw files you created with 01_fetch_ncbi.py
for fasta_file in glob.glob(f"{RAW_DIR}/*.fasta"):
    for rec in SeqIO.parse(fasta_file, "fasta"):
        seq = str(rec.seq).upper()
        # QC: keep 200-400bp, <5% Ns (real pqqD is 276bp)
        if 200 <= len(seq) <= 400 and seq.count("N")/len(seq) < 0.05:
            cleaned.append(rec)

# Sort by ID to keep order same as your tree
cleaned = sorted(cleaned, key=lambda x: x.id)

# Save combined
SeqIO.write(cleaned, COMBINED, "fasta")
# For now aligned = combined, 04 will align properly
SeqIO.write(cleaned, ALIGNED, "fasta")

print(f"Raw: {len(glob.glob(f'{RAW_DIR}/*.fasta'))} files in {RAW_DIR}")
print(f"Cleaned: {len(cleaned)} sequences -> {COMBINED}")
for rec in cleaned:
    print(f"  {rec.id}: {len(rec.seq)} bp")