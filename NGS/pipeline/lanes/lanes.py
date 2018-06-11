import os
import glob
import argparse
import fnmatch
import subprocess 

def parseargs():
    parser = argparse.ArgumentParser(description='generate lane file paths by sample')
    parser.add_argument('--fastq_folder','-f', dest='fastq_folder',action='store',required = True,help='an integer for the accumulator')
    parser.add_argument('--sep','-s',dest='sep',action= 'store',required = False, default =  '_', help =  'Sample separator in Fastqfile names')
    parser.add_argument('--fastq_extension','-e',dest='fastq_extension',action= 'store',required = False, default =  'fastq', help =  'Fastqfile extension')

    args = parser.parse_args()
    return args

def get_samplenames(files):
    samplenames = [os.path.basename(f).split(sep)[0] for f in files]
    samplenames = list(set(samplenames)) # drop duplicates
    return samplenames
    


def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

def look_for_sample_paths_and_write_to_disk(samplenames,fastq_extension):
    for sample in samplenames:
        r1 = recursive_glob(treeroot= fastq_folder, pattern='%s*R1*%s'%(sample,fastq_extension))
        r2 = recursive_glob(treeroot= fastq_folder, pattern='%s*R2*%s'%(sample,fastq_extension))
        with open(outputfolder+sample+'_R1.txt','wb') as fr1:
            for line in r1:
                fr1.write(line+'\n')
        fr1.close()        
        with open(outputfolder+sample+'_R2.txt','wb') as fr2:
            for line in r2:
                fr2.write(line+'\n')
        fr2.close()

def uncompress_gz(fastq_extension):
    ff = recursive_glob(treeroot= fastq_folder, pattern='*%s.gz'%fastq_extension)
    for f in ff:
        subprocess.call(["gzip", "-dk",f])
    uncompressed = [f.split('gz')[0] for f in ff]
    return(uncompressed)




if __name__ == '__main__':
    args = parseargs()
    fastq_folder, sep, fastq_extension = args.fastq_folder,args.sep,args.fastq_extension
    files = glob.glob(fastq_folder+'*')
    samplenames = get_samplenames(files)
    
    print 'uncompressing files'
    uncompressed = uncompress_gz(fastq_extension)

    outputfolder = '%slanes_samplepath/'%fastq_folder
    if not os.path.exists(outputfolder):
        os.mkdir(outputfolder)        

    look_for_sample_paths_and_write_to_disk(samplenames,fastq_extension)
    ## gaurdo nombres de archivos descomprimidos para despues de correr el pipeline borrarlos y liberar espacio.
    with open(outputfolder+'uncompressed_files.txt','wb') as f:
        for line in uncompressed:
            f.write(line +'\n')
    f.close()
        
    print 'output is located in the path: \n %s'%outputfolder 
            
        