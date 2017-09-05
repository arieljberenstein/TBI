#!/bin/bash
<<<<<<< HEAD

for i in {'AllseqsUpto150k','test_secs'};
=======
seqpath='/data/EBV/byACCIDs/'
for i in "$@";
>>>>>>> 40eac5c8206b95ee365c75b30f218d4c66619716
do
fname=$(basename $i) # remove path
fbname=${fname%.*}   # remove extension

# create output folder 
mkdir /data/EBV/msas/$fbname/
outpath = /data/EBV/msas/$fbname/
## harcoded paths to outputfiles
echo merging fasta files for group $fbname;
input=/data/EBV/seqGroups/$fbname.txt
outfa=$outpath$fbname.fa;
outclust=$outpath$fbname.clustal;

sudo python /home/ariel/repo/TBI/EBV-db/src/cat-fasta-files.py --idfile=$input --path=$seqpath --outputfile=$outfa;
echo runing msa-mafftfor group $fbname;
sudo mafft --clustalout --thread 4 $outfa > $outclust;

echo runing rate4site
sudo rate4site -s $outclust -t $outclust -o $outpath$fbname_rate4site.res

done


