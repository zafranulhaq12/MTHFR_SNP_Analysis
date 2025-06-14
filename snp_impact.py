import sys
sys.stdout.reconfigure(line_buffering=True)

import requests

def get_vep_info(rsid):
    server = "https://rest.ensembl.org"
    ext = f"/vep/human/id/{rsid}?"
    headers = {"Content-Type": "application/json"}

    try:
        r = requests.get(server + ext, headers=headers, timeout=10)  # Timeout added
        print(f"Status for {rsid}: {r.status_code}")
        if r.status_code != 200:
            print(f"Failed to fetch data for {rsid}: {r.text}")
            return

        data = r.json()
        print(f"\n--- {rsid} ---")
        for entry in data[0].get("transcript_consequences", []):
            print("Gene:", entry.get("gene_symbol", ""))
            print("Consequence:", entry.get("consequence_terms", ""))
            print("Amino acid change:", entry.get("amino_acids", ""))
            print("Codons:", entry.get("codons", ""))
            print("SIFT:", entry.get("sift_prediction", ""))
            print("PolyPhen:", entry.get("polyphen_prediction", ""))
            print("-" * 30)

    except requests.exceptions.Timeout:
        print(f"⏱️ Request for {rsid} timed out.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

# SNPs to test
get_vep_info("rs1801133")
get_vep_info("rs1801131")
