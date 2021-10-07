'''
import sys
sys.path.append("/home/eldull/Projects/Programming/Rosalind")
from helpers import read_data,write_data
'''
codon_table = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S','CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y','CAU':'H','AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D','UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E','UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R','AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G','UGG':'W','CGG':'R','AGG':'R','GGG':'G'}
rev_codon_table = {'F':['UUU','UUC'],'L':['CUU','CUC','UUA','CUA','UUG','CUG'],'I':['AUU','AUC','AUA'],'V':['GUU','GUC','GUA','GUG'],'M':['AUG'],'S':['UCU','UCC','UCA','UCG','AGU','AGC'],'P':['CCU','CCC','CCA','CCG'],'T':['ACU','ACC','ACA','ACG'],'A':['GCU','GCC','GCA','GCG'],'Y':['UAU','UAC'],'H':['CAU','CAC'],'N':['AAU','AAC'],'D':['GAU','GAC'],'Stop':['UAA','UAG','UGA'],'Q':['CAA','CAG'],'K':['AAA','AAG'],'E':['GAA','GAG'],'C':['UGU','UGC'],'R':['CGU','CGC','CGA','AGA','CGG','AGG'],'G':['GGU','GGC','GGA','GGG'],'W':['UGG']}
def read_data(filename, multiline = False):
    with open(filename) as f:
        if multiline == False:
            return f.readline().strip()
        else:
            return [s.strip() for s in f.readlines()]

def write_data(filename, data, multiline = False):
    with open(filename, 'w') as f:
        if multiline:
            f.writelines(data)
        else:
            f.write(data)

def read_fasta(filename):
    dic = {}
    with open(filename) as f:
        data = f.read().split(">")[1:]
    for el in data:
        temp = el.split("\n", 1)
        dic.update({temp[0]:temp[1].replace("\n","")})
    return dic

