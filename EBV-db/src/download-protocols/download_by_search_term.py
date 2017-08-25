from __future__ import print_function
from Bio import Entrez
import pandas as pd
import time
from os import listdir
from os.path import isfile, join
import argparse


parser = argparse.ArgumentParser(description='Download NCBI sequences using an explicit search_term')

parser.add_argument('-s','--search_term',required=True)
parser.add_argument('-o','--outputpath',required=True)
parser.add_argument('-r','--retmax',default = 2)

args = parser.parse_args()

#args = parser.parse_args()
search_term = args.search_term
outputpath = args.outputpath
RetMax = args.retmax

def main():
    handle = Entrez.esearch(db='nucleotide', term=search_term,RetMax = RetMax)
    genome_ids = Entrez.read(handle)['IdList']
    file_search_mapp =  outputpath + 'idList'+  search_term + '.txt'

    with open(file_search_mapp, 'w') as g:
        g.write('search_term : {} \n'.format(search_term))
        g.write("\n".join(genome_ids))
        g.write("\n")

    for genome_id in genome_ids:
        record = Entrez.efetch(db="nucleotide", id=genome_id, rettype="gb", retmode="text")

        filename = '{}genBankRecord_{}.gb'.format(outputpath,genome_id)
        print('Writing:{}'.format(filename))
        with open(filename, 'w') as f:
            f.write(record.read())
        
if __name__ == "__main__":
    main()
