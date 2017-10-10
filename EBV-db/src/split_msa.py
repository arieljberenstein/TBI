import argparse   
import pandas as pd
import os
from Bio import AlignIO 
from Bio import SeqIO
import numpy as np




parser = argparse.ArgumentParser(description='cut a msa file in fasta format')
if(True):
    parser.add_argument('-m','--msapath',required=True,help='msa file in fasta format')
    parser.add_argument('-s','--start',required=True,help='end coordinate',type=int)
    parser.add_argument('-e','--end',required=True,help='end coordinate',type=int)

    args = parser.parse_args()
    msapath = args.msapath
    refseq = args.start
    outputfile = args.end


msa = AlignIO.read(msapath,'fasta')
base = os.path.basename(msapath)

st = args.start
end = args.end


#if not os.path.isdir(outputpath):
#    os.system('mkdir %s'%outputpath)
    
if(end > st):
    cutted = msa[:,int(st-1):int(end-1)] # biopython start from 0 !!
    output = msapath+'_'+str(st)+'_'+str(end)+'.fa'
    AlignIO.write(cutted,output,'fasta')

else:
    last = msa.get_alignment_length()
    cut_first = msa[:,int(st-1):(last-1)] # biopython start from 0 !!
    cut_second =msa[:,0:int(end-1)]
    cutted = cut_first + cut_second
    output = msapath+'_'+str(st)+'_'+str(end)+'.fa'
    AlignIO.write(cutted,output,'fasta')

    