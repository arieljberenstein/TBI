#!/bin/bash
seqpath = '/data/EBV/byACCIDs/'
for i in {'AllseqsUnderto150k_withRef','test_secs'};
do
# create output folder 
mkdir /data/EBV/msas/$i/
outpath = /data/EBV/msas/$i/
## harcoded paths to outputfiles
echo merging fasta files for group $i;
input=/data/EBV/seqGroups/$i.txt
outfa=$outpath$i.fa;
outclust=$outpath$i.clustal;

sudo python /home/ariel/repo/TBI/EBV-db/src/cat-fasta-files.py --idfile=$input --path=$seqpath --outputfile=$outfa;
echo runing msa-mafftfor group $i;
sudo mafft --clustalout --thread 4 $outfa > $outclust;

echo runing rate4site
sudo rate4site -s $outclust -t $outclust -o $outpath$i_rate4site.res

done


