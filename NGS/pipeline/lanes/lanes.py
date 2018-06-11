import os
import glob
import argparse
import fnmatch


def parseargs():
    parser = argparse.ArgumentParser(description='generate lane file paths by sample')
    parser.add_argument('--fastq_folder','-f', dest='fastq_folder',action='store',required = True,help='an integer for the accumulator')
    parser.add_argument('--sep','-s',dest='sep',action= 'store',required = False, default =  '_', help =  'Sample separator in Fastqfile names')
    args = parser.parse_args()
    return args

def get_samplenames():
    samplenames = [os.path.basename(f).split(sep)[0] for f in files]
    samplenames = list(set(samplenames)) # drop duplicates
    return samplenames
    


def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

if __name__ == '__main__':
    args = parseargs()
    fastq_folder, sep = args.fastq_folder,args.sep
    files = glob.glob(fastq_folder+'*')
    samplenames = get_samplenames()
    outputfolder = '%slanes_samplepath/'%fastq_folder
    if not os.path.exists(outputfolder):
        os.mkdir(outputfolder)        

    for sample in samplenames:
        r1 = recursive_glob(treeroot= fastq_folder, pattern='%s*R1*gz'%sample)
        r2 = recursive_glob(treeroot= fastq_folder, pattern='%s*R2*gz'%sample)
        with open(outputfolder+sample+'_R1.txt','wb') as fr1:
            for line in r1:
                fr1.write(line+'\n')
        fr1.close()        
        with open(outputfolder+sample+'_R2.txt','wb') as fr2:
            for line in r2:
                fr2.write(line+'\n')
        fr2.close()
            
        