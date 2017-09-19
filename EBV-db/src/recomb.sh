#!/bin/bash



fastas=~/Projects/Gutierrez/EBV-db/recomb/msas/SAmerica_msa_gap100.fa;
output_dir=
group=
for msa in $fastas;
do
    python get_mod_fasta_format.py --msafile=$msa
    auxpath=${msa%.fa};
    modFasta=$auxpath'.modFasta'
    base=$(basename $modFasta);
    group=${base%_msa*};
    #convertLDHat -seq $i -prefix $group'/'$group'_';
done


#nseqs=16
#lkpref='n'$nseqs'_'
#lkfile=$lkpref'new_lk.txt'
# notar que el numero de secuencias de esta tabla debe ser el doble (por ser un genoma diploide)
#lkgen -lk ./lk_files/lk_n50_t0.1.txt -nseq $nseqs -prefix $lkpref


#pairwise -seq $pathToFile -loc $group'/'$group'_locs.txt' -lk $lkfile -prefix $fgroup


