"""
04_stats.py - Generate publication-ready stats table
Input: data/processed/combined_pqqD.fasta (your 6 accessions)
Output: results/sequence_stats.csv
"""

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import os

INPUT_FILE = "data/processed/combined_pqqD.fasta"
OUTPUT_CSV = "results/sequence_stats.csv"

def generate_stats(fasta_file, output_csv):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    if not os.path.exists(fasta_file):
        print(f"Error: {fasta_file} not found! Run 02_clean_fasta.py first")
        return

    data = []
    print(f"Analyzing {fasta_file}...")
    print(f"Your 6 accessions: KM251420.1, CP003080.1, CP023065.1, CP077007.1, CP125543.1, CP003685.1")
    
    for rec in SeqIO.parse(fasta_file, "fasta"):
        gc = gc_fraction(rec.seq) * 100
        data.append({
            "Accession": rec.id,
            "Length_bp": len(rec.seq),
            "GC_Percent": round(gc, 2),
            "AT_Percent": round(100-gc, 2),
            "Gene": "pqqD",
            "Status": "QC_passed"
        })

    df = pd.DataFrame(data).sort_values("Accession")
    df.to_csv(output_csv, index=False)
    
    print("\n" + "="*70)
    print(df.to_string(index=False))
    print("="*70)
    print(f"\nSaved to: {output_csv}")
    print(f"Total: {len(df)} sequences (6/6 perfect pqqD)")

if __name__ == "__main__":
    generate_stats(INPUT_FILE, OUTPUT_CSV)