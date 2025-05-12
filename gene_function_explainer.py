from Bio import Entrez

Entrez.email = "your@email.com"  # Replace with your email

gene = input("Enter a gene name (e.g., BDNF, DRD4, COMT): ")

handle = Entrez.esearch(db="gene", term=f"{gene}[sym] AND Homo sapiens[orgn]")
record = Entrez.read(handle)
handle.close()

if record["IdList"]:
    gene_id = record["IdList"][0]
    handle = Entrez.efetch(db="gene", id=gene_id, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    print(f"Function of {gene}:")
    print(records[0]["Entrezgene_summary"])
else:
    print("Gene not found.")
