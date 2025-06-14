 🧬 MTHFR SNP Analysis – Bioinformatics Project

This project analyzes two clinically significant SNPs in the **MTHFR gene** using Python tools.

## 🚀 Summary

- ✅ Gene sequence extraction (NCBI Entrez)
- ✅ Codon context identification of SNPs
- ✅ Population-based SNP frequency plotting
- ✅ Functional effect prediction using Ensembl VEP API (SIFT, PolyPhen)

## 📊 SNPs Analyzed

- `rs1801133 (C677T)`
- `rs1801131 (A1298C)`

## 📦 Tools & Libraries

- Biopython
- pandas
- matplotlib
- Ensembl REST API
- Jupyter Notebook

## 📁 Files

- `fetch_mthfr_seq.py`: Fetches full gene sequence
- `mthfr_codon_context.py`: Finds codon of SNPs
- `mthfr_snp_analysis.py`: Plots SNP frequencies
- `snp_impact.py`: Predicts variant impact via Ensembl API
- `mthfr_snp_freq.csv`: Population frequency data
- `MTHFR_SNP_Analysis.ipynb`: Combined pipeline (optional)

## 📚 Results
- rs1801133 → Missense variant (Ala→Val), probably damaging
- rs1801131 → Missense variant (Glu→Ala), tolerated

## 📎 Author
Muhammad Zafran ul Haq

