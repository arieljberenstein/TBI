from __future__ import print_function
from Bio import Entrez
import pandas as pd
import time
from os import listdir
from os.path import isfile, join
import argparse

parser = argparse.ArgumentParser(description='Download NCBI sequences using an accesion id file list')

parser.add_argument('-i','--inputfile',required=True)
parser.add_argument('-o','--outputpath',required=True)
args = parser.parse_args()

#args = parser.parse_args()
inputfile = args.inputfile
outputpath = args.outputpath

accession_ids = pd.read_csv(inputfile)


def download_accIds_from_list(list_of_accession_ids,outputfile = './output.gb',address = "arieljberenstein@gmail.com"):
    Entrez.email =address
    genomeAccessions = list_of_accession_ids

    search           = " ".join(genomeAccessions)
    handle           = Entrez.read(Entrez.esearch(db="nucleotide", term=search, retmode="xml"))
    genomeIds        = handle['IdList']
    records          = Entrez.efetch(db="nucleotide", id=genomeIds, rettype="gb")

    file_out = open(outputfile, "w")    # store each genomes .gb in separate files
    file_out.write(records.read())
    file_out.close()
    return None
    

def main():
    IDs = accession_ids.iloc[:,0].tolist()
    outputfile = outputpath + inputfile + '.gb'
    download_accIds_from_list(IDs,outputfile = outputfile)
    

if __name__ == "__main__":
    main()



