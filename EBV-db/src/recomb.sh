#!/bin/bash


modFastas=msas/N.America_msa_gap100.modFasta;
for i in $modFastas ;
do
    python 
    base=$(basename $i);
    group=${base%_msa*};
    mkdir $group;
    convertLDHat -seq $i -prefix $group'/'$group'_';
done


nseqs=16
lkpref='n'$nseqs'_'
lkfile=$lkpref'new_lk.txt'
# notar que el numero de secuencias de esta tabla debe ser el doble (por ser un genoma diploide)
lkgen -lk ./lk_files/lk_n50_t0.1.txt -nseq $nseqs -prefix $lkpref


pairwise -seq $pathToFile -loc $group'/'$group'_locs.txt' -lk $lkfile -prefix $fgroup


'