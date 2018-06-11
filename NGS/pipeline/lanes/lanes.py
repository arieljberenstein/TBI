import os
import glob
import argparser 

def parseargs():
    parser = argparse.ArgumentParser(description='generate lane file paths by sample')
    parser.add_argument('--fastq_folder','-f', dest='fastq_folder',action='store',required = True,help='an integer for the accumulator')
    parser.add_argument('--sep','-s',dest='sep',action= 'store',required = False, default =  '_', help =  'Sample separator in Fastqfile names')
    args = parser.parse_args()
    return args

    
if __name__ = '__main__':
    args = parseargs()
    fastq_folder, sep = args.fastq_folder,args.sep
    files = glob.glob(fastq_folder+'*')
    samplenames = [f.split(sep)[0] for f in files]
    print samplenames
