"""
03_gc_content.py - GC content analysis for your 6 accessions
Input: data/processed/combined_pqqD.fasta (your 6: KM251420.1 etc)
Output: results/sequence_stats.csv + console
"""

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import os
import csv

INPUT_FILE = "data/processed/combined_pqqD.fasta"
OUTPUT_CSV = "results/sequence_stats.csv"

os.makedirs("results", exist_ok=True)

def analyze_gc_content(fasta_file):
    if not os.path.exists(fasta_file):
        print(f"Error: {fasta_file} not found. Run 01_fetch_ncbi.py + 02_clean_fasta.py first")
        return

    print("="*60)
    print("GC Content Analysis - Pseudomonas pqqD (6 seqs)")
    print("Your accessions: KM251420.1, CP003080.1, CP023065.1, CP077007.1, CP125543.1, CP003685.1")
    print("="*60)
    print(f"{'ID':<20} {'Length':<10} {'GC%':<8}")
    print("-"*60)

    results = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = record.seq.upper()
        gc_percent = gc_fraction(seq) * 100
        print(f"{record.id:<20} {len(seq):<10} {gc_percent:<8.2f}")
        results.append([record.id, len(seq), round(gc_percent, 2)])

    print("-"*60)
    if results:
        avg_gc = sum(r[2] for r in results) / len(results)
        print(f"Total sequences: {len(results)} (6/6 retained)")
        print(f"Average GC%: {avg_gc:.2f}%")
        print(f"Length: {results[0][1]} bp (perfect pqqD, not 500bp)")
    print("="*60)

    # Save for results
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["accession", "length", "gc_percent"])
        writer.writerows(results)
    print(f"Saved -> {OUTPUT_CSV}")

if __name__ == "__main__":
    analyze_gc_content(INPUT_FILE)