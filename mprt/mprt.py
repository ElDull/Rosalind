# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import re
def parse_motif(motif):
    """
    Takes a motif and converts it to regex
    """
    motif = motif.replace("{", "[^").replace("}", "]")
    return motif


# %%
motif = parse_motif("N{P}[ST]{P}")


# %%
# Regex Test
import re

#Return a list containing every occurrence of "ai":
def findstr(st, subtxt):
	return re.search(st,subtxt).start()
txt = "The rain in Spain"
idx = 0
locs = []
while idx < len(txt):
	try:
		x = findstr("ai", txt[idx:])
		locs.append(x)
		idx += x+1
	except:
		break


# %%
# Change above function to suit our needs
def find_motif(motif,txt):
	# Find all motif locations in one protein
	idx = 0
	locs = []
	while idx < len(txt):
		try:
			x = findstr(motif, txt[idx:])
			locs.append(idx+x+1)
			idx += x+1
		except AttributeError:
			break
	return locs


# %%
import requests
def fetch_protein(uniprot_id):
    protein = "".join([i for i in requests.get(f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta").text.split("\n")[1:]])
    return protein


# %%
# Example Protein
fetch_protein("A2Z669")


# %%
import sys
sys.path.append("/home/eldull/Projects/Programming/Rosalind")
from helpers import read_data,write_data

prot_list = read_data("input.txt", multiline=True) 
d = dict()
for prot in prot_list:
    p = fetch_protein(prot)
    locs = find_motif(motif, p)
    if locs:
        print(prot)
        for i in locs:
            print(i, end=" ")
        print()
        


