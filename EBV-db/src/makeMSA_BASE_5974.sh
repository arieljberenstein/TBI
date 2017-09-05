#!/bin/bash

for i in {'AllseqsUnderto150k_withRef','test_secs'};
do
## harcoded paths to outputfiles
echo merging fasta files for group $i;
input=/data/EBV/seqGroups/$i.txt
outfa=/data/EBV/multiple_fastas/$i.fa;
outclust=/data/EBV/msas/$i.clustal;

sudo python /home/ariel/repo/TBI/EBV-db/src/cat-fasta-files.py --idfile=$input --path='/data/EBV/byACCIDs/' --outputfile=$outfa;
echo runing msa-mafftfor group $i;
sudo mafft --clustalout --thread 4 $outfa > $outclust;
done


