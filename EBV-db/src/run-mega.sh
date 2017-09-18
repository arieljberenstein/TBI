#!/bin/bash

#obs=PI-d # observable to compute
#group=SAmerica #group to analyze

    for maofile in /home/ariel/Projects/Gutierrez/EBV-db/MEGA/maofiles/rate-site*.mao;
    do
#        for group in {'Africa','Europe','N.America','Asia','Oceania','SAmerica'};
        for group in {'IM','Healty','pathol','HealtyIm'};
        do
            fname=$(basename $maofile); # remove path
            
            fbname=${fname%.*};   # remove extension
            echo 'group  '$group
            echo 'analysis '$fbname

            
            input=/data/EBV/msas/$group/$group'_msa_gap100.fa'
            out='/home/ariel/Projects/Gutierrez/EBV-db/MEGA/'$group/$fbname
            #run
            megacc -a $maofile -d $input -o $out
        done
    done


